#!/usr/bin/env python
# coding: utf-8
Question 1. What is an Exception in python? Write the difference between Exceptions and Syntax errors. Answer:In Python, an exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions. When an exception occurs, the program stops executing and Python raises an error message, providing information about what went wrong. Exceptions can occur for a variety of reasons, such as invalid input, file not found, network errors, and so on.

Syntax errors, on the other hand, are errors that occur when the Python interpreter cannot parse the code because of incorrect syntax. These errors usually occur before the program is executed and prevent the program from running at all. Examples of syntax errors include misspelled keywords, missing colons, incorrect indentation, and other similar errors.

The key differences between exceptions and syntax errors are as follows:

1.Timing of occurrence: Syntax errors occur before the program starts running, while exceptions occur during program execution.

2.Cause: Syntax errors are caused by incorrect syntax, whereas exceptions are caused by unexpected situations that occur during program execution.

3.Handling: Syntax errors must be fixed by correcting the code, while exceptions can be handled by using try-except blocks, which allow you to catch the exception and handle it in a way that allows the program to continue running.

4.Error message: Syntax errors usually provide a simple error message indicating the line number and type of error, while exceptions can provide more detailed information about the cause of the error, such as a traceback and a description of the error type.Question 2.What happens when the exception is not handled? Explain with example. Answer. When an exception is not handled in Python, the program will terminate and display an error message that includes a traceback showing the chain of function calls that led to the exception.

Here's an example to illustrate what happens when an exception is not handled:
# In[1]:


def divide(x, y):
    result = x / y
    return result

# Example 1: handling the exception
try:
    result = divide(5, 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is:", result)

# Example 2: not handling the exception
result = divide(5, 0)
print("Result is:", result)

Question 2.What happens when the exception is not handled? Explain with an example. Answer. with an error message displayed on the console or in a log file. This can lead to unexpected behavior and potentially corrupt data or files.

Here's an example to illustrate what happens when an exception is not handled: In this code, we are trying to divide two numbers entered by the user. If the user enters invalid input, such as a string instead of a number, the ValueError exception will be raised and the program will print "Please enter valid numbers." to the console.
# In[ ]:


# Example Question 2
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Please enter valid numbers.")

Question 3. Which Python statements are used to catch and handle exceptions? Explain with example. Answer : In Python, the try and except statements are used to catch and handle exceptions. The try statement is used to enclose the code that may raise an exception, while the except statement is used to define the block of code that will handle the exception if it is raised.

Here's an example of using try and except statements to handle a ValueError exception: In this code, we are trying to divide two numbers entered by the user. If the user enters invalid input, such as a string instead of a number, the ValueError exception will be raised. However, we have enclosed the code that may raise the exception within the try block, and we have defined the block of code that will handle the exception within the except block. If a ValueError exception is raised, the program will print "Please enter valid numbers." to the console.
# In[ ]:


# Example Question 3?
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Please enter valid numbers.")

"""We can also use multiple except statements to handle different types of exceptions. Here's an example:"""
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Question 4 :Explain with an example : a. try and else b. finally c. raise Answer:

a. try and else: In Python, the else block can be used along with the try block to specify a code block that should be executed when no exception occurs in the try block. Here's an example: In this code, we are trying to divide two numbers entered by the user. If the user enters invalid input, such as a string instead of a number, a ValueError exception will be raised. If the user enters zero as the second number, a ZeroDivisionError exception will be raised. If neither exception occurs and the division operation is successful, the else block will execute and print the result.

b. finally: In Python, the finally block can be used to specify a block of code that should be executed whether or not an exception occurs in the try block. Here's an example: In this code, we are trying to open a file named "myfile.txt" for reading. If an IOErro exception occurs while trying to open the file, the program will print an error message. Regardless of whether or not an exception occurs, the finally block will execute and close the file.

c. raise: In Python, the raise statement can be used to raise an exception. Here's an example: In this code, we are defining a function named divide that performs division and raises a ZeroDivisionError exception if the second argument is zero. We are then calling the divide function with arguments 10 and 0 inside a try block. Since the second argument is zero, a ZeroDivisionError exception will be raised and caught in the except block, where we print the error message.
# In[ ]:


"""example for a"""
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"The result is: {result}")

"""example for b"""
try:
    f = open("myfile.txt", "r")
    # perform some file operations
except IOError:
    print("Error: could not open file")
finally:
    f.close()

"""Example for c"""
def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)

Question 5 : What are custom exception in python ? Why do we need custom exception in python.? Explain with an example. Answer :In Python, custom exceptions are user-defined exceptions that are created by the programmer to represent specific errors that may occur in a program. Custom exceptions allow the programmer to define their own error conditions and provide custom error messages, which can make it easier to debug and maintain the code.

We need custom exceptions in Python because built-in exceptions may not always be specific enough to describe the type of error that occurred in our code. For example, if we are building an application that reads and writes files, and encounters an error while reading a file, the built-in IOError exception may not provide enough information to determine the cause of the error. In such cases, we can define our own custom exception, such as FileReadError, to represent this specific error condition. ere's an example of defining and using a custom exception in Python:
# In[ ]:


class FileReadError(Exception):
    def __init__(self, filename):
        self.filename = filename
    
    def __str__(self):
        return f"Error reading file {self.filename}"

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            # perform file operations here
    except IOError:
        raise FileReadError(filename)

try:
    read_file("myfile.txt")
except FileReadError as e:
    print(e)

In this code, we have defined a custom exception named FileReadError that inherits from the base Exception class. The FileReadError exception takes a filename argument in its constructor, and overrides the __str__ method to provide a custom error message.

We are then defining a function named read_file that reads a file and raises a FileReadError exception if an IOError occurs while trying to read the file.

In the try block, we are calling the read_file function and catching any FileReadError exceptions that may be raised. If a FileReadError exception is caught, we print the error message. Using custom exceptions can make our code more readable and easier to maintain, as it allows us to handle specific error conditions in a more meaningful way.Question 6 : Create a custom exception class. Use that class to handle and exception. Answer :In this code, we have defined a custom exception class named NegativeNumberError that inherits from the base Exception class. The NegativeNumberError exception is raised when the input to the calculate_squarefunction is a negative number.

We are then defining a function named calculate_square that calculates the square of a number, and raises a NegativeNumberError exception if the input is negative.

In the try block, we are calling the calculate_square function with a negative number (-5). Since the input is negative, a NegativeNumberError exception is raised. We are catching the exception in the except block and printing the error message.
# In[ ]:


class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def calculate_square(num):
    if num < 0:
        raise NegativeNumberError("Input must be a positive number")
    return num**2

try:
    result = calculate_square(-5)
    print(result)
except NegativeNumberError as e:
    print(f"Error: {e}")


# In[ ]:




