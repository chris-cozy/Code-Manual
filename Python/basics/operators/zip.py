#Zip - zips together lists. 
# If you just apply it (zip(list1, list2) it will return the location in memory where the zip is located. 
# If you iterate through it (for item in zip(list1, list2) it will return a tuple with the zipped lists. 
# You can cast the zip as a list to see the pairings as well.
test_list1 = [1,2,3]
test_list2 = ['a','b','c']

for item in zip(test_list1, test_list2):
    print(item)

print(list(zip(test_list1, test_list2)))