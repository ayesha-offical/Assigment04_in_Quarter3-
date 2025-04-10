# What is a Module in Python?

# A module in Python is a file that contains Python code (functions, classes, variables, or even runnable code) and is used to organize and reuse code efficiently.

# A module is simply a .py file that can be imported and used in other Python programs.

# Modules help keep the code modular, readable, and maintainable.

# Python has built-in modules (like math, random, os) and also allows users to create custom modules.

# Types of Modules in Python
# 1. Built-in Modules (Standard Library)
# Pre-installed modules in Python.
# Example: math, random, os, sys
import os 

print(os.getcwd()) # Get the current working directory
os.mkdir("new_folder") # Makes a new folder called "new_folder"

# 2. User-Defined Modules (Custom Modules)
# Any Python file (.py) you create can be used as a module.

import mymodule
print(mymodule.sub(10, 5)) # Call the sub function from mymodule.py


# 3. External Modules (Third-party Libraries)

# Installed via pip (pip install module_name).
# Example: numpy, pandas, requests

import requests 
response = requests.get("https://fake-json-api.mock.beeceptor.com/users")
print(response.status_code) # Print the status code of the response

# How to Import a Module in Python?

# Python provides several ways to import modules:

# 1. Basic Import

import math
print(math.sqrt(16)) # Print the square root of 16

# 2. Import with Alias (as)

import math as m

print(m.sqrt(16)) # Print the square root of 16 using the alias 'm'


# 3. Import Specific Functions or Variables (from ... import ...)
from math import sqrt, pi

print(sqrt(16)) # Print the square root of 16 without using the math prefix
print(pi)

from math import sqrt as s, pi as p
print(s(16)) # Print the square root of 16 using the alias 's'
print(p) # Print the value of pi using the alias 'p'

# 4. Import Everything (from module import *) (Not recommended for large modules)

#  Example (using math):

from math import *
print(sqrt(25))


# Advantages of Using Modules
# ✔ Code Reusability – Write once, use anywhere.

# ✔ Organization – Keep related functions together.

# ✔ Namespace Management – Prevents variable conflicts.

# ✔ Faster Development – Use existing libraries instead of writing everything from scratch.




# Understanding Functions in Python
# A function is a block of reusable code that performs a specific task.
# Functions help in breaking down complex problems into smaller, manageable pieces.
# They can take inputs (arguments) and return outputs (results).
# Functions can be defined using the def keyword followed by the function name and parentheses.
# The code block within the function is indented.
# Functions can be called by their name followed by parentheses.

# Example:

def my_func ():
    print("Hello, World from a Ayesha!") # Print "Hello, World!"

my_func() # Call the function to execute it

# Types of Python Functions
# Python provides the following types of functions −

# 1) Built-in functions

# Python's standard library includes number of built-in functions. Some of Python's built-in functions are print(), int(), len(), sum(), etc. These functions are always available, as they are loaded into computer's memory as soon as you start Python interpreter.
# 2) Functions defined in built-in modules

# The standard library also bundles a number of modules. Each module defines a group of functions. These functions are not readily available. You need to import them into the memory from their respective modules.
# 3) User-defined functions

# In addition to the built-in functions and functions in the built-in modules, you can also create your own functions. These functions are called user-defined functions.


# Built-in functions
# Python has many built-in functions that are always available. Some examples include:
# print(), len(), type(), int(), str(), etc.
# These functions can be used without any import statements.
# Example:

print("Hello, World!") # Print "Hello, World!"

# Functions defined in built-in modules
# Python's standard library includes many modules, each containing functions. Some examples include:
# math, random, datetime, etc.
# These modules need to be imported before use.
# Example:
import random
print(random.random()) 

# User-defined functions


# User-defined functions are created using the def keyword. The function definition includes a name, parameters, and a code block.
# Example:
def add(a, b):
    return a + b

result = add(5, 10) # Call the add function with arguments 5 and 10

# Syntax to Define a Python Function

# The syntax to define a function in Python is as follows:

def funct():
    "This is a function"
    function_body="hello from here"
    return function_body
final_funct= funct()
print(final_funct) # Call the function and print the result


# Pass by Reference vs Value
# Python uses pass by object reference. Immutable objects (e.g. integers) are unchanged, while mutable objects (e.g. lists) are modified. Examples:
# Integers: x = 5 remains 5 after modification.
# Lists: x = [1, 2, 3] becomes [1, 2, 3, 4] after appending 4.
# Example:

# # Immutable Example (like integers):

def modifyinge(a):
    a= 90
    print(("Within Function:", a)) # Print the modified value of a


# immutible Object (integer)
a = 10
print("Orignal: ", a) # Print the original value of a

# modifyiing value

modifyinge(a)
print("After Function Call:", a) # Print the value of a after function call

# Mutable Example (like lists):

def modify_list(lst):
    lst.append(7)
    print("Inside Function:", lst, " - ID:", id(lst)) # Print the modified list

# Mutable Object (list)
lst = [1,2,3]

print("Original List:", lst, " - ID:", id(lst)) # Print the original list

# Modifying value
modify_list(lst)

print("After Function Call:", lst, " - ID:", id(lst)) # Print the value of lst after function call


# Function Arguments

# Function arguments are the values or variables passed into a function when it is called.

def greet (name):
    print("Hello,", name)

greet("Ayesha") # Call the greet function with the argument "Ayesha"
greet("Ano") # Call the greet function with the argument "
greet("Ali") # Call the greet function with the argument "Ali"
greet("Sara") # Call the greet function with the argument "Sara"

# ✨ Types of Function Arguments in Python:
# Positional Arguments

# Keyword Arguments

# Default Arguments

# Variable-Length Arguments (*args, **kwargs)


# 🔹 2. Keyword Arguments

def intro(name, age):
    print(f"{name} is {age} year Old")

intro(age=18, name="Ayesha") # Call the intro function with keyword arguments    


# ✅ * Unpacking Iterables
# The * operator unpacks (opens up) an iterable like a list, tuple, or set — turning its elements into individual values.

# Example:

def add(a, b, c):
    print(a + b + c)

numbers = [1, 2, 3]

add(*numbers)  # Unpacks to: add(1, 2, 3)

# Without *, Python would throw an error:
add(numbers)   # ❌ Error: it tries to pass the whole list as one argument


#  What is a Default Argument?
# A default argument is used when:

# You don’t give a value for a parameter in the function call.

# # Python will use the default value you defined in the function.

# Example:
def greet(name="Friend"):
    print("Hello,", name)
greet() # Call the greet function without an argument (uses default value)
greet("Ayesha") # Call the greet function with the argument "Ayesha"

# 🧠 Explanation:
# In greet(), we didn’t give a name → so it used "Friend" (the default).

# In greet("Ayesha"), we gave a value → so it used "Ayesha" instead.

# Syntex:

# def function_name(x, y, /):
# function body
# Explanation:
# The / means that x and y can only be provided by their position, not by name.

# 🌟 Example:

def add(x, y, /):
    return x+y

# correct way

print(add(2, 3))  # Correct: positional arguments

# incorrect way
print(add(x=2, y=3))  # ❌ Error: keyword arguments not allowed


# 🎯 Why use Positional-only Arguments?
# Ensure correct order of arguments.

# Prevent misuse of keyword arguments.

# Improve code readability by enforcing a standard argument order.

# 📌 Syntax for Keyword-only Arguments:

# def function_name(x, y, *, z):
#     # function body
# Explanation:
# The * means that z must be passed as a keyword argument, while x and y can be positional or keyword.

# 🌟 Example:

def greet(name, age, *, city):
    print(f"{name} is {age} years old and lives in {city}.")

# correct way
greet("Ayesha", 18, city="Karachi") # Call the greet function with keyword argument for city

# incorrect way
greet("Ayesha", 18, "Karachi") # ❌ Error: city must be a keyword argument


# 🎯 Why use Keyword-only Arguments?
# Clarifies the function call by making the argument names explicit.

# Prevents accidental mistakes by ensuring that the arguments are passed in the correct way.

# Increases readability since you explicitly know what each argument means.

# 📝 Key Takeaway:
# * means that the arguments after it must be keyword arguments.

# Cannot be passed by position. They must be passed as param=value.

# ✅ What are Arbitrary or Variable-length Arguments?
# Arbitrary arguments allow you to pass a variable number of arguments to a function.

# You can pass any number of arguments (including none) without specifying them in the function definition.

# This is useful when you're not sure how many arguments the user might provide.

# 📌 Syntax for Non-keyword Variable Arguments (*args):
# def function_name(*args):
    # function body
# The *args allows the function to accept any number of positional arguments.

# The arguments are packed into a tuple.

# 🌟 Example of *args:

def function_name(*args):
    for num in args:
        print(num)

function_name(1, 2, 3, 4, 5)  # Call the function with arguments 1, 2, 3, 4, 5
function_name(10, 20)  # Call the function with arguments 10, 20

# In this example, *args can accept any number of arguments.

# It collects all the passed arguments into a tuple called args.

#  How does *args work?
# If no arguments are passed, args is an empty tuple.

# If multiple arguments are passed, args is a tuple containing all the values.

# ✅ What is the return Keyword in Python?
# The return keyword is used to exit the function and optionally return a value to the calling code.

# After the function hits the return statement, it ends and the program control goes back to where the function was called.

# If no value is provided, the function returns None by default.

# 📌 Syntax for Returning a Value:
# def function_name():
#     return value  # Return a value to the caller

# 🌟 Example with Return Value:

def add(a, b):
    return a + b  # Return the sum of a and b

result = add(5, 10)  # Call the add function and store the result

print(result)  # Print the result

# Here, add(5, 3) calls the function, and the result (8) is returned and stored in the variable result.

# The value can be used for further operations or printed.


# 🧠 Key Points about return:
# Ending the Function:

# When Python reaches the return statement, it exits the function.

# Returning Values:

# 1: The value after return is sent back to the place where the function was called.

# 2: Returning Multiple Values:

# 3: You can return multiple values by separating them with commas. Python automatically converts them into a tuple.

# 🎯 Why is it good practice to use return explicitly?
# It makes the function’s behavior clear to the reader.

# It helps in control flow management and makes debugging easier.

# Without return, a function implicitly returns None, which can be confusing if the function is expected to return something useful.

# In Python, anonymous functions are those that are defined without a name. These are typically created using the lambda keyword, which allows you to write functions in a single line without the need for the def keyword. The syntax for a lambda function is:

# lambda arguments: expression

# Key points:
# Lambda functions are often used when you need a simple function for a short period, and you don't want to formally define it using def.

# Lambda functions can be passed as arguments to higher-order functions like map(), filter(), and reduce().


numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]

# Global vs Local Variables in the Same Scope:
# If a local variable has the same name as a global variable, the local variable will take precedence inside that function. The global variable can still be accessed using the global keyword if needed.

# Example of shadowing (local variable overriding a global one):

x = 10  # Global variable

def my_function():
    x = 5  # Local variable, shadows the global variable
    print(x)

my_function()  # Output: 5
print(x)  # Output: 10 (global x remains unchanged)

# The **kwargs in Python allows you to pass a variable number of keyword arguments to a function. It stands for "keyword arguments" and collects all the keyword arguments passed to the function into a dictionary. The keys in the dictionary are the argument names, and the values are the corresponding argument values.


# Syntax:

# def my_function(**kwargs):
#     # kwargs is a dictionary
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")


# Example:
def display_information(**student):
    for key, value in student.items():
        print(f"{key} = {value}")

# Passing arbitrary keyword arguments
display_information(name="Ayesha", age=18, city="Kraachi")

# Key Points:
# **kwargs collects keyword arguments as a dictionary where the keys are argument names and the values are their corresponding values.

# The order of keyword arguments doesn't matter when using **kwargs because they are stored in a dictionary, which is unordered (as of Python 3.7, the insertion order is preserved, but it’s still not ordered like a list).

# You can use **kwargs along with normal positional arguments and other keyword arguments. However, **kwargs should always come last in the function definition.



# Key Features of Generator Functions:
# Lazy Evaluation:

# The values are generated only when needed. When the generator is iterated over (e.g., in a for loop), it yields the next value one by one.

# Memory Efficiency:

# Instead of storing the entire sequence of values, a generator only holds one value at a time in memory, making it much more memory-efficient, especially when dealing with large datasets or infinite sequences.

# Iterable:

# A generator function returns a generator object that can be iterated over using a for loop or manually using the next() function.

# Resumable:

# The state of the generator function is preserved between yield calls. This means when a yield is hit, the function’s execution is paused, and when the next value is requested, it resumes from where it left off.

# Syntax of a Generator Function:

# def my_generator():
#     yield value  # Instead of returning a value, use 'yield' to yield it

# Example of Simple Generator Function:
# Let’s create a simple generator that yields numbers from 1 to 3:

def count_up_to(limit):
    count =1
    while count <= limit:
        yield count  # Yield the current count
        count += 1  # Increment the count

# Now, let's create an instance of the generator and iterate over it:
counter = count_up_to(3)

for number in counter:
    print(number)  # Output: 1, 2, 3


#     How it works:
# The count_up_to() function is a generator function. Instead of returning all values at once, it yields one number at a time.

# When the generator is iterated over using for, it produces values one by one until the condition is met (count <= limit).

# Example 2: Infinite Sequence

# Generators are useful for generating infinite sequences since they don’t store all values in memory.

def infinite_count():
    count = 1
    while True:
        yield count  # Yield the current count
        count += 1  # Increment the count

gen = infinite_count()

for i in range(5):
    print(next(gen))  # Output: 1, 2, 3, 4, 5


# Recursive Function in Python:
# A recursive function calls itself during its execution. It is used to solve problems that can be broken down into smaller subproblems, and the function keeps calling itself with a smaller input until a base case is met.

# Key Components:

# Base Case: This condition stops the recursion. Without it, recursion would continue indefinitely, leading to a stack overflow error.

# Recursive Case: This part of the function calls itself with a modified input, gradually moving towards the base case