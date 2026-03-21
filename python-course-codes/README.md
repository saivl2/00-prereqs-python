# Python Course Codes - Cheatsheet

A comprehensive guide covering Python fundamentals with code examples and best practices. This document is continuously updated as we progress through the course.

---

## Table of Contents
1. [Variables](#variables)
2. [Numbers](#numbers)
3. [Strings](#strings)
4. [Booleans](#booleans)
5. [Lists](#lists)
6. [Tuples](#tuples)
7. [Dictionaries](#dictionaries)
8. [Sets](#sets)
9. [Input](#input)
10. [Built-in Functions](#built-in-functions)

---

## Variables

### Definition
Variables are containers for storing data values. In Python, a variable is created the moment you assign a value to it.

### Syntax
```python
variable_name = value
```

### Examples
```python
age = 30
name = "Alice"
price = 19.99
```

### Constants
By convention, constants are written in UPPERCASE:
```python
PI = 3.14159
RADIANS_TO_DEGREES = 180 / PI
```

### Key Points
- Variable names are case-sensitive
- Must start with a letter or underscore
- Can contain alphanumeric characters and underscores
- Reassignment updates the variable's value

---

## Numbers

### Integer (int)
Whole numbers, positive or negative
```python
age = 35
count = -10
```

### Float
Decimal numbers
```python
price = 56.78
temperature = -3.14
```

### Basic Operations
```python
# Addition
result = 5 + 3  # 8

# Subtraction
result = 10 - 4  # 6

# Multiplication
result = 7 * 6  # 42

# Division (returns float)
result = 12 / 3  # 4.0

# Floor Division (removes decimal, no rounding)
result = 12 // 3  # 4

# Modulus (remainder)
result = 10 % 3  # 1

# Exponentiation
result = 2 ** 3  # 8
```

### Order of Operations (PEMDAS)
Python follows the standard mathematical order:
```python
print(1 + 3 * 4 / 8 - 4)  # Multiplication and division first, then addition and subtraction
```

---

## Strings

### Definition
A sequence of characters enclosed in quotes.

### String Types
```python
# Single quotes
single = 'Hello, World!'

# Double quotes
double = "Hello, World!"

# Multi-line strings
multi = """This is a
multi-line
string"""
```

### Escaping Characters
```python
escaped = 'It\'s me'           # Escaping single quote
escaped = "It's me"            # Using double quotes to avoid escaping
escaped = 'He said "Hi"'       # Using single quotes to include double quotes
newline = "Line 1\nLine 2"     # Newline character
```

### String Formatting
```python
name = "Alice"
age = 25

# Using f-strings (Python 3.6+, recommended)
formatted = f"Name: {name}, Age: {age}"

# Using .format()
formatted = "Name: {}, Age: {}".format(name, age)

# Using % operator (older style)
formatted = "Name: %s, Age: %d" % (name, age)
```

### String Concatenation
```python
greeting = "Hello" + " " + "World"    # "Hello World"
repeated = "Ha" * 3                   # "HaHaHa"
```

### String Methods
```python
text = "Hello World"
print(text.lower())        # "hello world"
print(text.upper())        # "HELLO WORLD"
print(text.replace("H", "J"))  # "Jello World"
print(text.split())        # ["Hello", "World"]
```

### String Indexing & Slicing
```python
text = "Python"
print(text[0])             # "P"
print(text[-1])            # "n" (last character)
print(text[0:3])           # "Pyt"
print(text[::-1])          # "nohtyP" (reversed)
```

---

## Booleans

### Definition
Boolean values represent one of two states: `True` or `False`.

### Examples
```python
is_active = True
is_deleted = False
```

### Comparison Operators
```python
5 > 3         # True
5 < 3         # False
5 == 5        # True
5 != 3        # True
5 >= 5        # True
5 <= 3        # False
```

### Logical Operators
```python
# AND: Both conditions must be True
(5 > 3) and (3 > 1)        # True
(5 > 3) and (3 > 5)        # False

# OR: At least one condition must be True
(5 > 3) or (3 > 5)         # True
(5 < 3) or (3 > 5)         # False

# NOT: Inverts the boolean value
not True                    # False
not False                   # True
```

---

## Lists

### Definition
An ordered, mutable collection of items. Lists can contain different data types.

### Creating Lists
```python
friends = ['Amy', 'Bob', 'Ron']
random_list = [True, 4.5, "Hello"]
empty_list = []
```

### Accessing Elements
```python
friends = ['Amy', 'Bob', 'Ron']
print(friends[0])           # "Amy" (first element)
print(friends[2])           # "Ron" (third element)
print(friends[-1])          # "Ron" (last element)
print(friends[-2])          # "Bob" (second-to-last)
```

### Nested Lists
```python
matrix = [['apple', 'banana', 'cherry'], 
          [22, 14, 16], 
          [True, False, True]]
print(matrix[0][1])         # "banana"
print(matrix[2][2])         # True
```

### Adding Items
```python
friends = ['Amy', 'Bob']
friends.append('Ron')           # Add single item to end
friends.extend(['Henry', 'Zoe']) # Add multiple items
friends.insert(1, 'Charlie')    # Insert at specific index
```

### Removing Items
```python
friends = ['Amy', 'Bob', 'Ron']
friends.remove('Bob')           # Remove by value
item = friends.pop()            # Remove and return last item
item = friends.pop(0)           # Remove and return first item
del friends[0]                  # Delete by index
friends.clear()                 # Remove all items
```

### Modifying Items (Lists are Mutable)
```python
friends = ['Amy', 'Bob', 'Ron']
friends[1] = 'Bobby'            # Change specific item
friends[0:2] = ['Alice', 'Robert']  # Replace multiple items
```

### List Methods
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()                  # Sort in place
numbers.reverse()               # Reverse in place
index = numbers.index(4)        # Find index of value
count = numbers.count(1)        # Count occurrences
```

### Joining Lists
```python
list1 = ['a', 'b', 'c']
joined = ' '.join(list1)        # "a b c"
joined = '-'.join(list1)        # "a-b-c"
```

### List Slicing
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])             # [1, 2, 3]
print(numbers[:3])              # [0, 1, 2]
print(numbers[3:])              # [3, 4, 5]
print(numbers[::2])             # [0, 2, 4] (every 2nd item)
```

---

## Tuples

### Definition
An ordered, immutable collection of items. Once created, tuples cannot be modified.

### Creating Tuples
```python
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
mixed = (1, 'hello', 3.14, True)
single = (42,)                  # Note the comma!
```

### Accessing Elements
```python
coordinates = (10, 20, 30)
print(coordinates[0])           # 10
print(coordinates[-1])          # 30
```

### Tuple Unpacking
```python
x, y = (10, 20)
a, b, c = (1, 2, 3)
```

### Tuple Methods
```python
colors = ('red', 'green', 'blue', 'red')
index = colors.index('green')   # 1
count = colors.count('red')     # 2
```

### Key Differences from Lists
- **Immutable**: Cannot add, remove, or change items
- **Performance**: Slightly faster than lists
- **Use Case**: When you want to ensure data won't be modified

---

## Dictionaries

### Definition
An unordered, mutable collection of key-value pairs. Each key maps to a value.

### Creating Dictionaries
```python
friend_ages = {
    'Rolf': 24,
    'Adam': 30,
    'Anne': 23
}

empty_dict = {}
```

### Accessing Values
```python
friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 23}
print(friend_ages['Adam'])              # 30
print(friend_ages.get('Ron', 0))        # 0 (default if not found)
```

### Adding and Modifying Items
```python
friend_ages = {'Rolf': 24, 'Adam': 30}
friend_ages['Anne'] = 23                # Add new key-value pair
friend_ages['Rolf'] = 25                # Update existing value
friend_ages['Rolf'] += 1                # Increment value
```

### Removing Items
```python
friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 23}
del friend_ages['Anne']                 # Delete by key
value = friend_ages.pop('Rolf')         # Remove and return value
```

### Dictionary Methods
```python
friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 23}
keys = friend_ages.keys()               # dict_keys(['Rolf', 'Adam', 'Anne'])
values = friend_ages.values()           # dict_values([24, 30, 23])
items = friend_ages.items()             # key-value pairs
```

### Iterating Through Dictionaries
```python
for name, age in friend_ages.items():
    print(f"{name} is {age}")

for name in friend_ages:
    print(name)                         # Keys only

for age in friend_ages.values():
    print(age)                          # Values only
```

### Nested Dictionaries
```python
friends = {
    'friend1': {'name': 'Adam', 'age': 34},
    'friend2': {'name': 'Ron', 'age': 45}
}
print(friends['friend1']['name'])       # "Adam"
```

---

## Sets

### Definition
An unordered collection of unique items. Duplicates are automatically removed.

### Creating Sets
```python
colors = {'red', 'green', 'blue'}
numbers = {1, 2, 3, 4, 5}
empty_set = set()                       # Note: {} creates an empty dict
```

### Adding and Removing Items
```python
colors = {'red', 'green'}
colors.add('blue')                      # Add single item
colors.update(['yellow', 'purple'])     # Add multiple items
colors.remove('green')                  # Remove (error if not found)
colors.discard('orange')                # Remove (no error if not found)
```

### Set Operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2                     # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2              # {3, 4}
difference = set1 - set2                # {1, 2}
symmetric_diff = set1 ^ set2            # {1, 2, 5, 6}
```

### Set Methods
```python
numbers = {1, 2, 3, 4}
print(3 in numbers)                     # True (membership test)
print(len(numbers))                     # 4
```

---

## Input

### Getting User Input
```python
name = input("What is your name? ")     # Returns a string
print(f"Hello, {name}!")
```

### Converting Input to Other Types
```python
age = int(input("How old are you? "))   # Convert to integer
height = float(input("Your height: "))  # Convert to float
```

### Multiple Inputs
```python
data = input("Enter name, age, city: ").split(',')
name = data[0].strip()
age = int(data[1].strip())
city = data[2].strip()
```

---

## Built-in Functions

### Type Checking and Conversion
```python
type(5)                         # <class 'int'>
type("hello")                   # <class 'str'>

int("42")                       # 42
float("3.14")                   # 3.14
str(123)                        # "123"
bool(1)                         # True
list((1, 2, 3))                 # [1, 2, 3]
```

### Length and Size
```python
len("hello")                    # 5
len([1, 2, 3, 4])               # 4
len({'a': 1, 'b': 2})           # 2
```

### Min, Max, and Sum
```python
min(5, 2, 9, 1)                 # 1
max(5, 2, 9, 1)                 # 9
sum([1, 2, 3, 4])               # 10
```

### Sorting
```python
numbers = [3, 1, 4, 1, 5]
sorted(numbers)                 # [1, 1, 3, 4, 5] (returns new list)
sorted(numbers, reverse=True)   # [5, 4, 3, 1, 1]
```

### Iteration
```python
# range() generates a sequence of numbers
for i in range(5):
    print(i)                    # 0, 1, 2, 3, 4

# enumerate() gets index and value
for index, color in enumerate(['red', 'green', 'blue']):
    print(index, color)

# zip() combines sequences
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### Other Useful Functions
```python
abs(-5)                         # 5
round(3.14159, 2)               # 3.14
pow(2, 3)                       # 8 (same as 2 ** 3)
all([True, True, True])         # True
any([False, False, True])       # True
```

---

## Quick Reference

| Type | Mutable | Ordered | Duplicates | Example |
|------|---------|---------|-----------|---------|
| List | Yes | Yes | Yes | `[1, 2, 2]` |
| Tuple | No | Yes | Yes | `(1, 2, 2)` |
| Set | Yes | No | No | `{1, 2}` |
| Dict | Yes | Yes (3.7+) | No (keys) | `{'a': 1}` |
| String | No | Yes | Yes | `"hello"` |

---

## Updates Log

- **Initial**: Variables, Numbers, Strings, Booleans, Lists, Tuples, Dictionaries, Sets, Input, Built-in Functions

---

*To be continued as we progress through the course...*
