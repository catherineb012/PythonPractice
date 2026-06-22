def greet_user(): #short for defining a function, : mean we are defining a block of code
    print("Hi there!")
    print("Welcome aboard")

#always add 2 line breaks after defining a function

print("Start")
greet_user() #will execute the code that is inside the function, functions have to be defined above, before calling them
print("Finish") #after executing what is inside the funciton it will continue executing the next lines

#Passing information to functions

def greet_user2(first_name, last_name):#name is a parameter (the placeholder), name is alocal variable that we define in the function
#when a function as a paramter, we are obligated to pass a value for that parameter here *
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")

#always add 2 line breaks after defining a function

print("Start")
greet_user2("John", "Smith") # * John is the argument we pass to the 'name' parameter, arg - the actual piece of information we supply to these functions
greet_user2("Mary", "Jones") #re-using function and passing different arguments (positional arguments), order of the args matters
#Anywhere there is a parameter in the function, we must pass an arg for it
print("Finish") 

greet_user2(last_name = "Smith", first_name = "John") #these are KEYWORD args, order doesn't matter - can someetimes improve readability esp for numerical args, otherwise use pos args


def calc_cost(total, extra, shipping): 
    print(total)
    print(extra)
    print(shipping)
    print(total + extra + shipping)


calc_cost(total = 50, shipping = 5, extra = 2) #order of args doesn't need to be the same as the parameters if using KEYWORD args

greet_user2("John", last_name = "Smith") #must place positional args before keyword args
#can't have --> greet_user2("Smith", first_name = "John") #will give ERROR -> TypeError: greet_user2() got multiple values for argument 'first_name'

def square(number): #number is our parameter
    return number * number

result = square(2)
print(result)

print(square(3))

print(square(int(input()))) #allows user to input a number of their choosing to square


def cube(number):
    print(number * number * number) #no return statement

print(cube(2)) #by default all functions return None if function has no return statement



#Emoji Converter (again) in a function

#A function should generally not be concerned with receiving input or printing output

def emoji_converter(message): #a function should be responsible for one task and one task only
    words = message.split(' ')

    emojis = {
        ":)" : "😊",
        ":(" : "🥺",
        ";)" : "😉"
    }

    output = ""

    for word in words:
        output += emojis.get(word, f"{word} ")
        #or output += emojis.get(word, word) + " "

    return output

message = input("> ")
print(emoji_converter(message)) #message here is the arg which is an actual string