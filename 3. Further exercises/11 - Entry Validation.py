#11 - Entry Validation


print("11 - Entry Validation for Tuck Shop program")
print()

#these two lines are needed to import and set the local currency
import locale
locale.setlocale(locale.LC_ALL,'')


print("""

Menu:
    1) Crisps at 50p
    2) Cans at 80p
    3) Chocolate at 70p
    4) Water at 40p

""")    #displays menu


choice = int(input("Enter either 1, 2, 3 or 4 to choose: "))

#these three lines are the lines that make up the validation code to reject any choice that
#is not 1, 2, 3 or 4
while choice < 1 or choice > 4:
    print("Sorry,", choice, "is not recognised")
    choice = int(input("Enter either 1, 2, 3 or 4 to choose: "))
    #end of the 'while' block
    
#use 'while' as it will keep looping the code until the user inputs a valid response i.e. a number
#between 1 - 4. Using an 'if' statement will instruct the computer to only check the user's
#response once and will then continue with the code even if the user's second response is also invalid

number = int(input("How many do you want to buy? "))

#use 'elif' instead of 'if' as it is more efficient. Using 'if' means the computer will check
#each 'if' statement, but using 'elif' means that as the computer checks each 'elif' statement,
#when it finds the right one, it doesn't check the others and moves on with the rest of the code

if choice == 1:    #use double equal sign (==) because we are checking if a number is true(boolean value??)
    cost = number * 0.50

elif choice == 2:
    cost = number * 0.80

elif choice == 3:
    cost = number * 0.70

elif choice == 4:
    cost = number * 0.40
#end of selection

print()
print("The total cost = ", locale.currency(cost)) #displays the cost with correct currency
