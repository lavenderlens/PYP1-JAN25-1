# Python is dynamically-typed
# this means that datatypes can change during an application
# this type coercion or conversion happens implicitly in Python
# but may be called explicitly as well, on purpose
# each data type has its wrapper function of the same name

# conversion to boolean (bool)
# every datatype has its truthy and falsey values (convert to True or False)
# easier to remember the Falsey values - most values are truthy
# falsey values:
# Zero numbers 0 and 0.0
# empty collections/containers
# including str which is a collection or container (of single characters)
# note empty collections in JS, by contrast, are truthy!
# None

print("using bool() wrapper")
# numbers
print(bool(1))#True
print(bool(99))#True
print(bool(-99))#True
print(bool(0))#False

# strings
print(bool("hello"))#True
print(bool("h"))#True
print(bool(" "))#True
print(bool(""))#False

# containers
print("list:")
print(bool([1,2,3]))#True
print(bool([]))#False

print("tuple:")
print(bool((1,2,3)))#True
print(bool(()))#False

print("set:")
print(bool({1,2,3}))#True
print(bool({}))#False

print("dict:")
print(bool({1:1,2:2,3:3}))#True
print(bool(dict()))#False

print("coercion using int()")
print(int(True))#1
print(int(False))#0
print(int(1.0))#1
print(int(1.9))#1 not rounded but truncated (cut off)

print("coercion using str() wrapper")
print(str(True))#True
print(str(False))#False
# note that, once converted, the boolean values are both true
print(bool(str(True)))#True
print(bool(str(False)))#True
print(str(123))#"123"
print(type(str(123)))#<class 'str'>
