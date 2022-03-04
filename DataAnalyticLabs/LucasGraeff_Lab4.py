import numpy as np

def calcStats(title, dataset):
    mean = np.mean(dataset)
    median = np.median(dataset)
    std = np.std(dataset)
    q75, q25 = np.percentile(dataset, [75, 25])
    iqr = q75 - q25
    print(title)
    print("Mean:", mean.round(decimals=2))
    print("Median:", median)
    print("Standard Deviation:", std.round(decimals=2))
    print("Interquartile Range:", iqr, "\n")


my_data = np.genfromtxt('myfile.csv', dtype=int, delimiter=',', skip_header=1)
stats = np.array(my_data)
print("First Five Rows of the Data:")
print(stats[:5, :])
print("Shape of the data:", stats.shape, "\n")

#Calculate weight change
weight_change = stats[:, 2] - stats[:, 3]
calcStats("Descriptive Statistics for Weight Change Data:", weight_change)

#Concatenate
stats = np.column_stack((stats, weight_change))
print("First Five Rows of the Data with Weight Changes:")
print(stats[:5, :])
print("Shape of the data:", stats.shape, "\n")

#Male data
male_stats = stats[stats[:,5] == 1]
print("First Five Rows of the Data relevant to Males:")
print(male_stats[:5, :])
print("Shape of the data:", male_stats.shape, "\n")
calcStats("Descriptive Statistics for Data relevant to Males:", male_stats)

#Female data
female_stats = stats[stats[:,5] == 2]
print("First Five Rows of the Data relevant to Females:")
print(stats[:5, :])
print("Shape of the data:", female_stats.shape, "\n")
calcStats("Descriptive Statistics for Data relevant to Females:", female_stats)
