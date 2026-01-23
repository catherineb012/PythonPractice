#15 - Selective Net Calories Gained
#Catherine Bell
#6 Sep 2021

print("15 - Selective Net Calories Gained")
print()

#create arrays
calories_consumed = [0,0,0,0,0,0,0]
calories_burned = [0,0,0,0,0,0,0]
net_gain = [0,0,0,0,0,0,0]

chosen = [False, False, False, False, False, False, False]

#create running total variable
total = 0

#take in results for week and store in arrays
for day in range(7):
    print("Day", day + 1)
    calories_consumed[day] = int(input("Enter number of calories consumed: "))
    calories_burned[day] = int(input("Enter number of calories burned: "))
    net_gain[day] = calories_consumed[day] - calories_burned[day]

#find out which days are to be displayed
for day in range(7):
    answer = input(f"Enter y to display day {str(day + 1)}: ")
    if answer == "y":
        chosen[day] = True
        #end of 'if' block
    #end of 'for' block

#display results in a table

#first display the column heading using \t to put them in columns
print("Day \t Calories consumed \t Calories burned \t Net gain")

#now use a loop to display the table also using \t for columns
for day in range(7):
    if chosen[day] == True:
        print(day + 1, "\t\t", calories_consumed[day], "\t\t\t", calories_burned[day], "\t\t", net_gain[day])
        total = total + net_gain[day]
        #end of 'if' block
    #end of 'for' block

#display weekly gain for week
print()
print("That comes to", total, "Calories for those days")
