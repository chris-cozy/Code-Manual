#Basic if-statement syntax
hungry = True
if hungry:
    print('Feed Me!')
else:
    print('Im not hungry')

#elif works the same as 'else if' in C
loc = 'Bank'
if loc == 'Auto Shop':
    print('Cars are cool')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcom to the store!')
else:
    print('I do not know much.')