#COMPARISON OPERATORS

temperature = 35

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's a lovely day")

# == equality operator
# != not equal to
# >= more than or equal to


#EXERCISE 1

name = input("Enter your name: ")

if len(name) < 3:
    print("Your name must be at least 3 characters")
elif len(name) > 50:
    print("Your name can only be a maximum of 50 characters")
else:
    print("Name looks good!")


#EXERCISE 2 - weight converter

weight = input("Enter your weight: ")
unit = input("(L)bs or (K)g: ")

while unit.lower() != "l" and unit.lower() != "k":
    print("You did not enter L or K. Please try again: ")
    unit = input()

if unit.lower() == "l":
    weight_kg = float(weight) * 0.45
    print(f"You are {weight_kg} kilograms")
elif unit.lower() == "k":
    weight_pounds = float(weight) / 0.45
    print(f"You are approximately {round(weight_pounds)} pounds")