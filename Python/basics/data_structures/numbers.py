# There are different representations and built-in methods for numbers in Python
# Hexadecimal
# hex() - Coverts input number into hex format
test = 12
test_hex = hex(test)
print(test_hex)

# Binary
# bin() - Converts input number into binary format
test_bin = bin(test)
print(test_bin)

# Built-in functions
# pow(x, y) - x^y
# pow(x, y, z) - (x^y) % z
    # If you enter 3 arguments, the 3rd will be treated as a modulus
# abs(x) - Return the absolute value of x
# round(x) - Rounds x to a given precision in decimal points. Returns a float
    # You can specify the level of precision with a second argument

pow(2, 4)
abs(-15)
round(3.145962, 3)