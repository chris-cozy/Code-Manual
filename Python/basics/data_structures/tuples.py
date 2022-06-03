#Tuples are essentially immutable lists and use parenthesis
# mainly used for passing around objects in a program with 
# confidence that the contents will not be changed, data integrity
#You can access tuple items like you would a list
test = ('a', 'b', 'c', 'd', 'a')
first_letter = test[0]

#Built-in tuple functions
#count - returns number of occurences of that element
#index - returns index of the element
test.count('a')
test.index('d')

#Example of tuple unpacking
stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
for ticker,price in stock_prices:
    print(price+(0.1*price))

#Another example of tuple unpacking
test1 = ('APPL',200)
test2 = ('GOOG',400)

comp1, price1 = test1
comp2, price2 = test2
