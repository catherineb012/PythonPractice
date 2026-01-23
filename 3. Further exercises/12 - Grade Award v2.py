#12 - Validated Grade Award 
#Version 2


print('12 - Validated Grade Award')
print()

name = input("Type in your name here: ")
mark = int(input("Enter your mark (1 - 100): "))

#validates input of number
while mark < 1 or mark > 100:
    print("Sorry,", mark, "is not recognised")
    mark = int(input("Type in your REAL mark here: "))

#if statements
if mark >= 70:
    grade = "A - CONGRATS!!"
    
elif mark >=60:
    grade = "B"    

elif mark >=50:
    grade = "C"

elif mark >=40:
    grade = "D"

else:
    grade = "You got an F. You failed. :("
#end of selection

print()
print(name, "with a mark of ", mark, "earns a grade", grade)
#displays results


#IMPORTNT: if the 2nd & 3rd elif were swapped and the user entered 65, 'grade C' would be printed as the program checks the elif's in order,
#so as soon as it finds one that is true it would not check the rest even if another statement is correct