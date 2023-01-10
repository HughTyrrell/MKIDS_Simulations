3#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:16:27 2022

@author: hughtyrrell
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import pandas as pd
import scipy as sci
from scipy import signal
from pathlib import Path
from mkid_simulation import generate_data

def import_data():
    colnames = ['phase']
    filename = input("Enter filename: ")
    df = pd.read_csv(r'/Users/hughtyrrell/Downloads/'+str(filename), names = colnames, header=None)
    arr = [i for k in df.values.tolist() for i in k]
    return arr

def combine_data():
    
    
    while True: 
        real = input("Use imported data? <y/n> ")
        sim = input("Use simulated data? <y/n> ")
        if sim == "y" and real == "y":
            real_sig = import_data()
            print("When prompted for number of x-values, enter "+str(len(real_sig)))
            time, my_sig = generate_data()   
            combined = np.add(my_sig, real_sig)
            return time, combined
        
        elif sim == "n" and real == "y":
            real_sig = import_data()
            time = np.linspace(0, len(real_sig)/1000000, len(real_sig))
            
            return time, real_sig
        elif sim == "y" and real == "n":
            return generate_data()
        else: 
            print("Invalid entry, must choose signal source")

def plot(x,y,xlab,ylab):
    plt.plot(x,y)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.show()



def Welch(data):
    while True:
        try:
            fs = float(input("Sampling frequency (Welch): "))
            if fs<0:
                print("Must be greater than 0")
        except ValueError:
            print("Must be a number")
        
        else:
            break
        
    while True:
        try:
            nperseg = float(input("Points per segment: "))
        
            if nperseg<0:
                print("Must be greater than 0")
        except ValueError:   
            print("Must be number")
        else: break
    while True:
        try:
            noverlap = float(input("No. overlapping points: "))
        
            if noverlap<0:
                print("Must be greater than 0")
        except ValueError:   
            print("Must be number")
        else:
            break
    return sci.signal.welch(x=data, fs=fs, nperseg=nperseg, noverlap=noverlap)

def main():
    time, data = combine_data()
    plot(time, data,'Time','Phase')
    f, Pxx = Welch(data)
    plot(f, Pxx,'Frequency', 'Power')

if __name__ == "__main__":
    
    main()
        
    





