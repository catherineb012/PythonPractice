#FOR LOOPS

#a string is a sequence/list of characters

for item in "Python": #i is a loop variable, in each iteration it will hold one item
    print(item)


names = ["John", "Sarah", "Beth"]

for name in names:
    print(name)

for item in range(10):
    print(item) #will print 0 - 9

for i in range (5,10):
    print(i) #prints 5 - 9

for i in range(5,10,2): #2 is the step, starts at 5 then goes 2 steps forward
    print(i)


#EXERCISE

prices = [10,20,30]
total = 0

for price in prices:
    total += price

print(f"The total cost is £{total}")
