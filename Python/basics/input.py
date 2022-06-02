#input() - Displays text then asks user for input. 
# Typically saved under a variable for later callback. 
# Anything passed into it by the user is taken as a string. 
# Have to cast as int or float if you want the return variable as one of those types.
test = input('Enter a number here: ')
float(test)

#Built in function to test if a variable can be cast to an int
#Returns true or false
test.isdigit()