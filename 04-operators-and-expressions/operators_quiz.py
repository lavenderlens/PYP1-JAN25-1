print("# ARITHMETIC")
print(7 % 3)
print(7 ** 3)
print(7 // 3)
print(7 + 3.5)
print(["ho"] * 3)
# print("The meaning of life is " + 42)#TypeError: can only concatenate str (not "int") to str
print("The meaning of life is " + "42")#fixed
print("The meaning of life is " + str(42))#fixed
print(f"The meaning of life is {41 + 1}")#fixed but better
print(["hee", "haw"] * 3)
print("hee" * 3)
# to multiply strings is possible in Python
# because a special method of the string class is overidden
# to provide this behaviour
# it specifies what the * operator should do, in the case of strings
# more of that in objects and classes session!

print("\n# UNARY")
print(not False)
print(not 2)
# print(not 0)
print(not "")
print(not [1])#containers with content are True
print(not 1) #False too but for a different reason
print("a" > "b") #False based on ASCII values

print("\n# COMPARISON")
print("a" > "b")#ASCII values
# print("abc" > "dbc")#ASCII values
# print("ABC" > "abc")#ASCII values
print([1,2,3] < [1,1,4])#
print([1,2,3] > [1,1,4])#evaluating each member in turn
print("#evaluating each member in turn")
print([1,2,3] > [1,4,1])#
print([1,2,3] >= [1,4,1])#not taking the first comparison 
print([1,4,3] >= [1,2,1])#not taking the first comparison 
print([1,2,3] > [0,1,2])#compares one by one
print((1,2,3) > (0,1,2))#compares one by one but does not aggregate
# print({1,2,3} > {0,1,2})#

print({"a", "b", "c"} == {"b", "a", "c"})#sets are UNordered
print(["a", "b", "c"] == ["b", "a", "c"])
print(3 == 3)
print(3 is 3)#object method, but 3 is immutable so same object referenced
print([] == [])#True - same truthy value (coerced to boolean for comparison)
print([] is [])#False - different memory addresses
print("o" in "bobble")#membership operator
print("john" in {"name": "john"})#False: 
# membership operator in dicts compares KEYS

print("\n# LOGICAL")
print(True and bool(0))#==>>
print(True and False)
print(bool([]) or bool("Hello"))#==>>
print(False or True)
# NOTE: when OBJECTS are used in and/or expressions
# results are VERY different!
