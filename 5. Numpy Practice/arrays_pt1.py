import numpy as np

print(np.__version__)

#Arrays

arr = np.array([1, 2, 3, 4, 5]) #list
print(arr)
print(type(arr))

arr = np.array((1, 2, 3, 4, 5)) #converts tuple into an array


#0-D array
arr_0d = np.array(42) 
print(arr)

#a 1-D array is an array that has 0-D arrays as its elements
arr_1d = np.array([1, 2, 3, 4, 5]) #1-D array
print(arr_1d)

#a 2-D array is an array that has 1-D arrays as its elements
#often used to represent a matrix

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)

#a 3-D array is an array that has 2-D arrays as its elements

arr_3d = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]) #2 2d arrays


print(arr_0d.ndim) #prints number of dimensions of the array
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

arr_5d = np.array([1,2,3,4], ndmin = 5) #creates a 5d array, ndmin stands for min. dimen.
print(arr_5d)
print("Number of dimensions: ", arr_5d.ndim)


array1 = np.array([1, 2, 3, 4, 5])
print(array1[0]) #prints the element of the array at index 1
print(array1[0] + array1[2]) #can do arithmetic operations

array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("the 2nd element on the 1st row is: ", array2[0, 1])
print("the last element of the array: ", array2[1, -1])

array3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(array3[0, 1, 2]) #prints the 3rd element of 2nd array of the 1st array