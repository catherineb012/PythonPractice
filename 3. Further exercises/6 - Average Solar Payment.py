#6 - Average Solar Payment

print("6 - Average Solar Payment")
print()

total = 0

for quarter in range(4):
    payment = int(input("Enter the payment for the quarter: "))
    total = total + payment

print()
print("The total for the year = ", total)

monthly_average = total / 12

print("The monthly average = ", monthly_average)
