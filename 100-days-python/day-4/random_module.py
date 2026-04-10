# Generating random integers
import random
# Importing a sample module
import my_module

n = random.randint(2, 20) # Includes both parameters
print(n)

print(my_module.my_fav_num) # fetching the data in another module to my main program

# Generating random numbers between 0 and 1
print(random.random())

print(random.uniform(1, 10)) # random float between two numbers