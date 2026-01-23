#19 - Solid, Liquid, Gas

print("19 - Solid, Liquid, Gas")
print()

temp = int(input("Enter the current temperture: "))

if temp <= 0:
    print("at", temp, "centigrade, water will be solid")

elif temp > 0 and temp < 100:
    print("at", temp, "centigrade, water will be a liquid")

elif temp >= 100:
    print("at", temp, "centigrade, water will be a gas")
