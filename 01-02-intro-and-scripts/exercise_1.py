# 1. Create a script named exercise1_console_io.py.
# 2. Prompt the user to input his/her name and capture it in variable named name.
# 3. Prompt the user to input his/her age and capture it in a variable named age.
# 4. Print the user's name and age to the console. You might try doing this with one
# invocation of the built-in print function.
# 6. Optionally, try adding 1 to the age and display it as age next birthday.

# name = input("Enter your name:")
name = "AL"#testing
# this for handiness is often used
# but where something may go wrong with the input() function, 
# separate lines may be better:
# print("Enter your name:")# this should never go wrong
# name = input()#this might go wrong
# age = input("Enter your age:")
age = "21"#testing

print(name, age)

print(type(name))#<class 'str'>
print(type(age))#<class 'str'>

print("Name:", name, "Age:", age)#here Python is printing the string represntation of each variable
# concatenation: combining strings together
print("Name:" + name + "Age:" + age)#the commas provide spaces, concatention does not
# print age + 1: next birthday
# print("Name: " + name + " Age next birthday: " + age + 1)#TypeError: 
# can only concatenate str (not "int") to str
# the number 1 is causing this error
print("Name: " + name + " Age next birthday: " + age + str(1))#Name: ted Age next birthday: 211
# what we really want to do is coerce the type of age to number
age = int(age)#age is now number
print(type(age))
print("Name: " + name + " Age next birthday: " + str(age + 1))#Name: AL Age next birthday: 22

# PLACEHOLDERS Python 3 >
print("Name: {} Age next birthday: {}".format(name, (age + 1)))

# PLACEHOLDERS Python 3.5 >
print(f"Name: {name} Age next birthday: {age + 1}")

# PLACEHOLDERS Python 3.7 >
print(f"""
Name: {name} 
Age next birthday: {age + 1}
""")
# triple quotes may be either single or double quote characters
# triple quotes preserve line breaks in code

number_from_input = input("Enter a number:")
# number_from_input_to_int = int(number_from_input)
# print(type(number_from_input_to_int))#<class 'int'>
# if however I enter a decimal:
# ValueError: invalid literal for int() with base 10: '1.0'\
number_from_input_to_float = float(number_from_input)
print(type(number_from_input_to_float))#<class 'float'>
# when a whole number is added, the float() wrapper DOES NOT CRASH
# why?
# implicit type coercion happens in second example
# int (1) was entered, and automatically represented as a float (1.0) with the same value



