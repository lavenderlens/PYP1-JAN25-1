# variable declaration
# in Python there is NO keyword to declare a variable, apart from a couple of edge cases - TODO later (global and nonlocal)
# this means that a Python variable MUST be initialised with a value when first declared
# in Python, a variable takes its initial type from the type of the data on the right of the =
# a variable's type can change during the application - any type, at any time

my_variable = 1#declared variable name, assigned initial value of 1

my_name = "Alan"

# we use the type() builtin function to return the datatype

print(type(my_variable)) #<class 'int'>
print(type(my_name))#<class 'str'>

# we may re-assign values and new types after initialisation

my_variable = 1.0
my_name = True

print(type(my_variable)) #<class 'float'>
print(type(my_name))#<class 'bool'>

my_name = {"name": "Alan Lavender"}
print(type(my_name))#<class 'dict'>

# input from user
your_name = input("Enter your name:")
print(your_name)
print(type(your_name))#<class 'str'>


