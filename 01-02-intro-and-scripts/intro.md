# Introduction to the Python language

## Introduction and History

Python: not named after snakes, but after Monty Python TV show.

Guido van Rossum, Python's creator was a huge Monty Python fan. There are still obscure references to Monty Python humour in the official docs.

Object-oriented, high-level* language, arguably easier to learn than Java,

*high-level languages are declarative rather than imperative - one word may call several actions.

OO languages:
Favour data encapsulation in object structures (for PYTHON, THE DICTIONARY STRUCTURE IS AKIN TO A LITERAL OBJECT IN OTHER LANGAUGES)

JS: object literal:
{ name: "Alan",
age: 59}
JSON:
{ "name": "Alan",
"age": 59}
PY: dictionary:
{ name: "Alan",
age: 59}

objects: key: value pairs, comma separated, enclosed in curly braces{}

But that is the syntax definition. Why do we use objects? Because they wrap state (variables) and behaviour (functions) in one data structure. 

Objects are mutable (can be changed in an app) by default. 

as a complement to OOP (Object Oriented Programming) is

## Functional Programming, or FP

Immutable data structures preferred, that cannot change in the same way mutable objects can.

Think of OOP as "Save" - saves in place

Think of FP as "Save As" - saves a new copy with changes made.

Neither OOP NOR FP are exclusive! They play nicely together in most production apps.

## Python versioning

Python was re-written between versions 2 and 3. Strangely for a language, this was a BREAKING CHANGE. Code written in 3 > will not run on the 2 interpreter.

Most of what we do hasn't changed much since 3.5. But best to install latest version from python.org/downloads

Once installed, run two ways: -

1. as REPL shell (Read, Evaluate, Print, Loop) - one line at a time, always useful as you code larger scripts to check syntax -

2. script mode: write in an editor, save with the .py file extension, run in editor or from command line.

## Implementations

A Python implementation is not something we should concern ourselves with as it is to do with the underlying language.

Python code, using the standard implementation of CPython (underlying language is C) is interpreted - ie there is NO separate compile-time stage to check for syntax errors (that the code we write WILL NOT work at runtime). No performance optimisation at low-level machine code, but the IDE can still help us with suggestions (that the code we write MIGHT NOT work at runtime).

## Editors

PyCharm, Spyder, Idle (after Eric Idle), used to ship with Python install, Visual Studio (paid Microsoft.net environment), Visual Studio Code (Open Source), IntelliJ IDEA, Webstorm, Eclipse, Sublime, Atom.

We use Visual Studio Code as it is fully-featured and open source.

## Documentation

The Python official docs are intended for those who already have a level of proficiency in coding, and can be quite hard to read as a beginner. They are excellent for those for whom Python is not their first language.

Fortunately there are several alternatives. W3Schools.com is excellent for learning across many languages, and GeeksForGeeks.org is excellent for looking things up as you go. GFG is curated, individual contributions, and also does many different languages. More detail than W3Schools, but less in depth than Python docs.

If you want to search for, say the print() function, try combining it in your search string with the source eg
"geeksforgeeks python print()"
"W3 python print()"

## Naming conventions

Variables and functions should be named snake_case.

Classes should be named in PascalCase (CamelCase).

So if you EVER see a capital letter in Python, there should be a class definition associated with that.

Python does not support constants as such (variable that may not be reassigned) but should indicate that the data should not be changed by writing them in SCREAMING_SNAKE_CASE.

Comments should be whole sentences, sentence case, and terminated with a full stop and two spaces. delineated with a hash character at the start of each comment line:

#Yes, the spec is that fussy.

'''
Triple-quoted comments have a special use case inside functions,
but may be used also for multi-line comments
which only need quotes at the beginning and end of the whole block
'''

All these are BEST PRACTICE, and flouting them doesn't mean your code won't run, it's just best to stick to them for readability.

All these things are not manadatory, but to ignore them is to code in a non-Pythonesque way.

## Indenting and line-splitting

Indents are fundamental to Python and denote code blocks (LOC belonging to a particluar statement).

Each statement in Python is terninated by the new line character.

Multiple statements MAY be written on one line and semi-colon separated, but SHOULD NOT - not typical.

e.g. num1 = 1; num2 = 2

splits should happen if line length exceeds 79 characters or before

Note GDS (U.K. Goverment Digital Service) recommends a line length of 120

3 ways:

technology_without_an_interesting_name = "TWAIN"
technology_without_an_interesting_name /
= "TWAIN"
{technology_without_an_interesting_name
= "TWAIN"}
(technology_without_an_interesting_name
= "TWAIN") # probably most readable, see also Walrus operator for variation on this that returns as well as assigns
