#Error handling can be used to attempt to plan for possible errors. 
# We can use error handling to let the script continue with other code, while also reporting the error.
#3 keywords for this:
    #try: This is the block of code to be attempted (may lead to an error)
    #except: This block of code will  execute in case there is an error in the try block
        #You can specify this to catch specify error types and handle them differently
    #else: This block will execute if there is no error
    #finally: A final block of code to be executed, regardless of an error
#The python documentation contains a list/descriptions of error types
try:
    result = 10 + '10'
except:
    print('An error happened, oh no!')

#ANOTHER EXAMPLE
try:
    result = 10 + 10
except:
    print('An error happened, oh no!')
else:
    print(result)

#ANOTHER EXAMPLE - returns an OS Error
try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print('There was a type error!')
except OSError:
    print('There was an OS Error!')
finally:
    print('This block runs eveytime')

#A FINAL EXAMPLE
def ask():
    while True:
        try:
            result = int(input('Provide a number: '))
        except:
            print("That isn't a number")
            continue
        else:
            print('Thank you')
            break
        finally:
            print("End of try/except/finally")