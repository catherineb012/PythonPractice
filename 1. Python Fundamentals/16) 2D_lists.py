#2D LISTS

#2d list - where each item in a list is another list
#useful for data science and ML

matrix = [
    [1,20,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[1]) #returns the second row which is a list
print(matrix[0][1]) #returns the second value of the first row

matrix[0][1] = 2 #modified value
print(matrix[0][1])
print(matrix)

for row in matrix:
    for item in row:
        print(item)