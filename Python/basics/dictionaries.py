#Dictionarys are a collection of unordered key-value pairs
#They are flexible in the data types they can hold, can even hold lists and other dictionaries
test_dict = {'apple':2.99, 'oranges':1.99, 'milk':3.50, 'banana':{'yellow':0.99, 'green':0.50}}

#To access items make a key call
#To access the inner dict, make a double key call
apple_price = test_dict['apple']
green_banana_price = test_dict['banana']['green']

#Dictionaries cannot be sorted