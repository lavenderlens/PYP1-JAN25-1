from calculator_procedural import add, sub, mul, div, equals, total
################################################
# ::LENO11 version NOT COMPLETED IN CLASS
################################################

add(5)
sub(2)
mul(3)
div(9)
print(equals())#expected 1.0
print(total)#expected 0 - ALWAYS, as it is the total from the module, initial value

# import calculator_oo_module
# calculator = calculator_oo_module.Calculator()
# bit cumbersome

from calculator_oo import Calculator
calculator = Calculator()
# now all our functions are props of the Calculator object
# we just need to call them through the reference variable
calculator.add(5)
calculator.sub(2)
calculator.mul(3)
calculator.div(9)
print(total := calculator.equals())#expected 1.0