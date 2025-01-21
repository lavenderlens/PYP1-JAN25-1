# the standard, built-in datatypes
# literals, or single values, OR expressions that evaluate to them
# IMMUTABLE by default

# bool. or boolean
# values: True or False
# immutable type (values cannot be changed, just re-referenced)

my_bool = True
my_bool = False#a re-assignment of the same reference to point to a different value
# NOT a mutation of that value

# int. or integer/whole number value
# values: whole numbers, negative or positive, OR an expression that evaluates to a whole number
# immutable type (values cannot be changed, just re-referenced)

my_int = 1
my_int = 2

# float. or floating-point/decimal number value
# values: fractional numbers, negative or positive, with the dot character OR an expression that evaluates to a number
# immutable type (values cannot be changed, just re-referenced)

my_float = 1.0
my_float = 1.5

# str (strings)
# values: any characters of zero or more
# immutable type
# single, double OR triple-quoted
# zero indexed (from first character)
# have a length property, obtained by using len()

my_str = "Hello"
first_character = my_str[0]
print(first_character)#H
print(len(my_str))#5
# print(my_str[5])#IndexError: string index out of range
# tehre are only 5 elements numbered from zero to four
# index position 5 is sixth element - does not exist

# string methods do not mutate the original
print(my_str.upper())
print(my_str)#original unchanged
# we may re-assign a new value to the same refernce
# that doesn't mean the value itself is mutated
# just swapped out for a different one
my_str = my_str.upper()#re-assigned
print(my_str)
# we may re-assign the reference (LHS of = assignment operator)
# doing so give the APPEARANCE we have changed the data
# but we have not, just swapped in different data.

# CONTAINER TYPES (for multiple values)

# LIST LST() OR [] INSTANTIATED
# multiple values
# may be of same type but strictly do not have to be
# mutable by default
# commonly used for items of same type
# permits duplicates

my_list = ["bat", "ball", "gloves"]
my_list_copy = my_list#copied reference
print(my_list)
# access a member by group name and index:
print(my_list[0])#gives first element
# update member
my_list[1] = "cricket ball"
# add new member
my_list.append("whites")#adds to end of list
print(my_list)
print(len(my_list))#expect 4 got 4
print(my_list_copy)#same as my_list

# tuple 
# a datatype that CANNOT have its elements re-assigned
# permits duplicates

my_tuple = ("bat", "ball", "gloves")
my_tuple = ("goal", "football", "boots")#OK
print(my_tuple)#('goal', 'football', 'boots')
# my_tuple[0] = "sliothair"#TypeError: 'tuple' object does not support item assignment

# using tuples it may appear we can group unrelated data together:
my_restaurant = ("The end of the universe", 42, True)
# and when tuples are commonly returned from functions
# this is what we will see
# but best practice is to store ONE type of thing

# sets
# values: the elements can be of any type
# sets are NOT ORDERED
# sets may NOT contain duplicates
# set methods are powerful ways of examining sets and returning differences and similarities
my_set = {1,2,2,3,4,5,5}
# note DICTIONARIES ALSO take {} but store key:value pairs
print(my_set)#{1, 2, 3, 4, 5}#no duplicated values
my_other_set = {"one", "two", "two", "forty-four", "ninety-one", "a-one"}
print(my_other_set)
# {'two', 'a-one', 'ninety-one', 'forty-four', 'one'}
# {'forty-four', 'one', 'ninety-one', 'a-one', 'two'}

# dictionaries
# values: key: value, pairs, comma-separated
# keys: may be of any type but are commonly strings
# keys must be unique
# values: may be of any type and may be duplicated
# mutable
# note: a Python dict is NOT the same as an object, 
# even though they both print out with curly braces and key: value pairs !
# neither are dicts the same as sets, even though both are encoded with curly braces
# objects are made by classes
# the way we drill down into properties is different
# theoretically EVERYTHING is an object in Python

my_dict = {"name": "Fred", "age": 21, "employed" : True}
print(my_dict)

# None type
my_none = None
print(type(my_none)) # <class 'NoneType'>
# use None where you would use null in other languages -
# to de-reference objects we no longer require
my_dict = None
print(my_dict)

# TODO truthiness
# everything in Python is inherently TRUTHY or FALSEY
# that is, when passed to a bool() function, it returns True or False
print(type(my_tuple))#<class 'tuple'>
print(type(my_list))#<class 'list

print(bool(my_list))#True
print(bool(my_tuple))#True
print(bool([]))#False
print(bool(()))#False
print(bool(1))#True
print(bool(0))#False
print(bool([1,2,3]))#True
print(bool(""))#False
print(bool("x"))#True


