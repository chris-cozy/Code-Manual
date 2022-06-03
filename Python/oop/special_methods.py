#Special methods allow you to use built-in methods with user-created objects.
#If you use built-in methods such as print() or len() without using special methods, you will not get the desired result.
    #Example - using print() on a user-created object without the special method __str__ will return the object's memory location
    #Similar to overwriting toString() in Java
# A few examples of special methods and their corresponding built-in methods below:
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #print()
    def __str__(self):
        return f"{self.title} by {self.author}"

    #len()
    def __len__(self):
        return self.pages

    #del() - deletes a var from memory. Works without a special method, but you can add more functionality with one.
    def __del__(self):
        print("A book object has been deleted")

#Corresponding commands
book = Book('Python Rocks', 'Jose', 200)
print(book)
print(len(book))
del book