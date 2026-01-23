#Random Number Game

from random import * #mean I don't need prefix any pre-definied functions with 'random.' like I would need to if I did 'import random'
random_number = randint(0,100)
number_of_guesses = 0

print("You must guess the correct number between 0 - 100")
guess = int(input("Please enter your guess: "))

while guess != random_number:
    while guess > 100 or guess < 0: #input validation
        print("Your guess is invalid please enter again")
        guess = int(input())
    
    if guess > random_number:
        print("Your guess is too high. Try again")
        guess = int(input())
    elif guess < random_number:
        print("Your guess is too low")
        guess = int(input())
    number_of_guesses += 1
number_of_guesses += 1

print()
print("You guessed the correct number!")
print("The random number = ", random_number)
print("Number of guesses = ", number_of_guesses)
