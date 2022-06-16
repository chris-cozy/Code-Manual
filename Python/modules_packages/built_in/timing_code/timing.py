# An easy way to do test efficiency is to time your code's performance.
# 2 ways: 
    # Track time elapsed (has limitations/imprecise if the function is very fast or small)
    # Use the timeit module (most efficient approach)

# TRACKING ELAPSED TIME
# time.time() grabs the current time
import time

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))

start_time = time.time()
result = func_one(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(f'One: {elapsed_time}')

start_time = time.time()
result = func_two(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Two: {elapsed_time}')


# TIMEIT MODULE
# To time code:
    # timeit.timeit(statement, setup, # of times to run the code)
        # statement - code to be tested, passed in as a string
        # setup - code that needs to be run before the statement. For example, a function definition
    # The result is the total running time, added from all of the calls
import timeit
statement = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
timeit.timeit(statement, setup, number = 1000000)

statement = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(map(str, range(n)))
'''
timeit.timeit(statement, setup, number = 1000000)