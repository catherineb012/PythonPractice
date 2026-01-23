#11 - Formatting an Address

print("11 - Formatting an Address")
print()

house_no = input("What is your house number? ")
street_name = input("What is the name of your street? ")
town = input("What is the name of your town? ")

print(house_no, ",", street_name, ",", town)

#or formatted string:

address =  f'{house_no}, {street_name}, {town}'
print(address)
