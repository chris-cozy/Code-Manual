# Contains numerous mathematical functions
# If going in-depth with math in python, checkl out the NumPy library. It is designed for numerical processing
import math
help(math)

# Rounding numbers
    # Floor - rounds down
    # Ceiling - rounds up
    # Round - true rounding (rounds to all evens)
test = 4.35
math.floor(test)
math.ceil(test)
round(test)

# Constants
    # Pi
    # E
    # infinity
    # not a number (nan)
math.pi
math.e
math.inf
math.nan

# Logarithmics
    # Params (target number, base)
    # By default the base in python is e
math.log(math.e)
math.log(100, 10)

# Trigonometrics
    # Degrees - convert a radian value to degrees
    # Radians - convert a degrees value to radians
math.sin(10)
math.cos(10)
math.tan(10)
math.degrees(math.pi/2)
math.radians(90)