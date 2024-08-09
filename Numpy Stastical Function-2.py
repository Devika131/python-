#2.Compute the standard deviation of the NumPy array


# Python Program illustrating
# numpy .std( method
import numpy as np
# 1D array
arr = [20, 2, 7, 1, 34]
print("arr : ", arr)
print("std of arr : ", np.std(arr))
print ("InMore precision with float32")
print("std of arr : ", np.std(arr, dtype = np.float32))
print ("InMore acciracy with float64")
print("std of arr : ", np.std(arr, dtype = np. float64))


"""
OUTPUT:-
 arr :  [20, 2, 7, 1, 34]
std of arr :  12.576167937809991
InMore precision with float32
std of arr :  12.576168
InMore acciracy with float64
std of arr :  12.576167937809991

"""
