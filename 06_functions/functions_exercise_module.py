def get_greeting() -> str:
    return "G'Day"

def get_greeting(name: str) -> str:
    # return "G'Day " + name
    return f"G'Day {name}"#better- expressions are evaluated 
# and string representation returned
# no matter what the datatype is

def get_product(num1: float, num2: float) -> float:
    return num1 * num1

def get_first(lst):
    return lst[0]

def get_name(a_dict):
    return a_dict["name"]
# gets value assoc with key name

def get_circumference(radius):
    '''This is a docstring which all python production code should have.  
    It details function parameters, return types, and what the function does, in ordinary language.  
    It is picked up in interactive help by running help(function_name)
    It must be the first thing in a function body, triple-quoted
    (either double or single quotes but to auto-generate must be double)'''
    return 2 * 3.14 * radius

def print_first(a_list):
    """this function takes a list and returns the first element

    Args:
        a_list (list): a list
    """
    print(a_list[0])

def print_name(a_dict):
    print(a_dict["name"])

# def print_circumference(radius):
#     print(2 * 3.14 * radius)

    # take the above function
    # it takes a float as an arg
    # it returns None (because it has a print)
    # run auto docstring generator extension:

def print_circumference(radius):
    """takes a circle radius and calculates the area

    Args:
        radius (float): None
    """

    print(2 * 3.14 * radius)

