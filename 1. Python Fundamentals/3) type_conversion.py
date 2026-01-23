#TYPE CONVERSION

#int() - integer
#str() - string
#float() - floating point number
#bool() - boolean value

#Method 1
birth_year = input('Which year were you born? ')   #whenever you use the input function the type will always be a string
year = 2020   #the variable 'year' is an integer
print(type(birth_year))
age = year - int(birth_year)    #to do the sum, both of the numbers HAVE to be integers, so 'age' is now an integer
print('Your are ' + str(age) + ' years old')  #if you are displaying the result as a string then you have to turn 'age' from an intger to a string to make all the expressions strings
print(type(age))   #should still be an integer

#EXERCISE
weight_pounds = input('What is your weight in pounds? ')
weight_kg = float(weight_pounds) * 0.45
print(weight_kg)