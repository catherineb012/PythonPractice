#15 - Charity Collection

print("15 - Charity Collection")
print()

first_amount = int(input("Please enter the first amount raised: "))
second_amount = int(input("Please enter the second amount raised: "))
third_amount = int(input("Please enter the third amount raised: "))

total_amount = first_amount + second_amount + third_amount

if total_amount > 1000:
    print("A total of £", total_amount, "was raised")
    total_amount = total_amount * 2
    print("This will be doubled to £", total_amount)

else:
    print("A total of £", total_amount, "was raised")
    print("This will not be doubled")
