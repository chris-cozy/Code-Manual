# Generator functions can send back a value, then later resume where they left off.
# They allow you to generate a sequence of values over time, more memory efficient
# Instead of having to compute an entire series of values at once and holding them in memory, 
# the generator computes one value and waits until the next one is called for
# If the output of a function has the potential of taking up a large amount of memory and you only intend to iterator through it,
# use a generator
# The main syntax is the yield keyword
# The range() function utilizes a generator
def cubes(n):
    '''
    An example of generator
    '''
    for x in range(n):
        yield x**3


def fibonacci(n):
    '''
    Another generator example - fibonacci sequence
    '''
    a = 1
    b = 1
    for x in range(n):
        yield a
        a,b = b, a+b


# Generators can't be called like normal functions, but they can be iterated through
for num in fibonacci(10):
    print(num)

# The key to using generators are the 'next' and 'iter' functions
# next - access the next generator value
# iter - allows you turn an object into an interator, and be able to call 'next' on it
# for-loops internally use 'next'
test = fibonacci(10)
print(next(test))
print(next(test))
print(next(test))


s = 'hello'
new_s = iter(s)
next(new_s)