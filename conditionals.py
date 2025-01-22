'''
conditional statements are very smilar in Python to other languages,
they execute a block of code depending on whether a condition evaluates True or False
if True:
    code block, defined by indent, immediately following is executed
if False:
    skipped

an else block has NO condition and means, really ANYTHING else

you can test multiple conditions using if elif else

following execution of a branch the interpreter steps out of the statement structure, like a break

so when using ranges of values, if..elif blocks should be arranged with care to avoid unreachable code

Since recently in Python 3.10 there is another decision control statement
Called Structural Pattern Matching or match case
This mimicks the behaviour of switch in Java and JS, which traditionally has had no equivalent in Python
The match statement tests a single variable or expression for equality

'''

# single branch IF
if True:
    pass#pass is a placeholder which means the code will run but nothing happens
if True:
    print("true path executed")

# two branch IF-ELSE
if False:
    print("true path executed")
else:
    print("else executed")

# two or more branches IF - ELIF - ELSE
if False:
    print("first IF path executed")
elif True:
    print("SECOND IF path executed")
else:
    print("else executed")

# Make comments at the level of indent that they refer to. 
# if-else on one line
# this is Python equivalent to Ternary Operator in other languages
temperature = "cold"
temperature = "scorchio"
clothing = "jumper" if temperature == "cold" else "T-shirt"
print(clothing)

# ranges
heart_rate = 150
bp = {"diastolic": 150, "systolic": 100}

if heart_rate < 130 and bp["diastolic"] < 100:
    print("healthy individual")
elif heart_rate < 150 and bp["diastolic"] < 120:
    print("You should ring your GP for a checkup")
else:
    print("You should go to A&E")
