""" 
Problem Set 20: NumPy and Matplotlib
"""

import numpy as np
import matplotlib as plt
import pandas as pd

data_set= pd.read_csv("gtbc-1.csv")

mean=np.mean(data_set)
median=np.median(data_set)
st_dev=np.std(data_set)
min_value=np.min(data_set)
max_value=np.max(data_set)
lower_percentile=np.percentile(data_set,25)
upper_percentile=np.percentile(data_set,75)

print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", st_dev)
print("Minimum Value: ", min_value)
print("Maxinum Value: ", max_value)
print("25th Percentile: ", lower_percentile)
print("75th Percentile: ", upper_percentile)

plt.plot(data_set)
plt.title("Closing Prices From 2017 & Beyond ")
plt.xlabel("Time")
plt.ylabel ("Closing Price")
plt.show()

close_to_close = np.diff(data_set) / data_set[:-1] * 100

mean_change = np.mean(close_to_close)
median_change = np.median(close_to_close)
std_dev_change = np.std(close_to_close)
min_change = np.min(close_to_close)
max_change = np.max(close_to_close)
percentile_25_change = np.percentile(close_to_close, 25)
percentile_75_change = np.percentile(close_to_close, 75)

print("Mean Change: ", mean_change)
print("Median Change: ", median_change)
print("Standard Deviation Change: ", std_dev_change)
print("Minimum Change: ", min_change)
print("Maximum Change: ", max_change)
print("25th Percentile Change: ", percentile_25_change)
print("75th Percentile Change: ", percentile_75_change)


plt.hist(close_to_close, bins=50)
plt.title("Close-to-Close Percent Change")
plt.xlabel("Percent Change")
plt.ylabel("Frequency")
plt.show()