#Python has a built-in library to handle JSON files
#JSON files are structred very similarly to dictionaries
import json
 

a ={"name":"John",
   "age":31,
    "Salary":25000}
 
#dumps - converts the dictionary into JSON
    #Can add another argument, a json file to dump the data to
#Converts python objects into their respective JSON objects
b = json.dumps(a)
print(b)

#JSON supports primitive types, as well as nested lists, tuples, and objects
#Here are some examples
# list conversion to Array
print(json.dumps(['Welcome', "to", "GeeksforGeeks"]))
 
# tuple conversion to Array
print(json.dumps(("Welcome", "to", "GeeksforGeeks")))
 
# string conversion to String
print(json.dumps("Hi"))
 
# int conversion to Number
print(json.dumps(123))
 
# float conversion to Number
print(json.dumps(23.572))
 
# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))
 
# None value to null
print(json.dumps(None))


#Serialization is the process of encoding JSON. 
# The transformation of data into bytes to be stored or transmitted across a network.
#To handle data flow in a file, the dump function is used to make it easy to write data to files
var = {
      "Subjects": {
                  "Maths":85,
                  "Physics":90
                   }
      }

with open("filename.json", "w") as p:
     json.dump(var, p)

#Deserialization is the opposite of serialization. 
# It is the conversion of JSON objects into their respective Python formats.
#Uses the load() method
    #Usually used to load from string, otherwise, the root object is in a list or dict. 
with open("filename.json", "r") as read_it:
     data = json.load(read_it)

#Another example
json_var ="""
{
    "Country": {
        "name": "INDIA",
        "Languages_spoken": [
            {
                "names": ["Hindi", "English", "Bengali", "Telugu"]
            }
        ]
    }
}
"""
python_var = json.loads(json_var)