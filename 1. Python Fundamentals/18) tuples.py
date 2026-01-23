#TUPLES

numbers = (1,2,3) #tuples use () instead of []

print(numbers[0])

#they cannot be changed e.g., can't do this
#numbers[0] = 10
#will get 'TypeError: 'tuple' object does not support item assignment'

#also can't append, pop, remove etc
#only 2 methods: count and index

print(numbers.count(2))
print(numbers.index(3))