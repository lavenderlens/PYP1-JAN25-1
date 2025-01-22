# Part 1 Conditionals
# In this exercise you will create a script that prompts the user to input his/her birth year,
# and then prints to the console the generation of which he/she is a member, e.g. Baby
# Boomer, Generation X, etc.
# 1. Create a script named conditionals_exercise.py.
# 2. Prompt the user to input his/her birth year and capture it in a variable named
# birth_year.
# 3. Convert birth_year to an int.
# 4. If the user was born between 1946 and 1965, print Baby Boomer to the console.
# 5. If the user was born between 1966 and 1976, print Generation X to the console.
# 6. If the user was born between 1977 and 1994, print Millennial to the console.
# 7. If the user was born in 1995 or beyond, print Generation Z to the console.

year = input("Enter the year you were born:")
year = int(year)

if year < 1946:
    print("too old to be categorised")
elif year >= 1946 and year <= 1965:
    print(f"Born in: {year}: Baby Boomer")
elif year >= 1966 and year <= 1976:
    print(f"Born in: {year}: Gen X")
elif year >= 1977 and year <= 1994:
    print(f"Born in: {year}: Millenial")
else:
    print(f"Born in: {year}: Gen Z")