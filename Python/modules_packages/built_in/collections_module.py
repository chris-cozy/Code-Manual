#Implements specialized container data types, aleternatives to python's internal containers (dict, tup)
#Counter object - counts the number of instances for each unique item in a list
    #A dictionary subclass. The items are stored as keys, and their counts are the values
    #Returns this dictionary, which you can perform actions on
from collections import Counter
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,4,4,4]
Counter(mylist)

sentence = "How many times does each word whow up in this sentence with a word"
test = Counter(sentence.lower().split())

#Default dictionary - Assigns a default value for if a wrong key is entered.
    #The default value is entered as the argument in lambda format
from collections import defaultdict
test = defaultdict(lambda: 0)
test['a'] = 1
test['w']

#Named tuple - A tuple with named indices
    #Creation is similar to creating a class. Enter the type name as the first parameter, then a list of field names as the second
    #You can then create instances of the type object
    #You can call the fields like attributes (sammy.age) or with indexes (sammy[0])
from collections import namedtuple
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5,breed='Husky',name='Sam')
