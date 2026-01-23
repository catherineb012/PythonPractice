#STRINGS

#there are 2 types of quotation marks to define a string
#      ' '  single quotes
#      " "  double quotes

Python_course = "Python's Course for Beginners"
python_cousre = 'Python Couse for "Beginners" '
#if you want to add an apostrophe in the string you have to use " " double quotes otherwise it will get confused
#if you want to put words in double speech marks inside the string use ' ' single quotes

email_to_J = ''' Hi John,

This is our first email to you.

Thank you,
The support team'''

print(email_to_J)  #use triple ''' ''' single or """ """ double apostrophies to define a string that spans multiple lines

course = 'Python for Beginners'

print(course[0]) #prints the first character of the string
print(course[-1]) #print the last character of the string
print(course[0:3]) #python will print the character at the first index (e.g. 0) but not the end index (e.g. 3)
print(course[1:])  #if you don't supply an end index,then python will return all the rest of the characters
print(course[:5])  #if you don't supply a start index then python will return all of the indexes up to but not including the end index
print(course[3:-2])  #this won't include the last character but will include the first one i.e, will print the 4th character up to and incl the third last one
print(course[:])  #this prints a copy of the string
another = course[:]
print(another)  #prints a clone of the string

#EXERCISE
name = 'Jennifer'
print(name[1:-1])  #this will print 'eniffe'
print(name[1:7]) #will print same as above