# Built-in data types
# In this exercise you will create a script comprising airline passenger information. You
# must choose the most appropriate data type for each item of data. In practice, it is
# unlikely that you will hard-code data into a script in this manner, but the purpose of the
# exercise is to make you familiar with the built-in data types at your disposal. Don't forget
# about Python's naming conventions.
# 1. Create a script named ch3_data_types.py.
# 2. Declare and assign one variable for each of the items of data tabled below.

# Description             Value
# ID                      1234
# First name              John
# Last name               Doe
# Checked bags            False
# Visited countries       Latvia, Guyana, Yemen, Uzbekistan
# Flight                  LGW to CDG
# Flight time             1 hour 15 minutes

# 3. Print each variable and its data type to the console.

id = 1234
first_name = "John"
last_name = "Doe"
checked_bags = False
visited_countries = ["Latvia", "Guyana", "Yemen", "Uzbekistan"]#mutable
visited_countries.append("Ireland")
visited_countries[0] = "Estonia"
print(visited_countries)

visited_countries_as_set = {"Latvia", "Guyana", "Yemen", "Yemen","Uzbekistan", "Latvia"}
print(visited_countries_as_set)#{'Yemen', 'Latvia', 'Uzbekistan', 'Guyana'}

flight= {"departure":"LGW", "arrival": "CDG"}
flight_time = {"hours": 1, "mins":15}
# flight_time = 1.25#not as good

print("id", id)
print(f"id: {  id  }")#whitespace INSIDE placeholder braces is consumed
print(f"First Name: { first_name }")
print(f"Last Name: { last_name }")
print(f"Checked bags: { checked_bags }")
print(f"Visited Countries: { visited_countries }")
print(f"Visited Countries as set: { visited_countries }")
print(f"Flight: { flight }")
print(f"Flight Time (hours): { flight_time }")

