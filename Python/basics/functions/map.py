#The map function takes a function and a list as arguments and maps the function to each entry in the list. 
# Will return a memory address, but you can iterate through the map using a for-loop or use the list function 
# on the map to get the list of values.
#With map you can pass in any function you want, 
# as long as it will successfully take in the argument or parameter passed in with the list or iterable object.
def square(num):
    return num**2

nums = [1,2,3,4,5]
for item in map(square, nums):
    print(item)

#Another example
def splicer(mystring):
    if len(mystring)%2 ==0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Chris', 'Eve', 'Andy']
list(map(splicer, names))

#Another example
#Returns first letter of all names
list(map(lambda x:x[0], names))