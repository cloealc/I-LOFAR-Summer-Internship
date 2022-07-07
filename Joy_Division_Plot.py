#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7  2022

@author: cloealcaria
"""

import pandas as pd
import tkinter
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('attempt_new.txt',sep='\s+',header=None) # this is the data corresponding to the .tim timeseries file, converted to txtto be able to use it here
data = pd.DataFrame(data)
data.columns = ['time', 'amp']

array_data = data.to_numpy()

peaks_data = pd.read_csv('attempt_new.pls',sep='\s+',header=None) # this is the data corresponding to the single pulse search
peaks_data = pd.DataFrame(peaks_data)
peaks_data.columns = ['DM', 'width', 'sample_num', 'SNR', 'pow2']

array_peaks = peaks_data.to_numpy()
peak_bins = array_peaks[:,2]
peak_bins = peak_bins.tolist()

side_width = 500

plt.figure(figsize=(5,15))
plt.rcParams['axes.facecolor'] = 'black'

for i in peak_bins:
    start = int(i) - side_width
    end = int(i) + side_width
    y = array_data[start:end,1] / 1e7
    x = np.arange(0,len(array_data[start:end,1]))
    plt.plot(x,y - .5 * peak_bins.index(i), lw = 0.5, color = 'w') # y - .5 * peak_bins.index(i) lowers the position of the pulse at each iteration

plt.show()

