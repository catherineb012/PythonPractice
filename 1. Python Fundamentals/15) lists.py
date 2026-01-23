#LISTS

names = ["John", "Bob", "Mary", "Jane", "Peter"]
print(names)
print(names[0])
print(names[-1]) #returns last item of list
print(names[-2]) #returns second last item of list
print(names[2:]) #returns items from index 2 and the rest of the list
print(names[2:4]) #doesn't include item at index 4 i.e., 5th item
print(names[:]) #assumes 0 as the default index, returns the same list unmodified


names[0] = "Jon" #modified list
print(names)


#EXERCISE - find largest number in a list

list = [2,6,7,3,6,4]

largest_num = list[0]

for i in range(1,len(list)):
    if list[i] > largest_num:
        largest_num = list[i]
    else: #don't actually need this
        continue
print(largest_num)

# Method 2

numbers = [2,6,7,3,6,4]
max = numbers[0]
for number in numbers: #compares the first num with the first num but that is not a problem
    if number > max:
        max = number
print(max)

#? - different quicker methods, i.e., split in half??