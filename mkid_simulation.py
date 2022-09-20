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


def pulse_func(x, a = 10, b = 32, c = 1):
    # initialise amplitude, mean, standard deviation
    
    # define mathematical gaussian function
    return a*np.exp((-(x-b)**2)/(2*c**2))
        

def noise_func(x, low = 4, high = 6):
    
    # create list of random numbers
    # for each time interval within bounds
    noise = np.random.uniform(low,high,len(x))
    return noise


def generate_data():
    # create the time series against which the data is plotted
    time_data = np.arange(0,50)
    
    # create the signal data
    pulse_data = pulse_func(time_data)
    noise_data = noise_func(time_data)
    
    # combine signal and noise
    data = np.add(pulse_data, noise_data)
    
    # return the time and data series
    return time_data, data
 


def plot_data(time_data, data):
    # creates a scatter plot with time as x and data as y
    plt.scatter(time_data, data)
    
    # labels the axes
    plt.ylabel("Signal Strength")
    plt.xlabel("Time")
    
    # sets reasonable limits
    plt.ylim(0,20)
    plt.xlim(0,50)
    
    #saves plot
    
    # displays the plot
    plt.show()

# this main function allows the import of other functions
def main():
    # gets time and signal data from the generate function
    time_data, data = generate_data()
    
    # prints the raw data
    print("Times = ",time_data)
    print("Signal = ", data)
    
    # plots the data
    plt.savefig('pulse_plot.png', dpi = 300)
    plot_data(time_data, data)
    
    #saving data to csv file
    dict = {'Time': time_data, 'Signal': data}  
       
    df = pd.DataFrame(dict) 
        
    # saving the dataframe 
    df.to_csv('pulse_sim.csv')
    
 
# this syntax is used to allow functions to be imported
if __name__ == "__main__":
    main()
    





