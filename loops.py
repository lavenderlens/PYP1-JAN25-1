'''
Loops come in two sorts: the while loop and the for loop
# while loops are commonly used for console IO
# there may be no obvious end to the process
# for loops are commonly used to iterate over containers
# the length of the container is known in advance
The for loop in Python is syntactic sugar for a while loop, 
usually when the number of iterations is known in advance.
There are no for loops at runtime, only while loops that the code is compiled into.
While loops in source code are useful when the number of iterations is not known in advance.

In Python, an optional else clause may be added to the end of both types of loop, for and while.
It is executed if the loop completes and doesn't hit a break statement.
In other words, if the loop completes normally.
To make this clearly readable, add a comment "# no break" next to the else clause.
'''
names = ['Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson']

print(len(names))#for loops are suited for collections, which have a length property
# therefore the number of iterations is known in advance

for name in names:
    print(name)

# list slicing and for loops

# a list slice returns a new list
# therefore it could be said to be a FP technique
# new list is picked from the original, spec with up to 3 args:
# [start_index_inclusive, end_index_exclusive, step]

print("list slicing 1 - two args")
for name in names[2:4]:
    print(name)
# we may also assign the result of a list slice
funkiest_ones = names[2:4]
print(funkiest_ones)#['Janet Jackson', 'James Brown'] - a new list

# 2nd arg exclusive has the effect that you may ask for an index which is not in the list
print(last_name_in_list := names[6:7])#reminder: walrus assigns and returns at once
print(last_name_in_list)# saved
# print(names[7])#IndexError: list index out of range

print("list slicing 2 three args including step")
print(odd_number_names := names[0:7:2])
print(odd_number_names := names[6:0:-3])#TODO get first Michael Jackson

print("list slicing 3 one arg for step only")
print(odd_numbers := names[::-1])

print("list slicing 3 one arg for startIdx - end")
print(odd_numbers := names[0:])
print(odd_numbers := names[1:])

# passing to a set to filter out duplicates in a list
names_as_set = {'Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson'}
names_as_set = set(names)
print(names_as_set)#{'Janet Jackson', 'David Hume', 'Gordon Brown', 'Michael Jackson', 'James Brown', 'David Bowie'}
names_as_set_again = {'Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson'}
print(names_as_set_again)#{'Michael Jackson', 'Janet Jackson', 'James Brown', 'David Hume', 'Gordon Brown', 'David Bowie'}
# but order is not guaranteed to be same from one run of the program to the next

# dictionaries and loops

names_as_dict = {
    "politicians": ["Gordon Brown", "David Hume"],
    "musicians": ["Michael Jackson", "James Brown", "Janet Jackson"],
}

# keys
for key in names_as_dict.keys():
    print(key)

# values
for value in names_as_dict.values():
    print(value)

# both keys AND values
for key, value in names_as_dict.items():
    print(key,value)

# using a range function to control No. of iterations
for i in range(1,11):
    print(i)

# optional else clause, break, continue

counter = 0
while counter < len(names):
    if names[counter] == "Janet Jackson":
        # break
        counter += 1#otherwise infinite loop
        continue
    print(names[counter])
    counter += 1
else:
    print("no more names to print")

# conditionals exercise refactored to a loop:

while True:
    year = input("Enter the year you were born, or zero(0) to quit:")
    year = int(year)

    if year == 0:
        break
    elif year < 1946:
        print("too old to be categorised")
    elif year >= 1946 and year <= 1965:
        print(f"Born in: {year}: Baby Boomer")
    elif year >= 1966 and year <= 1976:
        print(f"Born in: {year}: Gen X")
    elif year >= 1977 and year <= 1994:
        print(f"Born in: {year}: Millenial")
    else:
        print(f"Born in: {year}: Gen Z")