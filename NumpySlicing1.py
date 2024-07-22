import numpy as np

# Create arrays of 10 zeros, 10 ones, and 10 fives
zeros = np.zeros(10, dtype=int)
ones = np.ones(10, dtype=int)
fives = np.ones(10, dtype=int) * 5 

# Concatenate the arrays
result = np.concatenate((zeros, ones, fives))

# Print the resulting array
print(result)


#OUTPUT:
#   [0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5] 
