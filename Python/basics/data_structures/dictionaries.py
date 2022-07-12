#Dictionarys are a collection of unordered key-value pairs
#They are flexible in the data types they can hold, can even hold lists and other dictionaries
# They cannot be sorted
test = {'apple':2.99, 'oranges':1.99, 'milk':3.50, 'banana':{'yellow':0.99, 'green':0.50}}

#To access items make a key call
#To access the inner dict, make a double key call
apple_price = test['apple']
green_banana_price = test['banana']['green']

# Dictionary comprehensions
# Creating a dictionary with a comprehension
# To assign keys that are not values you can use zip
test_1 = {x:x**2 for x in range(10)}

test_2 = {k:v**2 for k,v in zip(['a','b','c'], range(3))}

# Iteration
# iteritems() - for iterating through each key:value items
# itervalues() - for iterating through the values in the dictionary
# iterkeys() - for iterating through the keys in the dictionary
for k in test.iteritems():
    print(k)

for k in test.itervalues():
    print(k)

for k in test.iterkeys():
    print(k)

# Viewing - self explanatory
# viewitems()
# viewkeys()
# viewvalues()