#The range function returns a number in the range specified
for num in range(0,10,2):
    print(num)


#Range is a generator, so if you want a list of the generated values you must type-cast it as a list.
list(range(0,11,2))