#DICTIONARIES

#Stores key-value pairs

customer = {
    "name" : "John Smith", #keys have to be unique, can only be listed once
    "age" : 30,
    "is_verified" : True
}

print(customer["name"])

#print(customer["birthdate"]) --> this will result in an error as there is no 'birthdate' key
#so instead can do this:
print(customer.get("birthdate")) #if the key doesn't exist, then prints 'None' - as it represents the absence of a value

print(customer.get("birthdate", "Jan 1 1980")) #if key doesn't exist, then can set a default value

customer["name"] = "Jack Smith"
print(customer["name"])


customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

print(customer) #prints all key-value pairs


#EXERCISE

phone_number = input("Phone: ")

numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

for digit in phone_number:
    print(numbers[digit])


#ALT SOLUTION

phone_number = input("Phone: ")

numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

output = ""

for digit in phone_number:
    output += numbers.get(digit, "!")

