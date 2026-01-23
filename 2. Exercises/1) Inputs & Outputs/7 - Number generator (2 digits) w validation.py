#7 - Number generator (2 digits) w/ validation

print("7 - Number generator (2 digits)")
print()

digit_one = int(input("Enter a digit between 1-9 (inclusive): "))

#'while' will keep looping this piece of code until the number is in range
while digit_one < 1 or digit_one > 9:
    print("This number is not within range")
    digit_one = int(input("Please enter a digit between 1-9: "))

digit_two = int(input("Enter another digit between 1-9 (inclusive): "))

while digit_two < 1 or digit_two > 9:
    print("This number is not within range")
    digit_two = int(input("Please enter a digit between 1-9: "))

print(digit_one, digit_two)
