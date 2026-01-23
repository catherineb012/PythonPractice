#LIST METHODS

numbers = [5,2,1,7,4]
numbers.append(10) #adds 10 to the end of the list
print(numbers)

numbers.insert(0,5) #adds number (2nd arg) to position index 0 and "pushes" all the rest of the numbers to the right
print(numbers)

numbers.remove(2)
print(numbers)

numbers.pop() #removes last item in a list
print(numbers)

print(numbers.index(5)) #prints the index at which the number first occurs (even if it occurs more than once)

#print(numbers.index(100)) #if number doesn't appear in the list then returns an error
print(50 in numbers) #checks existence of a number in a list and returns a boolean value

print(numbers.count(5)) #counts the number of times the same number occurs in a list

numbers.sort() #sorts items in ascending order, the return value is None, so don't print it
print(numbers)
numbers.reverse() #reverses order of numbers in a list
print(numbers)

names = ["Alice", "Chris", "Ben"]
names.sort() #sorts list in alphabetical order
print(names)
names.reverse()
print(names)

numbers2 = numbers.copy() #makes copy of 'numbers' list
numbers.append(10) #any changes you make to the 'numbers' list after making a copy, won't affect the second list (numbers2)
print(numbers2)

numbers.clear() #removes all items in a list i.e., clears/empties list
print(numbers)


#EXERCISE - remove duplicates from a list

# Attempt 1

numbers = [2, 3, 2, 4, 5]
numbers2 = []
n = 0

numbers.sort()

for i in range(len(numbers)):
#    print(numbers2)
    if i+n > len(numbers)-1:
        break
    count = numbers.count(numbers[i+n])
    if count > 1:
        numbers2.append(numbers[i])
        n = count - 1
    else:
        numbers2.append(numbers[i+n])
        
print(numbers2)

#doesn't work for if there are three of the same numbers or 2 duplicates... therefore not robust


# Attempt 2

numbers = [2, 3, 2, 4, 4, 5, 4, 7]
numbers2 = []

numbers.sort()

#want to add a number only if it is different from the prev one

print(numbers2)
for i in range(1, len(numbers)):
    if numbers[i-1] != numbers[i]:
        numbers2.append(numbers[i-1])
#    print(numbers2) --- shows how the list is built
numbers2.append(numbers[i])
print(numbers2)


# Alt Method - without sorting first, keeping order same (and more simple)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques: #if the number does not appear in the new list, then add it
        uniques.append(number)
print(uniques)

#if not then don't add and check the next number



#? - can you stack 2+ methods on top and execute at same time e.g., append, remove and pop??
