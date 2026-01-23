#5 - Average Calories 

# Version 2 - more efficient

print("5 - Average Calories")
print()

total = 0

for day in range(7):
    calories = int(input(f"Number of Calories consumed on Day {day + 1}? "))
    total = total + calories

average = total / 7
print()
print("Your average consumption was ", average, "Calories")