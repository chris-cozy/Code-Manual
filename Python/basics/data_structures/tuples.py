#Tuples are essentially immutable lists and use parenthesis
# mainly used for passing around objects in a program with 
# confidence that the contents will not be changed, data integrity
test = ('a', 'b', 'c', 'd', 'a')

#Built-in tuple functions
#count - returns number of occurences of that element
#index - returns index of the element
test.count('a')
test.index('d')

#Example of tuple unpacking
stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
for ticker,price in stock_prices:
    print(price+(0.1*price))

