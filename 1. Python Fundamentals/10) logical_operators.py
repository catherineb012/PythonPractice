#LOGICAL OPERATORS

high_income = True
good_credit = True

if high_income and good_credit: #uses logial operator 'and' to combine multiple conditions
    print("Eligible for loan.")

elif high_income:
    print("Has high income, but not good credit. Not eligible for loan.")

elif good_credit:
    print("Has good credit, but not high income. Not eligible for loan.")

else:
    print("Is not allowed to take a loan!")


print()


does_homework = False
tidys_room = True
makes_food = True

if does_homework or tidys_room and makes_food:
    print("Is allowed to go to the party.")

else:
    print("Is NOT allowed to go to the party.")


print()


has_drama_lessons = True
less_than_12 = False

if has_drama_lessons and not less_than_12: #must be older than 12
    print("Can audition for the movie.")

else:
    print("Is NOT allowed to have an audition.")

#when using the 'AND' operator, all conditions have to be true
#when using the 'OR' operator, at least ONE of the conditions need to be true
#when using the 'NOT' operator, the boolean changes to having to be FALSE, instead of having to be TRUE