#18 - Tyre & Brake War

print("18 - Tyre & Brake War")
print()


speed = int(input("Please enter the test speed (mph): "))
distance = int(input("Please enter the test topping distance (m): "))

if speed == 20 and distance >6 or speed == 30 and distance > 14 or speed == 40 and distance > 24 or speed == 50 and distance > 38 or speed == 60 and distance > 55 or speed == 70 and distance > 75:
    print("Your car failed the braking distance test.")
    print("Submit yout car for a tyre & brake test soon.")
else:
    print("You passed the requirements")
print()


#or Method 2

if speed == 20 and distance > 6:
    print("Your car failed the braking distance test.")
    print("Submit yout car for a tyre & brake test soon.")
elif speed == 30 and distance > 14:
    print("Your car failed the braking distance test.")
    print("Submit yout car for a tyre & brake test soon.")
elif speed == 40 and distance > 24:
    print("Your car failed the braking distance test.")
    print("Submit yout car for a tyre & brake test soon.")
elif speed == 50 and distance > 38:
    print("Your car failed the braking distance test.")
    print("Submit yout car for a tyre & brake test soon.")
elif speed == 60 and distance > 55:
    print("Your car failed the braking distance test.")
    print("Submit yout car for a tyre & brake test soon.")
elif speed == 70 and distance > 75:
    print("Your car failed the braking distance test.")
    print("Submit yout car for a tyre & brake test soon.")