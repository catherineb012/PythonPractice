#14 - Net Calories Gained

print("14 - Net Calories Gained")
print()

#create empty lists
calories_consumed = [0,0,0,0,0,0,0]
calories_burned = [0,0,0,0,0,0,0]
net_gain = [0,0,0,0,0,0,0]

#create total
total = 0

#takes in results for week and store in arrays
for day in range(7):
    print("Day", day + 1)
    calories_consumed[day] = int(input("Enter calories consumed: "))
    calories_burned[day] = int(input("Enter calories burned: "))
    net_gain[day] = calories_consumed[day] - calories_burned[day]
    #end of 'for' block

#display results in a table
#first display the column headings using \t to put them in columns

print("Day \t Calories consumed \t Calories burned \t Net gain")

#now use a loop to display the table also using \t for columns
for day in range(7):
    print(day + 1, "\t\t", calories_consumed[day], "\t\t\t", calories_burned[day], "\t\t", net_gain[day])
    total = total + net_gain[day] #Keep a running total
    #end of 'for' block

#display net gain for week
    print()
    print("That comes to", total, "Calories over the week")


