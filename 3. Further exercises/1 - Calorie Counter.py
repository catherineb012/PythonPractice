#1 - Calorie Counter

print("1 - Calorie Counter Program")
print()

porridge_calories = int(input("How many caloies in porridge? "))
toast_calories = int(input("How many calories in toast? "))
marmalade_calories = int(input("How many caloies in marmalade? "))
coffee_calories = int(input("How many caloies in coffee? "))

total_calories = porridge_calories + toast_calories + marmalade_calories + coffee_calories
print()
print("At breakfast you consumed", total_calories, "calories")
