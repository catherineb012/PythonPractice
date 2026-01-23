import numpy as np

#Slicing 1d arrays

array1 = np.array([0,1,2,3,4,5,6,7])
print(array1[1:5]) #prints from the 2nd element (at index 1) to the 5th element (at index 4)
print(array1[4:]) #if nothing at end point, prints everything that follows
print(array1[:4]) #if nothing at start point, prints everything up to (not incl) element at index 4 
print(array1[-3:-1]) #prints from the 3rd element from the end to last (not incl last)

print(array1[1:5:2]) #2 is the step, so it skips every 2nd element
print(array1[::2]) #prints every other number from the entire array

#Slicing 2d arrays

array2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(array2[1, 1:4]) #means from the 2nd element of the 2d array, slice the elements of that array from index 1 to 4 
print(array2[0:2, 2]) #means from both elements in the 2d array, return element at index 2
print(array2[0:2, 1:4]) #means from both arrays, slice them from index 1 to 4 (returns a 2d array!)


#DATA TYPES in NumPy
"""
i - integer 
b - boolean
f - float
"""

array_nums = np.array([1,2,3,4])
print(array_nums.dtype) #prints the data type of the array


array_fruit = np.array(['apple', 'banana', 'cherry'])
print(array_fruit.dtype)

#Casting

array_mixed = np.array(['1', '2', '3'], dtype = 'i') #converts element in an array to data type specified e..g, i (integer)
#if the array was ['a', '2', '3'], then wouldn't work as 'a' is not an integer 
print(array_mixed)

#astype() function allows you to make a copy of an array and specify a data type as a paramenter

array3 = np.array([1.1, 2.1, 3.1])
array3_new = array3.astype('i') #or could do astype(int)
print(array3_new)
print(array3_new.dtype)


array4 = np.array([1, 0, 3])
array4_new = array4.astype(bool) #turns 0 into False and any other integer into True
print(array4_new)
print(array4_new.dtype)


#Copy VS View

