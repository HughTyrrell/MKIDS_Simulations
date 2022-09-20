#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:50:57 2022

@author: hughtyrrell
"""
import matplotlib.pyplot as plt
import numpy as np



def generate_data():
    # create the time series against which the data is plotted
    time_data = [0,1,2,3,4,5,6,7,8,9,10]
    
    # create the signal data
    pulse_data = [0,0,0,0,0,0,0,2,7,1,0]
    noise_data = [3,3,2,3,3,4,3,2,3,3,4]
    
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
    plt.ylim(0,15)
    plt.xlim(0,12)
    
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
    plot_data(time_data, data)

# this syntax is used to allow functions to be imported
if __name__ == "__main__":
    main()
