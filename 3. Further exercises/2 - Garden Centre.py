#2 - Garden Centre

print("2 - Garden Centre")
print()

tulips_cost = int(input("How much did you spend on tuplips? £"))
crocuses_cost = int(input("How much did you spend on crocuses? £"))
snowdrops_cost = int(input("How much did you spend on snowdrops? £"))
daffodils_cost = int(input("How much did you spend on daffodils? £"))

total_cost = tulips_cost + crocuses_cost + snowdrops_cost + daffodils_cost

print()
print("Total spent on bulbs was £", total_cost)

print()
if total_cost > 30:
    print("You may also recieve a free gift on us of a hyacynth bulb. Thank you for shopping with us.")

else:
    print("Thank you for shopping with us.")
