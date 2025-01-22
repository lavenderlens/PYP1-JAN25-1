# when both operands re booleans, & and |, technically binary operators, work like so:
truth = True
falsehood = False

print(truth & falsehood)#False
print(truth & (not falsehood))#True

print(truth | falsehood)#True
print(truth & (not falsehood))#True
print((not truth) | falsehood)#False
print((not truth) & (not falsehood))#False

# all the above may be achieved using the and and or operators 
# which is more common actually and best practice

print("using and + or")
print(truth and falsehood)#False
print(truth and (not falsehood))#True

print(truth or falsehood)#True
print(truth and (not falsehood))#True
print((not truth) or falsehood)#False
print((not truth) and (not falsehood))#False

# the and and the or are also short circuit operators
# when used with one or both operands as booleans
# they return booleans
# when used with one or more operands as objects
# they return OBJECTS, not boolean values
# in Python EVERYTHING is said to be an object, 
# so these rules do not differ for booleans either

print("x" or "")#'x'
print("" or [])#[]
print("x" and "")#'' (no output)
print("" and [])#'' (no output)

print("x" or "")#'x'
print("" or [])#[]
print("x" and 0)#0 
print(0 and [])#0

# substitute booleans for objects ONE side:
print("substituting a boolean for FIRST operand")
print(True or "")#True
print(False or [])#[]
print(True and 0)#0 
print(False and [])#False

# in Python EVERYTHING is said to be an object, 
# so these rules do not differ for booleans either

print("substituting a boolean for SECOND operand")
print("x" or False)#'x'
print("" or False)#False
print("x" and False)#False 
print(0 and [])#0

