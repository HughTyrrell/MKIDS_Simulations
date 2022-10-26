# MKIDS_Simulations
## Background
This script allows the user to simulate a signal consisting of a pulse and some background noise. 
The three types of pulse currently allowed are a gaussian, a sinc function, and a discontinuous function with an exponential rise and an exponential decay. 
The options for noise characteristics include gaussian noise, uniformly random noise, a constant ‘drift’ or slope, and periodic noise. 
The purpose of the script is to generate data whose ground truth is known, to test analysis tools

## How to use the script
When the script is run, it starts out by asking the user for the number of data points equally spaced on the x-axis, as well as the sampling frequency of them. These numbers must both be greater than zero. The user is then prompted to select the shape of the pulse from three options:

If “g” is given, the user then is prompted to give the amplitude, standard deviation and mean/centre of a gaussian function.

If “de” is given, the user is prompted to give the height, decay constant, centre, and growth constant of a function that rises exponentially and then falls exponentially. 

If “s” is given, the user must then provide the amplitude, phase/centre and frequency of a “sinc” function (sin x /x). 

If the user inputs anything other than a number, they are prompted to try again. 

The user is then asked if they would like to include periodic noise. If “y” is chosen, the user gives the amplitude, frequency and phase of a sin function. They will then be asked again if they would like to include periodic noise - if they choose “y” again, the second function they define will be added to the first. This continues until they type “n”. Once “n” is typed, the script moves to the next question. 

The user can then choose to add a “drift” or a slope to the background noise. They are prompted to give a value for that slope. Again, it must be a number. 

The user can finally choose between random background noise with a gaussian distribution, or with a uniform distribution within a certain margin above and below the mean. In both cases the noise is symmetrically distributed above and below the mean. The user is asked to define this mean or “offset”, which can be zero if they want. The offset simply shifts all data up or down the y-axis by a constant amount. 

If the user chooses gaussian noise, they will be asked for the standard deviation of noise from the mean. 

If the user chooses uniform noise, they will be asked for the maximum deviation of noise from the mean. For example, if the user chooses an offset of 1, and max deviation of 0.5, the background noise will be evenly, randomly distributed between 0.5 and 1.5 (except in the regime of the pulse). 

If the user just wants a pulse and no noise, they can simply set the standard devation/max deviation to 0. 

The user is then asked if they would like to save the data and plot. If “y” is chosen, they’ll be asked to input a path to the directory to save it in. The plot is then saved as a .png and the data as a .csv. 

## Output
The script produces a plot of the signal as well as its numerical data. Both can be saved if the user chooses to do so. 
