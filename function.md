## What the script does
The script allows a user to simulate a signal consisting of a pulse and some noise added to it, and allows the user to define the characteristics of these. The plot and data can then be saved to a directory of the user’s choosing. 

## Intended use
The script is expected to be used to test tools for analysing signals. We can design signals and know the ground truth of their characteristics, and then test if analysis tools return the same result.

## How it works
The script is triggered by an `if __name__ == "__main__"` statement. `main()` calls the output of `generate_data()` to define `time_data`, a list of evenly spaced points in time, and `data`, the corresponding signal amplitudes for each point in time. 

In a while loop, `generate_data()` asks the user for the duration of the simulated signal in seconds, and the sampling frequency. The loop doesn’t break until a positive number is entered for each. The main purpose of generate_data() is to combine the pulse and the noise, by using np.add to combine pulse_data() and the combined noise functions. Np.add sums the corresponding elements of two equally shaped arrays to create a third. The implication of this method, is that if the user doesn’t want to include a certain kind of noise, the function must return an array of N zeros. The noise functions are combined in `generate_data()` two at a time using np.add. `generate_data()` returns the signal in the form of a time array and an array of associated y-values. 

`pulse_func()` asks the user to choose between a Gaussian shaped pulse, a sinc function and a discontinuous pulse with exponential rise and exponential decay. The prompt asks the user to type “g”, “de” and “s”, although there is some leeway with capitalisation and inputting the entire word also being accepted. Once an option is chosen, the corresponding function is returned.

The user is then prompted to provide the parameters of the function they have chosen. Each of the three functions below takes one argument, `x`, and applies the relevant mathematical expression to `x`. If a non-number is input, an exception is raised and the user must try again. In the `double_exp()` function, the growth and decay parameters must also be greater than zero, or the input will not be accepted. The double_exp function works by using a for-loop to add values to a list which is returned at the end, as opposed to the other two functions which simply return the mathematical expression that will be applied to the time array. 

- The expression in `gaussian_func` is defined as $$f(x) = ae^{\frac{(-(x-b))^2}{2c^2}}$$ The parameters $a$, $b$ and $c$ are initialised by the user's response to the prompts `Amplitude: `, `Mean: ` and `Std. dev: ` respectively, and $x$ is the argument of the function.

- In the `double_exp()` function, the curve is calculated as: $$f(x) = ae^{d(x-c)} \text{ if } x < c$$ and $$f(x) = ae^{-b(x-c)} \text{ if } x \geq c$$.
$a$, $b$, $c$ and $d$ are initialised by the user's response to the prompts `Amplitude =`, `Decay parameter = `, `Centre = ` and `Rise parameter = ` respectively.
-  $\text{Sinc}(x)$ is defined mathematically as $\frac{\sin{x}}{x}$, howver to avoid the issue of dividing by zero, I used numpy.sinc, and adjusted it as follows:
$$f(x) = a\times\text{sinc}(2\pi w(x-b))$$ where $a$, $w$ and $b$ where initialised by the user's response to the prompts `Amplitude: `, `Frequency: ` and `Shift: ` respectively. 

`generate_data()` next calls the `noise_distrib()` function, which simply asks the user to choose between uniformly distributed noise and gaussian noise. The user is asked to type `u` or `g`, although some alternate responses are accepted such as capitalising the letter or typing `uniform` or `gaussian` in full. The loop continues until the user has inputted one of the acceptable responses, then it calls the corresponding function: either `gaussian_noise()` or `uniform_noise()`.

- `gaussian_noise()` first asks the user to define an offset, a constant added to the y-value of all data. The user is prompted to input the standard deviation of noise from the mean. Then, `np.random.normal` is used to create a noisy array, with the same dimensions as “x” (the argument of the function);  whose mean is the offset defined above and whose standard deviation is that chosen by the user.

- `uniform_noise()` acts similarly to gaussian_noise. It uses `np.random.uniform` to create an array of values evenly spaced between some upper and lower bound, with the same shape as “x”, the argument of the function. The user is asked for an offset and the max difference from this offset a value can take. `np.random.uniform` takes an upper and lower bound, which are defined as `high = offset + max difference`, and `low = offset - max difference`, respectively. 

The offset in the above two functions is defined by calling `offset()`, a very simply function which asks the user for a value and returns it. It uses a while loop and `try...except` syntax to ensure that the input is a number.

The next function referenced by `generate_data()` is `drift_noise()`, as it adds it to `noise_distrib()`. `drift_noise()` asks the user if they want to include a background drift, ie. a slope applied to all the data. If not, it returns an array of zeros, the same dimensions as its argument. This is necessary due to the `np.add()` in `generate_data()`, which must combine arrays of the same length. If the user chooses to include drift, then `drift_func()` is called. 

`drift_func()` takes `x` as an argument, asks the user for a slope, and then returns `x*slope`.

Next in `generate_data()`, `periodic_noise()` is added to the sum of `noise_distrib()` and `drift_noise()`. `periodic_noise()` takes one argument (`x`) and outputs an array of the same dimension as `x`, conisting of one or more periodic signals added together. It starts by initiating an array of zeros, called `arr1`, the same length as `x`. In a while loop, it asks the user if they would like to include periodic noise.

- If the response is `n`, the original array of zeros `arr1` is returned and the loop breaks. 
- If the response is `y`,`periodic_func()` is called and the resulting sine wave added to `arr1`. A new while loop opens, and the user is asked if want to include more periodic noise. If so, `periodic_func()` is called again and the result added to `arr1`. The loop repeats until `n` is received as a response, at which point `arr1` is returned as the output of the function.

`periodic_func()` takes one argument `x` and produces an array with the same dimensions as `x`, with each value passed through the sine function $$A\sin{2\pi w (x-b)}$$, with the parameters $A$, $w$ and $b$ chosen by the user as the inputs for the prompts `Amplitude: `, `Frequency: ` and `Shift: ` respectively. It uses `numpy.sin`. 

`generate_data()` adds the output of `noise_distrib()` (either Gaussian or uniform noise) to the output of `drift_noise()` using `np.add`. Then it adds `periodic_noise()` to the result of this. Finally, it combines this noise with the output of `pulse_func()` and returns this result. 

`plot_data()` is also called from `main()`. It takes two inputs to be plotted against each other. This creates a simple scatter plot using matplotlib.pyplot, with y-axis labelled “Signal strength” and x-axis labelled “Time”. Because no axis limit are set, it automatically resizes to fit the data. 

In a while loop, `save_data()` asks the user if they wish to save the data. If so, the user is then asked for the filepath to the location where the data will be saved. (To save outside the current working directory, this must be an absolute filepath ending with ‘/’.) It uses pandas to save the raw data in two columns in a .csv file, and saves the plot as a .png. 



