#5 - Average Calories 

# Version 1 - less efficient

print("5 - Average Calories")
print()

print("Please enter how many calories you ate for each day...")

day_one_kcals = int(input("Day 1: "))
day_two_kcals = int(input("Day 2: "))
day_three_kcals = int(input("Day 3: "))
day_four_kcals = int(input("Day 4: "))
day_five_kcals = int(input("Day 5: "))
day_six_kcals = int(input("Day 6: "))
day_seven_kcals = int(input("Day 7: "))

total_kcals = day_one_kcals + day_two_kcals + day_three_kcals + day_four_kcals + day_five_kcals + day_six_kcals + day_seven_kcals

average_daily_kcals = total_kcals / 7

print()
print("Average daily Calories = ", average_daily_kcals)