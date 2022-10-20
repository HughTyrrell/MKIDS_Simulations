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
import scipy as sci
from pathlib import Path
import os

# Three kinds of pulse are defined below:
def gaussian_func(x):
    # loop that asks for variables for Gaussian function
    # ends after valid input
    while True:
        try:
            #a, b, c = [float(y) for y in input("Enter amplitude, mean, std. dev: ").split()]
            a = float(input("Amplitude: "))
            b = float(input("Mean: "))
            c = float(input("Std dev: "))
                    
           
        except ValueError:
            print("Three comma seperated values, please")
        else:
            break
    # expression of a gaussian
    return a*np.exp((-(x-b)**2)/(2*c**2))

def double_exp(x):
    # asks for three parameters for a Double Exponential
    exp_list = []
    
    while True:
        try:
            a = float(input("Amplitude: "))  
        except ValueError:
            print("Please enter a number")
        else: break
    
    while True:
        try:
            b = float(input("Decay parameter = "))           
        except ValueError:
            print("Please enter a number: ")
        if b< 0:
            print("Must be greater than 0")
        else:
            break  
        
    while True:  
        try:
            d = float(input("Rise parameter = "))
        except ValueError:
            print("Please enter a number: ")
        if d< 0:
            print("Must be greater than 0")
        else:
            break
    while True:
        try: 
            c = float(input("Centre = "))
        except ValueError:
            print("Please enter a number")
        else: 
            break
        
        
        
    for i in (x):
        if i < c:
            exp_list.append(a*np.exp(d*(i-c)))
        elif i >= c:
        # expression of double exponential:
            exp_list.append(a*np.exp(-b*(i-c)))
    return exp_list

def sinc(x):
    # asks for three parameters to define a sinc function
    while True:
        try :
           # A,w,b = [float(y) for y in input("Please enter Amplitude, freq, shift: ").split()]
           A = float(input("Amplitude: "))
           w = float(input("Frequency: "))
           b = float(input("Shift: "))
        except ValueError:
            print("Please enter a number: ")
        else:
            break
    # expresses sinc function using numpy.sinc
    return A*np.sinc(w*(x-b))

def pulse_func(x):
    # asks which one of the above pulses you wish to simulate
    while True:
        distrib_type = input("Pulse type: Enter g for gaussian, de for double exponential, s for sinc: ")
        if distrib_type in ["Gaussian", "gaussian", "G", "g"]:
            return gaussian_func(x)
        elif distrib_type in ["Double Exponential", "de", "DE", "De", "double exponential"]:
            #vfunc = np.vectorize(double_exp)
            #return vfunc(x)
            return double_exp(x)
        elif distrib_type in ["sinc","S", "s","Sinc"]:
            return sinc(x)
        # Must take exact spelling to exit loop
        else:
            print("Invalid input, please check spelling")
            
            
# four different kinds of noise defined below
def drift_func(x):
    # simple linear function that causes data to drift
    while True:
        try:
            slope = float(input("Slope: "))
        except ValueError:
            print("Please enter a number")
        else:
            break
    return slope*x

def uniform_noise(x, offset):
    # uniform random noise, depends on offset defined in pulse_func
    while True:
        # define bounds in relation to offset
        try:
            dev = float(input("Enter max dev from mean: "))
            
        except ValueError:
            print("Please enter a number")
        else:
            break
    offset = offset(x)
    low = offset - dev, 
    high = offset + dev
    noise = np.random.uniform(low,high,len(x))
    return noise

def gaussian_noise(x,offset):
    # normally distributed random noise
    offset = offset(x)
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
            #A, w, b = [float(y) for y in input("Please enter Amplitude, freq, shift: ")]
            A = float(input("Hamplitude: "))
            w = float(input("Frequency: "))
            b = float(input("Shift: "))
            return A*np.sin(w*x - b)
        except ValueError:
            print("Must be a number ")
        else:
            break
    
#def noise_func(x):
    
    # this function can add either gaussian noise or uniform noise
    # in addition periodic, drift and offset can all be included
    
def offset(x):
    while True: 
        # defines offset used in functions above
        try:
            offset = float(input("Please enter offset: "))
        except ValueError:
            print("Must be a number")
        else: 
            break
    return offset

def noise_distrib(x):
    while True:
        # loop asks which noise distribution, until valid input
        noise_type = input("Noise: Type u for uniform, g for gaussian: ")
        if noise_type in  ["u", "U", "uniform", "UNIFORM", "Uniform"]:
            return uniform_noise(x,offset)
        elif noise_type in ["g", "Gaussian", "G", "gaussian", "GAUSSIAN"]:
            return gaussian_noise(x,offset)
        else:
            print("Please pick valid option")


        # then asks for optional periodic noise
        # if <n> selected, moves on

def periodic_noise(x):
    func = np.zeros(len(x))
    while True:       
        periodic = input("Add (more) periodic noise? <y/n> ")
        if periodic == "y":
            func = np.add(func, periodic_func(x))           
        elif periodic == "n":
            break
        else:
            print("invalid response, try again")
    return func

def drift_noise(x):
        # adds optional drift
    while True:
        slope = input("Include drift noise? <y/n> ")
        if slope == "y":
            drift = drift_func(x)
            
            # adds drift to other noise
            return  drift
        elif slope == "n":
            return np.zeros(len(x))
        else:
            print("Invalid response, try again")

def generate_data():
    # create the time series against which the data is plotted
    while True:
        try:
            N = float(input("Number of time measurements/x-values: "))
        except ValueError:
            print("Must be number")
        if N<0:
            print("Must be greater than 0")
        else:
            break
        
    time_data = np.arange(0,N,0.2)
 
            
    # create the signal data
    pulse_data = pulse_func(time_data)
    #n1 = np.add(offset(time_data),noise_distrib(time_data))
    n2 = np.add(periodic_noise(time_data), drift_noise(time_data))
    noise_data = np.add(noise_distrib(time_data),n2)
    
    
            
    
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
    #plt.ylim(-10,20)
    plt.xlim(0,max(time_data))
    
    # displays the plot
    plt.show()
def save_data(time_data, data):
     
    
    # saving the dataframe 
    while True:
        save = input("Save plot and data? <y/n> ")
        if save == "y":
            path = input("Enter path name to folder, starting and ending with /: ") 
            dict = {'Time': time_data, 'Signal': data}       
            df = pd.DataFrame(dict)
            df.to_csv(Path(path, 'pulse_data.csv'))
            plot_data(time_data, data)
            plt.savefig(path + 'pulse_plot.png', dpi = 300)
        elif save == "n":
            break
        else:
            print("Invalid response, please try again")
    # calls plot_data to save plot
# this main function allows the import of other functions
def main():
    # gets time and signal data from the generate function
    time_data, data = generate_data()
    save_data(time_data, data)
    # prints the raw data
    print("Times = ",time_data)
    print("Signal = ", data)
    plot_data(time_data, data)
# save data as csv and plot as png

    
    
#def welch():
    
    
# this syntax is used to allow functions to be imported
if __name__ == "__main__":
    main()

    





