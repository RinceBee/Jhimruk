# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 09:55:22 2023

@author: kumar
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the excel file
df = pd.read_excel('average of all year_1.xlsx')

# Select the data in the range A2:L30
data = df.iloc[0:13, 1:30]



# Concatenate all columns into a single column
data = pd.concat([data[col] for col in data.columns], axis=0)

# Reset the index
data = data.reset_index(drop=True)
# Save the data to a new Excel file
#data.to_excel('fileee111.xlsx', index=False)


# Create a simple series
#x = np.array([1, 2, 3, 4, 5])
#y = x ** 2

# Plot the series
plt.plot(data)
#print(data)

# Add labels to the axes
plt.ylabel('discharge(m3/s)')
plt.xlabel('Months from 2051 shrawan 1')
plt.savefig("Monthly_seris.png")


# Display the plot
plt.show()


