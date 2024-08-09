#1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 


import numpy as np

# Input temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify hot days (temperature > 35 degrees)
hot_days = temperatures > 35

# Identify cold days (temperature < 5 degrees)
cold_days = temperatures < 5

# Combine the conditions
extreme_days = hot_days | cold_days

# Print the results
print("Temperature readings:", temperatures)
print("Days with extreme temperatures:", temperatures[extreme_days])


"""
OUTPUT:
Temperature readings: [32.5 34.2 36.8 29.3 31.  38.7 23.1 18.5 22.8 37.2]
Days with extreme temperatures: [36.8 38.7 37.2]
"""
