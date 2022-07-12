#Sets are an unordered collection of unique objects
#To initialize:
test_1 = set()

# Built-in functions
# add(x) - adds value x to set if valid
# clear() - remove all elements from the set
# copy() - returns a copy of the set
# discard(x) - removes element x from the set if it is present 
test_1.add(1)
test_1.add(2)
test_1.add(3)
test_1.discard(1)

test_2 = test_1.copy()
test_2.clear()

# difference(x) - returns the elements that aren't in both set
# difference_update(x) - returns the set after removing the elements that are in common with x
# interesection(x) - returns a set of all the elements in common
# intersection_update(x) - updates itself with the intersection of set x
test_1 = {1,2,3,4,5}
test_2 = {1,4,5}
test_1.difference_update(test_2)
print(test_1.intersection(test_2))
test_1.intersection_update(test_2)

# symmetric_difference(x) - returns a set of the elements that are in exactly one of the sets
# symmetric_difference_update(x) - updates the set with the symmetric differnce of x
# union(x) - returns the union of both sets (all elements in both)
# update(x) - updates the set with the union of itself and x
test_1 = {1,2,3,4,5}
test_2 = {1,4,5,6}
test_1.symmetric_difference(test_2)
test_1.symmetric_difference_update(test_2)
test_3 = test_1.union(test_2)


# isdisjoint(x) - returns true is the sets have a NULL intersection (no elements in common)
# issubset(x) - returns true if a subset of x
# issuperset(x) - returns true if a superset of x
test_1 = {1,2,3,4,5}
test_2 = {1,4,5}
test_3 = {6,3,8,2}
test_1.isdisjoint(test_2)
test_2.isdisjoint(test_3)
test_2.issubset(test_1)
test_1.issuperset(test_2)


#You can cast a list to a set to get only the unique values
test_list = [1,2,3,3,3,3,5,5,5,6,6,6,2,2,7]
test_set = set(test_list)
