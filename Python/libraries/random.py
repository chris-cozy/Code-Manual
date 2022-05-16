#Random is a library, so to import functions from that library we use:
#from (library) import (Tab)
#Random is a built in library so no downloads are needed
from random import shuffle
from random import randint


#Shuffle doesn't return anything, it shuffles the actual list
test_list = [1,2,3,4,5,6,7,8,9,10]
shuffle(test_list)

#Randint grabs a random integer from between the bounds. It returns that value
test = randint(0,100)