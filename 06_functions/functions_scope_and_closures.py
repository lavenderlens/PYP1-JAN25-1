'''
scope defines the visibility and lifespan of a variable
local scope:
-   declared within a function
-   visible only within the function or its blocks
-   lives and dies with the function execution
global scope:
-   declared outside of any functions
-   visible to all functions in the script
-   lives whilst the whole script is executing
-   pure functions: accept copies of data, 
-   ALWAYS return the same thing EVERY time, for given same input
-   impure functions: have global dependencies on OTHER functions/variables,
-   do not always return same result for same given input

'''
next_num = 1 # global

# impure function
# NOT idempotent
# has global dependency
def get_next_num():
    return next_num

print(get_next_num())
print(get_next_num())
next_num = 2
print(get_next_num())#output change for GIVEN input (nothing)
# we don't want STUFF suddenly doing DIFFERENT STUFF
# because OTHER STUFF changes

# pure function
# idempotent
# no global dependencies
# passes in a COPY of data
# not the binding or reference to it

def get_next_num_pure(next_num):# next_num is placeholder NOT global variable of same name
    return next_num

print(get_next_num_pure(next_num)) 
print(get_next_num_pure(next_num))
next_num = 3
print(get_next_num_pure(next_num))#output change for GIVEN input (parameter)
# on the face of it, the two functions appear to have the same usage behaviour
# BUT, the pure function will never change output for the given input (COPY of next_num)
# when we re-assign next_num global
# the INPUT for the pure function is also changed
# not so for the impure (nothing)
# pure functions are far easier to test
# they do not require mocking of dependencies

#  let's prove this!

# reset next_num
next_num = 1
def increment_next_num():
    # next_num = 100#fixed with a new LOCAL variable, not bound to global
    global next_num#fixed by binding to the global variable
    next_num = next_num + 1# UnboundLocalError: cannot access local variable 'next_num' where it is not associated with a value
    return next_num #global value and local return value are now in sync - bound
# print(result := increment_next_num())#101, with local variable initialised as 100
print(result := increment_next_num())#2, with global binding
print(next_num)#still 1
# would we want to do this? 
# probably NOT - many functions could access and mutate global state

# BUT this pattern, although somewhat of an ANTI-pattern, does do an intriguing thing:
increment_next_num()
increment_next_num()
increment_next_num()
print(next_num)#5
# the gloval variable maintains its state from one function call to the next!
# so a function (acting on a global variable) can be said to have memory of its own state!
# what would be useful is if we could capture that state WITHIN a function scope
# so we weren't relying on a global variable to store that state
# which could then be accessed and mutated by OTHER functions also
# answer is LEXICAL SCOPE

def increment_with_lexical_scope():
    next_num = 1001#this does NOT refernce the global of the same name
    # as it is initialised within the outer function
    # this variable is lexically-scoped
    # scope is LOCAL to the outer function
    # but EFFECTIVELY GLOBAL to a function that the outer function returns
    # define and return an INNER function 
    # (possible because functions are first-order objects: 
    # they can both be passed to other functions and returned from other functions)
    def get_next_num():
        # the nonlocal keyword binds the inner function scope to the lexical scope
        nonlocal next_num
        next_num += 1
        return next_num
    return get_next_num

# create a closure around the lexically-scoped variable
# by passing the inner function returned, to another reference
my_closure = increment_with_lexical_scope()

print(my_closure())#1002
print(my_closure())#1003
print(my_closure())#1004

# want to reset? make a new closure
my_closure = increment_with_lexical_scope()

print(my_closure())#1002
print(my_closure())#1003
print(my_closure())#1004
