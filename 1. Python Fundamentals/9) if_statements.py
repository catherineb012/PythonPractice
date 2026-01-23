#IF STATEMENTS

is_hot = False #can change these to True if want
is_cold = False

if is_hot:
    print("It's hot day")
    print("Drink plenty of water")

elif is_cold: 
    print("It's a cold day")
    print("Wear warm clothes")

else:
    print("It's a lovely day")

print("Enjoy your day")

#if you used all if statements then the program would evaluate each logical expression, using elif means that the program stops checking the statemnets when it find one that is true (more efficient)   

print("-" * 20)


#EXERCISE
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price

else:
    down_payment = 0.2 * price

print(f"Down payment: £{down_payment}")