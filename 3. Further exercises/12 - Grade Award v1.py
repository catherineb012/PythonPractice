#12 - Validated Grade Award
#Version 1

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

elif mark >59 and mark <70:
    grade = "B"

elif mark >49 and mark <60:
    grade = "C"

elif mark >39 and mark <50:
    grade = "D"

elif mark >=0 and mark <40:
    grade = "You got an F. You failed. :("
#end of selection

print()
print("Your name: ", name)
print("Your mark: ", mark)
print("Your grade: ", grade)
#displays results
