import functions_module 

# we get all the runtime code from the module in this script!
'''
32
None
Hello
from a function
How are you today?
'''

# AFTER if __name__ == "__main__": added to module

'''
no output from module
'''

# I can now reference any function from the module:

print(greeting := functions_module.greet6("Alan", 21))

# the wider picture is data/method hiding:
# as a dev, we know WHAT functions do from the module
# this is because they are meaningfully named
# we do not need to know HOW they do

# ########################
# named vs positional args
# ########################
print('''
# ########################
# named vs positional args
# ########################
''')

# print(functions_module.greet6(21, "Alan"))#TypeError: can only concatenate str (not "int") to str
print(functions_module.greet7(age=21, name="Alan"))#STILL RUNS - args in "wrong" order
print(functions_module.greet7())#STILL RUNS - NO args
