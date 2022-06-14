# Allows the creation of random numbers
# If going in-depth with probability in python, checkl out the NumPy library. It is designed for numerical processing
import random

# Returns a random int
random.randint(0, 100)

# Setting a seed allows you to recieve results from the same batch of random numbers
    # The same random numbers will show up in a series
    # The seed value is totally arbitrary
        # 101 is common
        # 42 is common - reference to hitchhiker's guide to the galaxy
# You will get the same numbers back now
random.seed(101)
random.randint(0, 100)


# Choice - Returns a single random item from a list
# Picking multiple items
    # Sampling with replacement - allow the same item to be picked twice
        # Choices (population = list, k = item num)
        # Returns a list of selected items
    # Sampling without replacement - do not allow the same item to be picked twice
        # Sample (population = list, k = item num)
        # Returns a list of selected items
test = list(range(0,20))
random.choice(test)
random.choices(population = test, k = 5)
random.sample(population = test, k = 5)


# Shuffling a list
    # Affects the actual list
random.shuffle(test)

# Probablilty distributions
    # Uniform - randomly picks a value between a and b. FLoating nums are allowed
    # Normal/ Gaussian - takes in a mean and standard deviation
random.uniform(a  = 0, b = 100)
random.gauss(mu = 0, sigma = 1)