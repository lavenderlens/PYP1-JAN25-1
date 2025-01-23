import functions_exercise_module

# different ways of importing from a module

# WAY 1: fully-qualified name
print(functions_exercise_module.get_greeting("Alan"))
# pros: you know exactly which function is being called 
# from exactly what module
# cons: fully-qualified names can be tedious when repeatedly called in the importing script

# WAY 2: named imports (best IMHO)
# print(get_product(2,20)) #will not work if before import:
# NameError: name 'get_product' is not defined

from functions_exercise_module import get_product
# functions individually named in the import
# usage:
print(get_product(2,20))
# pros - you can see exactly which functions from the module are used
# you don't have to repeat the module code
# cons - if your code that calls the functions is a million miles away from the import statement 
# (usually at the top of the script importing)
# function may look like a local one

# WAY 3: the wildcard, *, IMHO worst of all!
from functions_exercise_module import *
# the wildcard is used, meaning ALL functions from the module
# usage:
print(get_first([1,2,3]))
# pros: much faster to write during development
# cons: you have absolutely no clue which functions come from a module

# NONE of the different ways have a perf benefit over the others
# you are only SYMBOLICALLY linking to module code
