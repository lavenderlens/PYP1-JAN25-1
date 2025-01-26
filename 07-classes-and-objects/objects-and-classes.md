## Objects and Classes

### Introduction

Python is an object-oriented language.

You don't have to code in an OO way (most Python devs don't!).

Procedural programming: code that focuses on variables and functions

OO programming: code that focuses on objects (and their internal variables and functions)

**Procedural script**

    variables
    functions

**OO script**

    _______________
    object1
    |variables    |
    |functions    |
    _______________

    _______________
    object2
    |variables    |
    |functions    |
    _______________

Object: group of related data and functions


data: state

functions: behaviour

generally, it only makes sense to include behaviour that affects one or more items of state

`Class`: a template/blueprint for creating objects in a uniform or consistent manner

The Dictionary structure in Python is the eqyuvalent of an object literal in JS

In Python objects different from dictionaries:

Object notation:

my_object.prop

Dictionary notation:

my_dictionary["prop_name"]

- In Python you cannot create objects without first defining a class

- A class defines what data and function attributes (state and behaviour) each object of the class has
- Note: these are often referred to as object properties or fields
- The idea of classes is NOT to enforce the same prop VALUES, but the same prop names.
- By convention, class names should be Pascal or CamelCase - no underscores (!) starts with capital letter

### differences between languages with respect to classes

In Java, for instance, the name of the class is used to initialise an instance of the class TOGETHER WITH the "new" keyword

    JAVA: var myClass1 = new MyClass()

    OR: MyClass myClass2 = new MyClass()

there exists, therefore, code that looks like

    class MyClass{
    ...some code
    }

In Python there is no "new" keyword.
In Python, the ONLY CLUE we have of the existence of an associated class is the capital letter.

    PYTHON: my_class = MyClass()


