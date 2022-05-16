#Basic syntax
#The else is unneccessary, but can be added
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('X is greater than 5')

#Keywords
#break - breaks out of current enclosing loop
#continue - goes to the top of the closest enclosing loop
#pass - does nothing. This can be used as a placeholder so that you can come back and fill out the loop later

#Pass example
x = [1,2,3]
for item in x:
    pass
print('End of my script')

#Continue example
mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

#Break example
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x +=1