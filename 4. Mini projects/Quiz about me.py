#Python Quiz - 10 questions

score = 0


#asking if they want to play + input validation
play = input("Do you want to take part in a quiz (press Y or N)? ")


while play != "Y"  and play != "N":
    play = input("Please press either Y or N: ")


if play == "Y":
    print()
    print("okay - here is the first question...")

elif play == "N":
    print("okay - this program will now end")
    exit() #stops the intepreter from running the program altogether


#asking questions
answer = input("Question 1: What is my favourite programming language? ")
if answer.lower() == "python": #so the user isn't penalised for using different cases to the code
    score += 1
    print("correct")

else:
    print("wrong answer")


answer2 = input("Question 2: What is one of my favourite colours? ")

if answer2.lower() == "blue" or answer2.lower() == "purple":
    score += 1
    print("correct")

else:
    print("wrong answer")


answer3 = input("Question 3: What is a sport that I do regularly? ")
if answer3.lower() == "tennis" or answer3.lower() == "golf" or answer3.lower() == "dance":
    score += 1
    print("correct")

else:
    print("wrong answer")


answer4 = input("Question 4: Name a musical instrument that I can play: ")
if answer4.lower() == "piano" or answer4.lower() == "keyboard" or answer4.lower() == "guitar" or answer4.lower() == "singing":
    score += 1
    print("correct")

else: print("wrong answer")

answer5 = input("Question 5: What is my favourite dessert to make? ")
if answer5.lower() == "tiramisu":
    score += 1
    print("correct")

else:
    print("wrong answer")
    
print()


#presenting the score
print("This quiz has finished and your score is... ")
print(score, "out of 5")

if score == 5:
    print("Well Done - you must know me well! ")
    
elif score == 4 or score == 3:
    print("Good job")
    
elif score == 2 or score == 1:
    print("You should get to know me more!")
    
else:
    print("Tut tut tut :( ")
    
