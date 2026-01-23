#NESTED LOOPS

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})") #will print a complete set of coordinates, x from 0-3 and y from 0-2


#CHALLENGE - print letter F

#Method 1
numbers = [5, 2, 5, 2, 2]

for number in numbers:
    print("x" * number)


#Method 2 - using nested loops
numbers = [5, 2, 5, 2, 2]

for number in numbers:
    for i in range(number):
        print("x", end = "")
    print()

#(Diff method of printing)
for no_of_x in numbers: #naming variables carefully can help solve the problem 
    output = ""
    for i in range(no_of_x):
        output += "x"
    print(output)

    
#CHALLENGE 2 - print letter L

numbers = [1, 1,1, 1, 5]

for number in numbers:
    for i in range(number):
        print("x", end = "")
    print()