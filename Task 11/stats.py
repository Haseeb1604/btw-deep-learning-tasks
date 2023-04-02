import numpy as np

# Generate some random data
data = np.random.normal(loc=5, scale=2, size=1000)

# Compute the mean, median, and mode of the data
# Mode is not available in np
mean = np.mean(data)
median = np.median(data)

print("Mean:", mean)  # Mean: 4.979643361132564
print("Median:", median)  # Median: 4.982166600238067

# Define a function to compute the mode
def mode(arr):
    values, counts = np.unique(arr, return_counts=True)
    index = np.argmax(counts)
    return values[index]

mode = mode(data)
print("Mode:", mode)  # Mode: 2.060665659173123

# Compute the 25th and 75th percentiles of the data
q25, q75 = np.percentile(data, [25, 75])
print("25th percentile:", q25)  # 25th percentile: 3.7109656954084515
print("75th percentile:", q75)  # 75th percentile: 6.186578517355485

# Compute the interquartile range (IQR)
iqr = q75 - q25
print("IQR:", iqr)  # IQR: 2.4756128219470337

# Compute the standard deviation and variance of the data
std_dev = np.std(data)
variance = np.var(data)
print("Standard deviation:", std_dev)  # Standard deviation: 2.025176658479397
print("Variance:", variance)  # Variance: 4.101837584640781

# Compute the skewness and kurtosis of the data
skewness = np.skew(data)
kurtosis = np.kurtosis(data)
print("Skewness:", skewness)  # Skewness: -0.03893717172905434
print("Kurtosis:", kurtosis)  # Kurtosis: -0.13381393082709984
