
#INPUT:

import numpy as np
arr = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])
# Reshape the array to a 2x3 matrix
reshaped_array = arr.reshape(3, 3)
print("Original array:")
print(arr)
print("\nReshaped array:")
print(reshaped_array)


#OUTPUT:
"""Original array:
   [ 2  3  4  5  6  7  8  9 10]

   Reshaped array:
   [[ 2  3  4]
   [ 5  6  7]
   [ 8  9 10]] """ 
