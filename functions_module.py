'''
functions, as in any other language, wrap one or more LOC in a function name
to be called zero, one, or many times at some time in the future
functions are commonly defined in a script ON THEIR OWN, with no runtime code
the script with the runtime code in it, that USES the functions,
is separate, and IMPORTS them from the first script
the first script is called a module

how short can a function be?
1 LOC
why? to make code more declarative
the function name may be more descriptive than its workings
how long can a function be?
Not too long.
As a rule of thumb I would be wary of functions over 50-100 LOC
It is very likely they will have dependencies on other code.
If that other code were to break, so would your function.
You may never know this while unit testing
if a function consistently produces the same result for the same given input
it is said to be pure, or idempotent 
pure functions are much easier to test in an automated test environment
we do not have to mock dependencies that may change independently of the function
'''

def add_two_numbers(num1, num2):
    return num1 + num2
# generally, all such code is not in the module:
# result = add_two_numbers(2,2)#should be refactored outside this module
# print(result)
# print(add_two_numbers(4,4))#output as input
# print(result := add_two_numbers(8,8))#both assigns and returns
# def add_two_numbers(num1, num2):#parameters at function definition time
# arguments at function runtime (real data)

def print_sum_of_two_numbers(num1, num2):
    print(num1 + num2)
# runtime code in module, expect 32
# refactored to name builtin: see bottom of module
# print(result := print_sum_of_two_numbers(16,16))#None - nothing returned to the system

# with input, output, there are 4 basic function types
# runtime code in module expect 3 print statements
# print("Hello")
# print("from a function")
# print("How are you today?")
# candidate code to wrap in a function 

#  WAY 1: no input, no output
def greet1():
    print("Hello")
    print("from greet1")
    print("How are you today?")

#  WAY 2: no input, output
def greet2():
     return "Hello\nfrom greet2\nHow are you today?"

#  WAY 3: input, output
def greet3(name):
     return f"Hello\nfrom {name}\nHow are you today?"

# WAY 4: input, no output
def greet4(name):
    print("Hello")
    print(name)
    print("How are you today?")

# positional and named args
def greet5(name, age):
    return f"Hello {name}, you are {age + 1} next birthday."

# Q: what says that age should be a number?
# A: nothing (with positional arguments)
# if you wanted to type the args you would have to write custom code
# e.g. if type(age) == 'int'

def greet6(name, age):
    return f"Hello {name}, you are {age + 1} next birthday."

# print(greet6("Alan", "21"))#TypeError: can only concatenate str (not "int") to str

def greet7(name="name", age=21):
    return f"Hello {name}, you are {age + 1} next birthday."

# ########################
# named vs positional args
# ########################


# hide any runtime code in module by dunder (double underscore/magic methods) method:
if __name__ == "__main__":
    print(result := print_sum_of_two_numbers(16,16))#32, None
    print("Hello")
    print("from a function")
    print("How are you today?")
    #None - nothing returned to the system
    print('''
    # ########################
    # named vs positional args
    # ########################
    ''')
    # print(greet6(21, "Alan"))#TypeError: can only concatenate str (not "int") to str
    print(greet7(age=21, name="Alan"))#STILL RUNS - args in "wrong" order
    print(greet7())#STILL RUNS - NO args

# answer is named args - TODO tomorrow