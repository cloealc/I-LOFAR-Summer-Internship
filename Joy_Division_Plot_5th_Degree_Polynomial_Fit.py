import pandas as pd
import tkinter
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data = pd.read_csv('attempt_new.txt',sep='\s+',header=None)
data = pd.DataFrame(data)
data.columns = ['time', 'amp']

array_data = data.to_numpy()

peaks_data = pd.read_csv('attempt_new.pls',sep='\s+',header=None)
peaks_data = pd.DataFrame(peaks_data)
peaks_data.columns = ['DM', 'width', 'sample_num', 'SNR', 'pow2']

array_peaks = peaks_data.to_numpy()
peak_bins = array_peaks[:,2]
peak_bins = peak_bins.tolist()

side_width = 500

def objective(x, a, b, c, d, e, f): # define the true objective function
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

plt.figure(figsize=(5,20))
plt.rcParams['axes.facecolor'] = 'black'

for i in peak_bins:
    start = int(i) - side_width
    end = int(i) + side_width
    y = array_data[start:end,1] / 1e7
    x = np.arange(0,len(array_data[start:end,1]))
    popt, _ = curve_fit(objective, x, y) # curve fit
    a, b, c, d, e, f = popt # summarize the parameter values
    x_line = np.arange(min(x), max(x), 1) # define a sequence of inputs between the smallest and largest known inputs
    y_line = objective(x_line, a, b, c, d, e, f) # calculate the output for the range
    plt.plot(x_line, y_line - .1 * peak_bins.index(i), '-', color='w',zorder=1 + 1 * peak_bins.index(i), linewidth=3)
    plt.fill_between(x_line, y_line - .1 * peak_bins.index(i), -9.15 , color='k', zorder=2 + 1 * peak_bins.index(i))

plt.show()

