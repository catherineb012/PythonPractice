#24 - Cricket Over

print("24 - Cricket Over")
print()

score_list = [0,0,0,0,0,0]
total_score = 0

for score in range(6):
    print("Score", score + 1)
    score_list[score] = int(input("Please enter the score for the ball: "))

total_score = sum(score_list)

print(total_score)

#Method 2 - better

total = 0
for i in range(6):
    over = int(input(f"Enter the score for ball {i+1}: "))
    total += over

print("The over's score was: " + str(total))