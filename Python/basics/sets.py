#Sets are an unordered collection of unique objects
#To initialize:
test = set()

#Built-in functions
#add - adds value to set if valid
test.add(1)
test.add(2)
test.add(3)

#You can cast a list to a set to get only the unique values
test_list = [1,2,3,3,3,3,5,5,5,6,6,6,2,2,7]
test_set = set(test_list)
