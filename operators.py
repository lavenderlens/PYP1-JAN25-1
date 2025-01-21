# an expression involves operators (symbols that perform operations) 
# and operands (values that are transformed by the operator)
x = 1
x = x + 1
# the first line initialises x with a single value, 1
# the second line assigns x the result of an expression - itself plus 1
# the expression has an operator, +
# and two operands, x (again), and 1


# arithemetic operators
# +
# -
# *     - 2 squared is 2 * 2
# **    - 2 ** 3 is 2 cubed
# /
# %     - remainder, whole number division
# //    - quotient, whole number division

print(10 / 2)#5.0
print(10 % 2)#0

print(10 / 3)#3.3333333333333335
# promotion going on: result for division is a float if ints are input
# standard for floating-point arithmetic
# IEEE 754 since the 80s
# we should not use float values where accuracy is of primary concern!
# we could format our output, but the inherent inacurracy is still there
print(f"formatted output: {(10/3):.2f}")#formatted output: 3.33

# promotion:
# the process of storing smaller datatypes in larger ones
print(10/3)#yields a float result as likely to have fractions
print(9 + 2)#int result as it will be whole number
print(9 + 2.0)#float result as first operand promoted to match second

# non-numeric arithmetic
print("ho" * 3)
print("*" * 50)

# assignment operators
# = is single assignment
# += is compound assignment
# note these work for strings and numbers both

my_num = 1
my_num = my_num + 1
my_num += 1
print(my_num)#expected: 3

my_string = ""
my_string = my_string + "I "
my_string += "love "
my_string += "Python."
print(my_string)

# note this way of building strings is expensive in memory when long strings are involved
# other methods see https://www.tracedynamics.com/python-string-builder/

# walrus operator
# said to be like a walrus tusks lying on side :=
# assigns AND RETURNS AT ONCE
# BEFORE
x = 1
print(x)
# print(x = 2)#TypeError: print() got an unexpected keyword argument 'x'
# with the walrus operator:
print(y := 2)#2 no errors
print(y)#2

# nested data with respect to tuples in particular
my_nested_dict = {
    "name": "Alan",
    "languages": ("Python", "Java", "JavaScript")
}
# tuple within a dict
# tuple ELEMENTS may not be reassigned
# but the overall reference may be
print(my_nested_dict)
print(my_nested_dict["languages"])
print(my_nested_dict["languages"][0])
# try to re-assign to tuple element:
# my_nested_dict["languages"][0] = "CSS"#TypeError: 'tuple' object does not support item assignment
my_nested_dict["languages"] = ("HTML", "CSS", "JavaScript")
print(my_nested_dict["languages"])#completely swapped out for different tuple

# things that are NOT very Python-esque:

# increment/decrement operators ++ / -- in other languages
# not in Python - use
# += or -= instead

# multiple assignment on on eline:
x = 1; y = 2; z = 3

# this way is much better:
x, y, z = 4, 5, 6
# equivalent in JS destructuring assignment

# assignment operator chaining is confusing to read
x = 1
y = 1
# may be rewritten as
x = y = 1

#  container operators
# dict
my_dict = {"name": "Alan", "age": 21}
# multiple assignment
name, age = my_dict["name"], my_dict["age"]
# NOTE square brackets notation for dict props
#  one of the ways objects differ is to use DOT NOTATION

# list
my_nums = [1,2,3]
first_num, second_num, third_num = my_nums[0], my_nums[1], my_nums[2]

# comparison operators
# <         less than
# <=        less than or equal to
# >         greater than
# >=        greater than or equal to
# 3 >= 4    #order important
# !=        not equal to
# is        tests for IDENTITY: references the same object as

# shallow copying and deep copying
my_list = [1,2,3]
my_other_list = [1,2,3]
my_copied_list = my_list#equality of reference

# using the is operator to establish equality of reference

print(my_list is my_other_list)#False - two separate containers in memory which just happen to contain the same data
print(my_list is my_copied_list)#True - only one container, with two references to it

# the system Python uses to determine if two references point to the same object is built-in id()
print(id(my_list))#4376034688 - same
print(id(my_other_list))#4376022784 - different
print(id(my_copied_list))#4376034688 - same

# because the copy copies the reference only it is called a SHALLOW copy
# the original may be mutated through the new reference
my_copied_list.append(4)
print(my_copied_list)       #[1, 2, 3, 4]
print(my_list)              #[1, 2, 3, 4]

# fortunately Python has a module that specialises in creating immutable (deep) copies
import copy
my_deep_copied_list = copy.deepcopy(my_list)#has 4 in it as 4th element now
my_deep_copied_list.append(5)
print(my_deep_copied_list)#[1, 2, 3, 4, 5]
print(my_list)#[1, 2, 3, 4]


