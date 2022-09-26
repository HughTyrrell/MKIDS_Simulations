#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:50:57 2022

@author: hughtyrrell
"""
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

# Three kinds of pulse are defined below:
def gaussian_func(x):
    # loop that asks for variables for Gaussian function
    # ends after valid input
    while True:
        try:
            a, b, c = [int(y) for y in input("Enter mamplitude, mean, std. dev: ").split(",")]
           
        except ValueError:
            print("Three comma seperated values, please")
        else:
            break
    # expression of a gaussian
    return a*np.exp((-(x-b)**2)/(2*c**2))

def double_exp(x):
    # asks for three parameters for a Double Exponential
    while True:
        try:
            a,b,c = [float(y) for y in input("Enter height param, centre, risetime: ").split(",")]
        except ValueError:
            print("Three comma seperated values, please")
        else:
            break
    # expression of double exponential:
    return a*np.exp(-c*np.abs(x-b))

def sinc(x):
    # asks for three parameters to define a sinc function
    while True:
        try :
            A,w,b = [float(y) for y in input("Please enter Amplitude, freq, shift: ").split(",")]
            
        except ValueError:
            print("Three comma seperated values please ")
        else:
            break
    # expresses sinc function using numpy.sinc
    return A*np.sinc(w*(x-b))

def pulse_func(x):
    # asks which one of the above pulses you wish to simulate
    while True:
        distrib_type = input("What form of pulse? (Enter Gausssian, Double Exponential, Sinc): ")
        if distrib_type == "Gaussian":
            return gaussian_func(x)
        elif distrib_type == "Double Exponential":
            return double_exp(x)
        elif distrib_type == "Sinc":
            return sinc(x)
        # Must take exact spelling to exit loop
        else:
            print("Invalid input, please check spelling")
            
            
# four different kinds of noise defined below
def drift_func(x):
    # simple linear function that causes data to drift
    slope = float(input("Slope: "))
    return slope*x

def uniform_noise(x, offset):
    # uniform random noise, depends on offset defined in pulse_func
    while True:
        # define bounds in relation to offset
        try:
            dev = float(input("Enter max dev from mean: "))
            
        except ValueError:
            print("A number, please")
        else:
            break
    
    low = offset - dev, 
    high = offset + dev
    noise = np.random.uniform(low,high,len(x))
    return noise

def gaussian_noise(x,offset):
    # normally distributed random noise
    while True:
        # similar to above, standard deviation 
        # defined wrt offset
        try:
            std_dev = float(input("Enter standard dev from mean of noise: "))
        except ValueError:
            print("Must be a number")
        else: 
            break
    noise = np.random.normal(offset, std_dev, len(x))
    return noise
    
def periodic_func(x):
    # simple sine wave with user defined parameters
    while True:       
        try:
            A, w, b = [float(y) for y in input("Please enter Amplitude, freq, shift: ").split(',')]
            return A*np.sin(w*x - b)
        except ValueError:
            print("Three comma seperated values please ")
        else:
            break
    
def noise_func(x):
    # this function can add either gaussian noise or uniform noise
    # in addition periodic, drift and offset can all be included
    while True: 
        # defines offset used in functions above
        try:
            offset = float(input("Please enter offset: "))
        except ValueError:
            print("Must be a number")
        else: 
            break
    while True:
        # loop asks which noise distribution, until valid input
        noise_type = input("Noise: Type u for uniform, g for gaussian:")
        if noise_type == "u":
            noise = uniform_noise(x,offset)
        elif noise_type == "g":
            noise = gaussian_noise(x,offset)
        else:
            print("Please pick valid option")

        # then asks for optional periodic noise
        # if <n> selected, moves on
        periodic = input("Include periodic function? y/n ")
        if periodic == "y":
            p_noise = periodic_func(x)
            noise = np.add(p_noise, noise)
        elif periodic == "n":
            pass
        else:
            print("invalid response, try again")
        
        #can
        slope = input("Include drift noise? <y/n")
        if slope == "y":
            drift = drift_func(x)
            
            # adds drift to other noise
            return  np.add(drift, noise)
        elif slope == "n":
            break
        else:
            print("Invalid response, try again")
    return noise

def generate_data():
    # create the time series against which the data is plotted
    time_data = np.arange(0,50,0.2)
 
            
    # create the signal data
    pulse_data = pulse_func(time_data)
    noise_data = noise_func(time_data)
    
    
            
    
    # combine signal and noise
    data = np.add(pulse_data, noise_data)
    
    # return the time and data series
    return time_data, data
 


def plot_data(time_data, data):
    # creates a scatter plot with time as x and data as y
    plt.scatter(time_data, data, s = 0.4)
    
    # labels the axes
    plt.ylabel("Signal Strength")
    plt.xlabel("Time")
    
    # sets reasonable limits
    plt.ylim(-10,20)
    plt.xlim(0,50)
    plt.savefig('pulse_plot.png', dpi = 300)
    # displays the plot
    plt.show()

# this main function allows the import of other functions
def main():
    # gets time and signal data from the generate function
    time_data, data = generate_data()
    
    # prints the raw data
    print("Times = ",time_data)
    print("Signal = ", data)
    plot_data(time_data, data)
# save data as csv and plot as png
def save_data():
    
    # call data from function above
    time_data, data = generate_data()
    
    
    dict = {'Time': time_data, 'Signal': data}  
       
    df = pd.DataFrame(dict) 
    
    # saving the dataframe 
    df.to_csv('pulse_sim.csv')
    
    # calls plot_data to save plot
    plot_data(time_data, data)
    
# this syntax is used to allow functions to be imported
if __name__ == "__main__":
    main()

    





