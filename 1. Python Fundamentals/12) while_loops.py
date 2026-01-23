#WHILE LOOPS

i = 1

while i<= 5:
    print(i)
    i += 1
print("Done")
print()

i = 1

while i<= 5:
    print("*" * i)
    i += 1
print("Done")


#EXERCISE - number guesser

secret_num = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_num:
        print("You won!")
        break #terminates the loop and carries on with the program
else:
    print("Sorry, you failed :(")


#EXERCISE 2 - car game

# Method 1
user_input = input()

while user_input != "quit":
    if user_input == "help":
        print(""" 
          start - to start the car
          stop - to stop the car
          quit - to exit
          """)
        user_input = input()
    elif user_input == "start":
        print("Car started... Ready to go!")
        user_input = input()
    elif user_input == "stop":
        print("Car stopped.")
        user_input= input()
    elif user_input != "start" and user_input != "stop" and user_input != "quit":
        print("I don't understand that...")
        user_input = input()
    elif user_input == "quit":
        break

# Method 2:
user_input = ""

while True: #block of code will run repeatedly  until you explicitly  break out of it
    user_input = input("> ").lower() #so don't need to write .lower for all instances of user_input
    if user_input == "help":
        print(""" 
start - to start the car
stop - to stop the car
quit - to exit
          """)
    elif user_input == "start":
        print("Car started... Ready to go!")
    elif user_input == "stop":
        print("Car stopped.")
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...")


#Improved (check if started or stopped) - Method 1

user_input = ""
prev = ""

while True: #block of code will run repeatedly  until you explicitly  break out of it
    user_input = input("> ").lower() #so don't need to write .lower for all instances of user_input
    if user_input == "help":
        print(""" 
start - to start the car
stop - to stop the car
quit - to exit
          """)
    elif user_input == "start":
        if user_input == prev:
            print("Error: Car is already started!")
        else:
            print("Car started... Ready to go!")
        prev = user_input
    elif user_input == "stop":
        if user_input == prev:
            print("Error: Car is already stopped!")
        else:
            print("Car stopped.")
        prev = user_input
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...")


#Improved - Method 2

user_input = ""
started = False

while True: #block of code will run repeatedly  until you explicitly  break out of it
    user_input = input("> ").lower() #so don't need to write .lower for all instances of user_input
    if user_input == "help":
        print(""" 
start - to start the car
stop - to stop the car
quit - to exit
          """)
    elif user_input == "start":
        if started:
            print("Error: Car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")
    elif user_input == "stop":
        if not started:
            print("Error: Car is already stopped!")
        else:
            stared = False
            print("Car stopped.")
        prev = user_input
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...")