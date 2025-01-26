class Calculator:

    # total = 0#our global state becomes the constructor in the class
    # for an object to have fileds, they MUST be declared inside the class constructor
    def __init__(self):
        self.total = 0

    def add(self, num):#add parameter self
        # global total#get rid of global binding
        self.total += num#reference self
    def sub(self, num):
        self.total -= num
    def mul(self, num):
        if self.total != 0:
            self.total *= num #long hand is total = total * num
    def div(self, num):
        if self.total != 0:
            self.total /= num

    def equals(self):
        return_value = self.total
        self.total = 0
        return return_value

if __name__ == "__main__":
    # we can test our OO code here
    # and it will not run if funcs imported elsewhere
    calculator = Calculator()
    # now all our functions are props of the Calculator object
    # we just need to call them through the reference variable
    calculator.add(5)
    calculator.sub(2)
    calculator.mul(3)
    calculator.div(9)
    print(result := calculator.equals())#expected 1.0
