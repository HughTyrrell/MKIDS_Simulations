#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:50:57 2022

@author: hughtyrrell
"""
import matplotlib.pyplot as plt
import numpy as np

time_data = [0,1,2,3,4,5,6,7,8,9,10]

def generate_data():
    pulse_data = [0,0,0,0,0,0,0,2,7,1,0]
    noise_data = [3,3,2,3,3,4,3,2,3,3,4]
    return np.add(pulse_data, noise_data)

#create scatter plot
plt.scatter(time_data, generate_data())
plt.ylabel("Signal Strength")
plt.xlabel("Time")
plt.ylim(0,15)
plt.xlim(0,12)
plt.show()

"""f = open("pulse_script.txt", "w")
f.write(time_data, generate_data())
f.close()"""