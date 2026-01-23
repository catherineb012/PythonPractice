#17 - Advice Please (part 2)

print("17 - Advice Please (part 2)")
print()


advice = input("Would you like some advice (enter 'Y' or 'N')? ")

while advice != "Y" and advice != "N":
    print("Sorry, you were asked to enter Y or N. Try again.\n") #/n creates a new line
    advice = input("Would you like some advice (enter 'Y' or 'N')? ")

print()

if advice == "Y":
    print("Amazing piece of advice")

elif advice == "N":
    print("No advice for you")

