#10 - Standard Scratch

print("10 - Standard Scratch")
print()


par_three_holes = int(input("Enter the number of par 3 holes: "))
par_four_holes = int(input("Enter the number of par 4 holes: "))
par_five_holes = int(input("Enter the number of par 5 holes: "))
difficulty = int(input("What is the difficulty adjustment of the course? "))

standard_scratch = par_three_holes + par_four_holes + par_five_holes + difficulty
print(standard_scratch)
