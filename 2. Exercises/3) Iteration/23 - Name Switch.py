#23 - Name Switch

print("23 - Name Switch")
print()

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

for i in range(3):
    for i in range(2):
        print(first_name, last_name, end = " ")
    print()
    for i in range(2):
        print(last_name, first_name, end = " ")
    print()
