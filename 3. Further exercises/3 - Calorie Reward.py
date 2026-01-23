#3 - Calorie Reward

breakfast_kcals = int(input("How many calories did you eat for breakfast today? "))
lunch_kcals = int(input("How many calories did you eat for lunch today? "))
dinner_kcals = int(input("How many calories did you eat for dinner today? "))

total_kcals = breakfast_kcals + lunch_kcals + dinner_kcals

print()
print("Today you ate", total_kcals, "Calories")

print()
kcals_burnt = int(input("And how many calories did you burn today? "))

net_loss = kcals_burnt - total_kcals

print()
print("Your net loss is", net_loss, "calories")

if net_loss > 100:
    print("Well done! You deserve to treat yourself to some goodies!")
