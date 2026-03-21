# Python Fundamentals Course

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive, hands-on Python programming course covering fundamental concepts from basic data types to advanced built-in functions. This repository contains code examples, exercises, and detailed explanations for each topic.

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Course Structure](#course-structure)
- [Topics Covered](#topics-covered)
  - [Variables](#variables)
  - [Numbers](#numbers)
  - [Strings](#strings)
  - [Booleans](#booleans)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Dictionaries](#dictionaries)
  - [Sets](#sets)
  - [Input/Output](#inputoutput)
  - [Built-in Functions](#built-in-functions)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This course provides a structured learning path for Python beginners, focusing on practical examples and real-world applications. Each module includes:

- **Code Examples**: Working Python scripts demonstrating concepts
- **Detailed Explanations**: In-depth coverage of syntax and usage
- **Best Practices**: Industry-standard coding conventions
- **Common Pitfalls**: Solutions to frequently encountered issues

## 📋 Prerequisites

- **Python Version**: 3.6 or higher
- **Basic Computer Skills**: File navigation, text editing
- **No Prior Programming Experience Required**

### Recommended Tools
- Python Interpreter (pre-installed on most systems)
- Text Editor or IDE (VS Code, PyCharm, etc.)
- Command Line/Terminal access

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/saivl2/00-prereqs-python.git
cd python-course-codes
```

### 2. Verify Python Installation
```bash
python --version
# or
python3 --version
```

### 3. Run Your First Program
```bash
python variables.py
```

## 📚 Course Structure

The course is organized into progressive modules, each building upon previous concepts:

```
python-course-codes/
├── variables.py           # Basic data storage
├── numbers.py             # Numeric operations
├── strings.py             # Text manipulation
├── booleans.py            # Logical operations
├── lists.py               # Ordered collections
├── tuples.py              # Immutable sequences
├── dictionaries.py        # Key-value mappings
├── sets.py                # Unique collections
├── input.py               # User interaction
├── built_in_functions.py  # Essential utilities
└── README.md             # This documentation
```

## 📖 Topics Covered

### Variables

**Overview**: Variables are named containers that store data values in memory. Python variables are dynamically typed and can be reassigned to different data types.

**Key Concepts**:
- Variable naming conventions
- Dynamic typing
- Constants (by convention)
- Variable scope

**Code Example**:
```python
# Variable assignment
age = 30
name = "Alice"
price = 19.99

# Constants (convention: uppercase)
PI = 3.14159
MAX_CONNECTIONS = 100

# Reassignment
age = 31  # Valid: same type
age = "thirty-one"  # Valid: different type (dynamic typing)
```

**Best Practices**:
- Use descriptive, lowercase names with underscores
- Avoid single-character names except for loops
- Use constants for values that shouldn't change

### Numbers

**Overview**: Python supports two main numeric types: integers (whole numbers) and floats (decimal numbers). Both support standard mathematical operations.

**Key Concepts**:
- Integer vs Float types
- Arithmetic operators
- Order of operations (PEMDAS)
- Type conversion

**Code Example**:
```python
# Integer operations
count = 35
negative = -10

# Float operations
price = 56.78
temperature = -3.14

# Arithmetic operations
result = 1 + 3 * 4 / 8 - 4  # Follows PEMDAS: 1 + 12/8 - 4 = 1 + 1.5 - 4 = -1.5

# Floor division (integer division)
whole_result = 12 // 3  # Returns 4, not 4.0

# Modulus (remainder)
remainder = 10 % 3  # Returns 1
```

**Common Operations**:
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division (float result)
- `//` Floor division
- `%` Modulus
- `**` Exponentiation

### Strings

**Overview**: Strings are sequences of characters used to represent text. Python provides extensive string manipulation capabilities.

**Key Concepts**:
- String literals (single, double, triple quotes)
- String concatenation and repetition
- String formatting methods
- String indexing and slicing
- Escape sequences

**Code Example**:
```python
# String literals
single_quotes = 'Hello, World!'
double_quotes = "Hello, World!"
multi_line = """This is a
multi-line
string"""

# Escaping characters
escaped = 'It\'s a beautiful day'
path = "C:\\Users\\Documents\\file.txt"

# String operations
greeting = "Hello" + " " + "World"  # Concatenation
repeated = "Ha" * 3                 # "HaHaHa"

# String formatting
name = "Alice"
age = 25

# f-strings (Python 3.6+, recommended)
message = f"My name is {name} and I'm {age} years old"

# .format() method
message = "My name is {} and I'm {} years old".format(name, age)

# % operator (legacy)
message = "My name is %s and I'm %d years old" % (name, age)
```

**String Methods**:
```python
text = "Hello World"

text.lower()        # "hello world"
text.upper()        # "HELLO WORLD"
text.title()        # "Hello World"
text.replace("H", "J")  # "Jello World"
text.split()        # ["Hello", "World"]
"-".join(["Hello", "World"])  # "Hello-World"
```

### Booleans

**Overview**: Boolean values represent truth states with only two possible values: `True` and `False`. Used extensively in conditional logic and comparisons.

**Key Concepts**:
- Boolean literals
- Comparison operators
- Logical operators (AND, OR, NOT)
- Truthiness of values

**Code Example**:
```python
# Boolean literals
is_active = True
is_deleted = False

# Comparison operators
print(5 > 3)         # True
print(5 < 3)         # False
print(5 == 5)        # True
print(5 != 3)        # True
print(5 >= 5)        # True
print(5 <= 3)        # False

# Logical operators
# AND: Both conditions must be True
result = (5 > 3) and (3 > 1)    # True
result = (5 > 3) and (3 > 5)    # False

# OR: At least one condition must be True
result = (5 > 3) or (3 > 5)     # True
result = (5 < 3) or (3 > 5)     # False

# NOT: Inverts the boolean value
result = not True                # False
result = not False               # True

# Complex expression
result = ('hello' == 'Hello' or 'bye' != 'Goodbye') and 4 < -1
# Evaluates as: (False or True) and False = True and False = False
```

### Lists

**Overview**: Lists are ordered, mutable collections that can store items of different types. They are one of Python's most versatile data structures.

**Key Concepts**:
- List creation and initialization
- Accessing elements (indexing)
- List modification (mutable)
- List methods and operations
- Nested lists

**Code Example**:
```python
# Creating lists
friends = ['Amy', 'Bob', 'Ron']
random_list = [True, 4.5, "Hello"]
empty_list = []

# Accessing elements
print(friends[0])      # "Amy" (first element, index 0)
print(friends[2])      # "Ron" (third element, index 2)
print(friends[-1])     # "Ron" (last element)
print(friends[-2])     # "Bob" (second-to-last)

# Nested lists (lists of lists)
matrix = [['apple', 'banana', 'cherry'],
          [22, 14, 16],
          [True, False, True]]

print(matrix[0][1])    # "banana"
print(matrix[2][2])    # True

# Adding elements
friends.append('Henry')                    # Add to end
friends.insert(1, 'Charlie')               # Insert at index
friends.extend(['Zoe', 'David'])           # Add multiple items

# Removing elements
friends.remove('Bob')                      # Remove by value
last_item = friends.pop()                  # Remove and return last
first_item = friends.pop(0)                # Remove and return first
del friends[0]                             # Delete by index

# Modifying elements (lists are mutable)
friends[1] = 'Bobby'                       # Change specific item
friends[0:2] = ['Alice', 'Robert']         # Replace multiple items

# List operations
numbers = [3, 1, 4, 1, 5]
numbers.sort()                             # Sort in place
numbers.reverse()                          # Reverse in place
index = numbers.index(4)                   # Find index of value
count = numbers.count(1)                   # Count occurrences

# Joining lists into strings
words = ['Hello', 'World']
joined = ' '.join(words)                   # "Hello World"
joined = '-'.join(words)                   # "Hello-World"
```

### Tuples

**Overview**: Tuples are ordered, immutable sequences. Once created, their contents cannot be modified. They are useful for data that should not change.

**Key Concepts**:
- Tuple creation syntax
- Immutability
- Tuple unpacking
- Use cases vs lists

**Code Example**:
```python
# Creating tuples
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
mixed = (1, 'hello', 3.14, True)
single_element = (42,)  # Note: comma required for single element

# Accessing elements (same as lists)
print(coordinates[0])     # 10
print(colors[-1])         # "blue"

# Tuple unpacking
x, y = coordinates        # x=10, y=20
a, b, c = colors          # a='red', b='green', c='blue'

# Immutability demonstration
# colors[0] = 'yellow'    # TypeError: 'tuple' object does not support item assignment

# Adding to tuples (creates new tuple)
short_tuple = ('Rolf', 'Bob')
extended_tuple = short_tuple + ('Amy',)  # ('Rolf', 'Bob', 'Amy')

# Tuple methods
colors = ('red', 'green', 'blue', 'red')
index = colors.index('green')    # 1
count = colors.count('red')      # 2
```

**When to Use Tuples vs Lists**:
- **Tuples**: For immutable data, dictionary keys, function returns
- **Lists**: For mutable collections, dynamic data

### Dictionaries

**Overview**: Dictionaries are unordered collections of key-value pairs. They provide fast lookups and are extremely versatile for structured data.

**Key Concepts**:
- Key-value pair structure
- Dictionary creation and access
- Dictionary modification
- Dictionary methods
- Nested dictionaries

**Code Example**:
```python
# Creating dictionaries
friend_ages = {
    'Rolf': 24,
    'Adam': 30,
    'Anne': 23
}

empty_dict = {}

# Accessing values
print(friend_ages['Adam'])                    # 30
print(friend_ages.get('Ron', 0))              # 0 (default if key not found)

# Adding and modifying items
friend_ages['Charlie'] = 28                   # Add new key-value pair
friend_ages['Rolf'] = 25                      # Update existing value
friend_ages['Rolf'] += 1                      # Increment value

# Removing items
del friend_ages['Anne']                       # Delete by key
age = friend_ages.pop('Rolf')                 # Remove and return value

# Dictionary methods
keys = friend_ages.keys()                     # dict_keys object
values = friend_ages.values()                 # dict_values object
items = friend_ages.items()                   # key-value pairs

# Iterating through dictionaries
for name, age in friend_ages.items():
    print(f"{name} is {age} years old")

for name in friend_ages:                      # Keys only
    print(name)

for age in friend_ages.values():              # Values only
    print(age)

# Nested dictionaries
friends = {
    'friend1': {'name': 'Adam', 'age': 34},
    'friend2': {'name': 'Ron', 'age': 45}
}

print(friends['friend1']['name'])             # "Adam"
print(friends['friend2']['age'])              # 45
```

### Sets

**Overview**: Sets are unordered collections of unique elements. They automatically remove duplicates and provide efficient membership testing.

**Key Concepts**:
- Set creation and uniqueness
- Set operations (union, intersection, difference)
- Set methods
- Use cases

**Code Example**:
```python
# Creating sets
art_friends = {'Rolf', 'Anne'}
science_friends = {'Jen', 'Charlie'}
empty_set = set()  # Note: {} creates empty dict

# Adding elements
art_friends.add('Jen')                        # Add single element
art_friends.update(['Mike', 'Sarah'])         # Add multiple elements

# Removing elements
art_friends.remove('Jen')                     # Remove (error if not found)
art_friends.discard('NonExistent')            # Remove (no error if not found)

# Set operations
print(art_friends)
print(science_friends)

# Difference: elements in first set but not second
art_only = art_friends.difference(science_friends)
print(art_only)                               # {'Rolf', 'Anne'}

# Symmetric difference: elements in either set but not both
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

# Intersection: elements in both sets
both_groups = art_friends.intersection(science_friends)
print(both_groups)

# Union: elements in either set
all_students = art_friends.union(science_friends)
print(all_students)

# Membership testing
print('Rolf' in art_friends)                  # True
print('Mike' in art_friends)                  # False

# Set comprehensions
squares = {x**2 for x in range(5)}            # {0, 1, 4, 9, 16}
```

### Input/Output

**Overview**: Input functions allow programs to receive data from users, while output functions display information to the console.

**Key Concepts**:
- Input function behavior
- Type conversion
- Error handling
- Output formatting

**Code Example**:
```python
# Basic input (always returns string)
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Type conversion
age = int(input("Enter your age: "))          # Convert to integer
height = float(input("Enter your height: "))  # Convert to float

print(f"Name: {name}, Age: {age}, Height: {height}")

# Multiple inputs on one line
data = input("Enter name, age, city: ").split(',')
name = data[0].strip()                        # Remove whitespace
age = int(data[1].strip())
city = data[2].strip()

print(f"{name} from {city} is {age} years old")

# Error handling for input
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Please enter a valid number")
```

### Built-in Functions

**Overview**: Python provides numerous built-in functions for common operations. Mastering these functions is essential for efficient programming.

**Key Concepts**:
- Type conversion functions
- Mathematical functions
- Sequence operations
- Utility functions

**Code Example**:
```python
# Type conversion
int("42")                    # 42
float("3.14")               # 3.14
str(123)                    # "123"
bool(1)                     # True
bool(0)                     # False
list((1, 2, 3))            # [1, 2, 3]
tuple([1, 2, 3])           # (1, 2, 3)
set([1, 2, 2, 3])          # {1, 2, 3}

# Length and size
len("hello")                # 5
len([1, 2, 3, 4])          # 4
len({'a': 1, 'b': 2})       # 2

# Mathematical functions
abs(-5)                     # 5
round(3.14159, 2)           # 3.14
pow(2, 3)                   # 8 (same as 2 ** 3)
min(5, 2, 9, 1)             # 1
max(5, 2, 9, 1)             # 9
sum([1, 2, 3, 4])           # 10

# Sequence operations
sorted([3, 1, 4, 1, 5])     # [1, 1, 3, 4, 5]
reversed([1, 2, 3])          # <reversed object>
list(reversed([1, 2, 3]))    # [3, 2, 1]

# Iteration helpers
# range() - generates sequences
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

# enumerate() - adds index to iteration
for index, color in enumerate(['red', 'green', 'blue']):
    print(f"{index}: {color}")

# zip() - combines sequences
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Utility functions
all([True, True, True])      # True (all elements truthy)
any([False, False, True])    # True (at least one truthy)
type(42)                     # <class 'int'>
isinstance(42, int)          # True
```

## ✅ Best Practices

### Code Style
- Follow PEP 8 style guidelines
- Use 4 spaces for indentation
- Limit lines to 79 characters
- Use descriptive variable names
- Add comments for complex logic

### Error Handling
```python
# Always handle potential errors
try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(f"Invalid input: {e}")
```

### Performance Considerations
- Use sets for membership testing
- Prefer list comprehensions over loops when appropriate
- Use built-in functions instead of custom implementations
- Consider memory usage for large data structures

### Security
- Validate user input
- Avoid using `eval()` with untrusted input
- Use appropriate data types for sensitive data

## 🤝 Contributing

We welcome contributions to improve this course! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make your changes** with clear commit messages
4. **Test your changes** thoroughly
5. **Submit a pull request** with a detailed description

### Contribution Types
- Bug fixes and corrections
- Additional examples and exercises
- Improved documentation
- New topic coverage

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📚 Additional Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [Real Python Tutorials](https://realpython.com/)

---

*Happy coding! 🚀*

**Last Updated**: March 2026
**Python Version**: 3.6+
**Course Level**: Beginner to Intermediate