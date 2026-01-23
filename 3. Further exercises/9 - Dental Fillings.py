#9 - Dental Fillings

print("9 - Dental Fillings")
print()

print("""

Options for dental fillings:

    1) Temporary at £8
    2) Amalgam at £14
    3) White at £43
    4) Super white at £67
    
""")

choice = int(input("Enter either 1, 2, 3 or 4: "))
number_fillings = int(input("How many fillings do you want done? "))

if choice == 1:
    cost = number_fillings * 8

if choice == 2:
    cost = number_fillings * 14

if choice == 3:
    cost = number_fillings * 43

if choice == 4:
    cost = number_fillings * 67

print()
print("The cost for your filling(s) will be £", cost)

