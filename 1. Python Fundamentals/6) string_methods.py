#STRING METHODS

course = 'Python for Beginners'
print(len(course)) #displays how many characters are in the string i.e., the length, it is a built-in function
print(len(course[1:6]))
print(course.upper()) #turns all characters upper case
print(course.lower()) #turns all characters lower case

print(course.find('P')) #prints the index where it finds the letter 'P' (? - what if there is more than 1 instance of the same letter??)
print(course.find('o'))
print(course.find('Beginners')) #prints the index of the first letter of the string
print(course.find('xyz'))  #if not in string then it prints '-1'

print(course.title()) #returns every word with a capital letter

print(course.split())   #splits a string into a list

print(course.replace('Beginners', 'Absolute Beginners')) #replaces the first argument with the second
print(course.replace('B', 'J'))
new_course = (course.replace('Beginners', 'Absolute Beginners'))
print(new_course)

print('Python' in course) #produces a boolean value
print('python' in course)  #will get False because it is case sensitive


'''

RECAP:
len()
course.upper()
course.lower()
course.title()
course.find()
course.replace()
'...' in course

'''