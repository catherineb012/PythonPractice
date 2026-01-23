#14 - Darts

print("14 - Darts")
print()

score = int(input("Please enter your score for darts: "))

#input validation
while score > 180 or score < 0:
    print("The score you have entered is invalid. Please enter it again: ")
    score = int(input())

if score > 100:
    print("What a great score! Well Done :)")

elif score < 10:
    print("That was rubbish. Get practising!")

else:
    print("Good job")