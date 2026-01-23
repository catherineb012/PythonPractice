#20 - Charity Collection (part 2)

print("20 - Charity Collection (part 2)")
print()

first_amount = int(input("Please enter the first amount raised: "))
second_amount = int(input("Please enter the second amount raised: "))
third_amount = int(input("Please enter the third amount raised: "))

total_amount = first_amount + second_amount + third_amount

print("A total of £", total_amount, "was raised")

if total_amount < 1000:
    low_amount = total_amount + 100
    print("With the company bonus, this will be raised to £", low_amount)

elif total_amount >= 1000 and total_amount <= 2000:
    middle_amount = total_amount * 2
    print("With the company bonus, this will be raised to £", middle_amount)

elif total_amount > 2000:
    high_amount = 2 * 2000 + (total_amount - 2000)
    print("With the company bonus, this will be raised to £", high_amount)

#or using lists

amounts = [0,0,0]
number = ["first", "second", "third"]

for i in range(3):
    amounts[i] = int(input(f"Please enter the {number[i]} amount raised: "))

total_amount = sum(amounts)

print("A total of £", total_amount, "was raised")

if total_amount < 1000:
    low_amount = total_amount + 100
    print("With the company bonus, this will be raised to £", low_amount)

elif total_amount >= 1000 and total_amount <= 2000:
    middle_amount = total_amount * 2
    print("With the company bonus, this will be raised to £", middle_amount)

elif total_amount > 2000:
    high_amount = 2 * 2000 + (total_amount - 2000)
    print("With the company bonus, this will be raised to £", high_amount)