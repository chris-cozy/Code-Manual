#Basic Syntax
mylist = [1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print('Reimuru Tempest')

#Tuples can also be unpacked with for loops
myTupList = [(1,2),(3,4),(5,6),(7,8)]
for a,b in myTupList:
    print(b)

#Dictionary
#This will print all key-value pairs
dic = {'k1':1, 'k2':2, 'k3':3}
for item in dic.items():
    print(item)

#This will print all values
for key,value in dic.items():
    print(value)

#Another way to access all values
for values in dic.values():
    print(values)


#Common syntax if you don't intend to use 
# the variable name is to replace it with an _ instead.
for _ in 'Hello World':
     print('Cool')

