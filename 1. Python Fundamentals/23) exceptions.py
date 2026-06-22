try: #try running 
    age = int(input("Age: " ))
    income = 2000
    risk = income / age
    print(age)

except ValueError: #if program encounter this type of error then print this message, when trying to convert non-numerical value to an interger
    print("Invalid value")

except ZeroDivisionError:
    print("Age cannot be 0")




#exit code 0 - means 
#exist code [anything but 0] - means program crashed