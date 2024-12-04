# Python Beginner Guide by Kerwin & Arnav
Welcome to the **Beginner Python Master Document**! This is a simple introduction to Python, a perfect tool for beginners who want to learn the basics of Python coding. This guide covers comments, variables, data types, printing, and more.

## Requirements
To follow this guide, you need:
- Access to [GitHub Codespaces](https://github.com/features/codespaces) (where you can write and run Python code online!)

## Vocabulary
- Input: Input is the code you type into your computer after you hit the "play" button. You will see these later in the document as **Code Blocks**.
- Output: Output is what comes out after your input. You will see this later in the document as a dropdown that says **Output**

## Topics Covered
1. **Comments**
2. **Variables**
3. **Data Types**
4. **Printing**
5. **Input**
6. **Changing Data Types**
7. **Strings**
8. **Operators and Basic Math**
9. **Return Statment**
10. **Functions**
11. **If Statments**
12. **Loops**

## Usage
You can use this guide as a reference for Python basics. Each section has examples to help you understand.

### <a name="comments"></a>1. Comments
**Comments** are notes in your code that Python ignores. They help explain what your code does. Use a hashtag (#) before your explanation so Python will just ignore the line. Like below, the one with the hashtag will just be ignored by the system; only the line without a hashtag can be received by Python.
```python
# Remember to print "Hello World"
print("Hello, World!")
```

<details>
<summary>Output</summary>

Hello, World!
</details>


### <a name="var"></a>2. Variables

**Variables** are like containers that hold values. You can use variables to store things like numbers, words, or other types of data, and you can change these values later in your code.

```python
name = "Alice"    # "name" is the variable that stores "Alice"
age = 12          # "age" is the variable that stores the number "12"
is_student = True # This variable stores the value "True"

# Printing the values of the variables
print(name, age, is_student)  # This will print: Alice 12 True
```

<details>
<summary>Output</summary>

```
Alice 12 True
```
</details>


### <a name="datatype"></a> 3. Data Types

#### Basic Types
- **String (str):** Text data, like `"hello"` or `'world'`
- **Integer (int):** Whole numbers, like `42` or `-17`
- **Float:** Decimal numbers, like `3.14` or `-0.001`
- **Complex:** Complex numbers, like `3+4j`
- **Boolean (bool):** True or False values

#### Collection Types
- **List:** Ordered, changeable sequences `[1, 2, 3]`
- **Tuple:** Ordered, unchangeable sequences `(1, 2, 3)`
- **Set:** Unordered collection of unique items `{1, 2, 3}`
- **Dictionary (dict):** Key-value pairs `{"name": "Alice", "age": 12}`

```python
# Basic Types
text = "Hello"           # String
number = 42              # Integer
decimal = 3.14           # Float
complex_num = 3 + 4j     # Complex
is_active = True         # Boolean

# Collection Types
my_list = [1, 2, 3]                    # List
my_tuple = (1, 2, 3)                   # Tuple
my_set = {1, 2, 3}                     # Set
my_dict = {"name": "Alice", "age": 12} # Dictionary

# Print types of all variables
print("Basic Types:")
print(f"String: {type(text)}")
print(f"Integer: {type(number)}")
print(f"Float: {type(decimal)}")
print(f"Complex: {type(complex_num)}")
print(f"Boolean: {type(is_active)}")
# We will be explaining the f after the print soon
print("\nCollection Types:")
print(f"List: {type(my_list)}")
print(f"Tuple: {type(my_tuple)}")
print(f"Set: {type(my_set)}")
print(f"Dictionary: {type(my_dict)}")
```

<details>
<summary>Output</summary>
  
```
Basic Types:
String: <class 'str'>
Integer: <class 'int'>
Float: <class 'float'>
Complex: <class 'complex'>
Boolean: <class 'bool'>

Collection Types:
List: <class 'list'>
Tuple: <class 'tuple'>
Set: <class 'set'>
Dictionary: <class 'dict'>
```
</details>
</details>


### <a name="printing"></a> 4. Printing

#### Basic Print
The `print()` function is used to output text to the console:
```python
# Simple print statement
print("Hello, World!")

# Print multiple items
print("Hello", "World", "!")

# Print with numbers
print("I am", 25, "years old")
```

<details>
<summary>Output</summary>
  
```
Hello, World!
Hello World !
I am 25 years old
```
</details>

#### Print Formatting
Different ways to format your print statements:

##### Using F-strings (Recommended)
```python
name = "Alice"
age = 12
print(f"My name is {name} and I am {age} years old")

# F-strings with expressions
price = 10
quantity = 3
print(f"Total cost: ${price * quantity}")
```

<details>
<summary>Output</summary>
  
```
My name is Alice and I am 12 years old
Total cost: $30
```
</details>

#### Special Characters
Print statements can include special characters:
```python
# New line
print("Line 1\nLine 2")

# Tab
print("Name:\tAlice")

# Print without newline
print("I", end=" am ") # You can change this " am " to anything you want the string to end with.
print("Amazing!")
```

<details>
<summary>Output</summary>
  
```
Line 1
Line 2
Name:	Alice
I am Amazing!
```
</details>


### <a name="input"></a> 5. Input

**Input** allows your program to receive data from the user. The `input()` function waits for the user to type something and press Enter.

#### Basic Input
```python
# Simple input
name = input("What is your name? ") # "name" is equal to what you enter into the computer for "what is your name?"
print(f"Hello, {name}!") # print "Hello" and the variable "name," which is what you enter.

# Input with numbers
age = input("How old are you? ")
print(f"You are {age} years old")
```

<details>
<summary>Output</summary>
  
```
What is your name? Alice
Hello, Alice!
How old are you? 12
You are 12 years old
```
</details>

#### Converting Input Types
Remember: `input()` always returns a string! To work with numbers, you need to convert the input:
```python
# Converting to integer
age = int(input("Enter your age: "))
next_year = age + 1
print(f"Next year you'll be {next_year}")

# Converting to float
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters")
```

<details>
<summary>Output</summary>
  
```
Enter your age: 12
Next year you'll be 13
Enter your height in meters: 1.5
Your height is 1.5 meters
```
</details>

#### Input Validation Example
```python
# Simple check if input is a number
number = input("Enter a number: ")
if number.isdigit():
    print(f"{number} is a valid number!")
else:
    print("That's not a number!")
```

<details>
<summary>Output</summary>
  
```
Enter a number: 42
42 is a valid number!
```
</details>

### <a name="datachange"></a> 6. Changing Data Types

**Type Conversion** (or Type Casting) is when you convert one data type to another. In Python, you can convert between different data types using built-in functions.

#### Basic Type Conversion
```python
# Converting strings to numbers
text_number = "42"
number = int(text_number)      # Convert to integer
decimal = float(text_number)   # Convert to float

print(f"String to Integer: {number}")
print(f"String to Float: {decimal}")
```

<details>
<summary>Output</summary>
  
```
String to Integer: 42
String to Float: 42.0
```
</details>

#### Common Conversions
```python
# Converting numbers to strings
age = 12
height = 1.75
age_text = str(age)          # Integer to string
height_text = str(height)    # Float to string

print(f"Number types: age is {type(age)}, height is {type(height)}")
print(f"After conversion: age is {type(age_text)}, height is {type(height_text)}")
```

<details>
<summary>Output</summary>
  
```
Number types: age is <class 'int'>, height is <class 'float'>
After conversion: age is <class 'str'>, height is <class 'str'>
```
</details>

#### Converting User Input
```python
# Getting numbers from user input
user_age = int(input("Enter your age: "))    # Convert input to integer
user_height = float(input("Enter your height in meters: "))  # Convert input to float

print(f"Next year you will be {user_age + 1} years old")
print(f"Your height in centimeters is {user_height * 100}")
```

<details>
<summary>Output</summary> 
  
```
Enter your age: 12
Enter your height in meters: 1.5
Next year you will be 13 years old
Your height in centimeters is 150.0
```
</details>



### <a name="string"></a> 7. Strings

**Strings** are sequences of characters (text). They can be created using single quotes (`'`) or double quotes (`"`).

#### Creating Strings
```python
# Different ways to make strings
name = "Alice"
message = 'Hello, World!'
long_text = """This is a
multi-line
string"""

print(name)
print(message)
print(long_text)
```

<details>
<summary>Output</summary>
  
```
Alice
Hello, World!
This is a
multi-line
string
```
</details>

#### String Methods
```python
text = "Hello, Python!"

# Common string methods
print(text.upper())         # Makes all letters uppercase
print(text.lower())         # Makes all letters lowercase
print(text.replace("Hello", "Hi"))  # Replaces text
print(text.split(","))      # Splits string into a list
```

<details>
<summary>Output</summary>
  
```
HELLO, PYTHON!
hello, python!
Hi, Python!
['Hello', ' Python!']
```
</details>

#### String Operations
```python
first = "Hello"
last = "World"

# Combining strings
print(first + " " + last)  # Adding strings together
print(f"{first} {last}")   # Using f-strings

# Getting string length
text = "Python"
print(f"Length of {text}: {len(text)}")  # Count characters

# Check if something is in a string
message = "I love Python"
print("Python" in message)  # Checks if "Python" is in the string
```

<details>
<summary>Output</summary>
  
```
Hello World
Hello World
Length of Python: 6
True
```
</details>


### <a name="math"></a> 8. Operators and Basic Math

#### Arithmetic Operators

Python has several arithmetic operators for basic math:

| Operator | Name | Example | Result |
|----------|------|---------|---------|
| + | Addition | 5 + 3 | 8 |
| - | Subtraction | 5 - 3 | 2 |
| * | Multiplication | 5 * 3 | 15 |
| / | Division | 5 / 3 | 1.666... |
| // | Floor Division | 5 // 3 | 1 |
| % | Modulus | 5 % 3 | 2 |
| ** | Exponentiation | 5 ** 3 | 125 |

```python
x = 10
y = 3

# Basic arithmetic operations
sum_result = x + y      # 13
diff_result = x - y     # 7
prod_result = x * y     # 30
div_result = x / y      # 3.333...
floor_div = x // y      # 3
remainder = x % y       # 1
power = x ** y          # 1000
```

## Comparison Operators

Use these to compare values:

| Operator | Meaning | Example | Result |
|----------|---------|---------|---------|
| == | Equal to | 5 == 5 | True |
| != | Not equal to | 5 != 3 | True |
| > | Greater than | 5 > 3 | True |
| < | Less than | 5 < 3 | False |
| >= | Greater than or equal to | 5 >= 5 | True |
| <= | Less than or equal to | 5 <= 3 | False |

```python
a = 5
b = 7

# Comparison operations
equal = a == b          # False
not_equal = a != b      # True
greater = a > b         # False
less = a < b            # True
greater_equal = a >= b  # False
less_equal = a <= b     # True
```

## Assignment Operators

These operators combine arithmetic with assignment:

| Operator | Example | Equivalent to |
|----------|---------|---------------|
| = | x = 5 | x = 5 |
| += | x += 3 | x = x + 3 |
| -= | x -= 3 | x = x - 3 |
| *= | x *= 3 | x = x * 3 |
| /= | x /= 3 | x = x / 3 |
| //= | x //= 3 | x = x // 3 |
| %= | x %= 3 | x = x % 3 |
| **= | x **= 3 | x = x ** 3 |

```python
number = 10
number += 5    # number is now 15
number *= 2    # number is now 30
number -= 5    # number is now 25
number /= 5    # number is now 5.0
```
### <a name="return"></a>9. Return Statement

**Return** specifies what a function should give back when it's called.

### Basic Return
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```
<details>
<summary>Output</summary>

```
8
```
</details>

### Return Multiple Values
```python
def calculator(a, b):
    return a + b, a - b, a * b

sum, diff, prod = calculator(4, 2)
print(sum, diff, prod)
```
<details>
<summary>Output</summary>

```
6 2 8
```
</details>

### Early Return
```python
def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(4))
print(is_even(5))
```
<details>
<summary>Output</summary>

```
True
False
```
</details>

### Return None
```python
def no_return():
    print("This function does something")

result = no_return()
print(result)
```
<details>
<summary>Output</summary>

```
This function does something
None
```
</details>

### <a name="functions"></a>10. Functions

**Functions** are reusable blocks of code that perform a specific task. They help organize your code and make it more readable.

### Basic Function Definition
```python
def greet(name):
    print("Hello, {name}!")

# Calling the function
greet("Alice")
```
<details>
<summary>Output</summary>

```
Hello, Alice!
```
</details>

### Parameters and Arguments
```python
def add(a, b):
    return a + b

# Calling the function
result = add(5, 3)
print(result)
```
<details>
<summary>Output</summary>

```
8
```
</details>

### Default Parameters
```python
def power(base, exponent=2):
    return base ** exponent

# Calling with default exponent
print(power(3))     

# Calling with custom exponent
print(power(3, 3))  
```
<details>
<summary>Output</summary>

```
9
27
```
</details>

### Multiple Return Values
```python
def min_max(numbers):
    return min(numbers), max(numbers)

# Unpacking return values
lowest, highest = min_max([1, 2, 3, 4, 5])
print(f"Lowest: {lowest}, Highest: {highest}")
```
<details>
<summary>Output</summary>

```
Lowest: 1, Highest: 5
```
</details>

### Lambda Functions (One-Line Functions)
```python
# Lambda function to square a number
square = lambda x: x ** 2
print(square(4))
```
<details>
<summary>Output</summary>

```
16
```
</details>

### Function with Docstring
```python
def calculate_stats(numbers):
    """
    Calculate statistical summary of a list.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        dict: Dictionary with mean, min, and max
    """
    return {
        'mean': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }

# Using the function
stats = calculate_stats([1, 2, 3, 4, 5])
print(stats)
```
<details>
<summary>Output</summary>

```
{'mean': 3.0, 'min': 1, 'max': 5}
```
</details>

### Keyword Arguments
```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

# Using keyword arguments
describe_pet(animal_type="hamster", pet_name="Harry")
describe_pet(pet_name="Willie", animal_type="dog")
```
<details>
<summary>Output</summary>

```
I have a hamster named Harry
I have a dog named Willie
```
</details>

### <a name="if-statements"></a>11. If Statements

**If statements** allow you to make decisions in your code based on certain conditions.

### Basic If Statement
```python
age = 18
if age >= 18:
    print("You are an adult")
```
<details>
<summary>Output</summary>

```
You are an adult
```
</details>

### If-Else Statement
```python
score = 75
if score >= 70:
    print("You passed!")
else:
    print("You need to study more")
```
<details>
<summary>Output</summary>

```
You passed!
```
</details>

### If-Elif-Else Statement
```python
grade = 85
if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")
else:
    print("Needs improvement")
```
<details>
<summary>Output</summary>

```
B grade
```
</details>

### Nested If Statements
```python
temperature = 25
humidity = 60
if temperature > 20:
    if humidity < 70:
        print("Comfortable weather")
    else:
        print("Feels humid")
```
<details>
<summary>Output</summary>

```
Comfortable weather
```
</details>

### Logical Operators
```python
x = 10
y = 5
if x > 0 and y < 10:
    print("Both conditions are true")

if x == 10 or y == 6:
    print("At least one condition is true")
```
<details>
<summary>Output</summary>

```
Both conditions are true
At least one condition is true
```
</details>

### <a name="loops"></a>12. Loops

**Loops** help you repeat code multiple times.

### For Loop with Range
```python
for i in range(5):
    print(i)
```
<details>
<summary>Output</summary>

```
0
1
2
3
4
```
</details>

### For Loop with List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
<details>
<summary>Output</summary>

```
apple
banana
cherry
```
</details>

### While Loop
```python
count = 0
while count < 3:
    print(count)
    count += 1
```
<details>
<summary>Output</summary>

```
0
1
2
```
</details>

### Break Statement
```python
for number in range(10):
    if number == 5:
        break
    print(number)
```
<details>
<summary>Output</summary>

```
0
1
2
3
4
```
</details>

### Continue Statement
```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```
<details>
<summary>Output</summary>

```
0
1
3
4
```
</details>

### Nested Loops
```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```
<details>
<summary>Output</summary>

```
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```
</details>