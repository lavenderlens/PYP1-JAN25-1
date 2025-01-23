'''
a class is
a BLUEPRINT or TEMPLATE for
creating objects of a certain user-defined type
there exist many system classes such as string and list
when we create our own classes, however, we create our own types
you may choose classes over dictionaries to represent complex data
as every instance of the class will have 
the same fields (variables) and
the same methods (functions)
whereas if we used dictionaries, every usage has to be defined again
classes enforce standards applied by all objects of that class
'''

class Client:#note no params passed to class directly
    # pass
    # dunder method constructor
    # runs once, when the class is called Client()
    def __init__(self):#constructor
        # self refers to the current object under construction
        # ALL class methods MUST pass a reference to self
        #  we can use self to set attributes (props) on the object
        self.name = "Client name"
        self.email = "Client email"
        self.dependents = []
        # in order to get a meaningful string representation 
        # of the object's properties and values 
        # when the reference is passed to print
        # we override another dunder (double UNderscore) method, __str__
    def __str__(self):
            return f"""
Name: {self.name}, 
Email: {self.email}
dependents: {self.dependents}"""
        

client1 = Client()
print(client1)#<__main__.Client object at 0x100a0e900># the object, with no code in the class
print(client1)#with __str__ overridden in class
"""
Name: Client name, 
Email: Client email
dependents: []
"""
print(client1.__str__())#with __str__ called explicitly: no difference

client1.name = "Elon"
client1.email = "elon@salute.com"
client1.dependents = ["Grimes", "AEX11", "Donald"]

# NOTE dot notation for object props
# square brackets notation for dictionary keys

print(client1)

# what if we wished to pass in prop values at instantiation time (instance of the class)?

class Client2:
    def __init__(self, name, email, dependents):# parameterised variables - declared within parameters
        self.name = name#expression - parameter value, passed in and assigned R-L to the prop name
        self.email = email
        self.dependents = dependents
    def __str__(self):
            return f"""
Name: {self.name}, 
Email: {self.email}
dependents: {self.dependents}"""
    
client2 = Client2("Donald", "potus@gov.us", ["Ivanka", "Donald Jr.", "Elon"])
print(client2)

# encapsulating custom functions wihin a class

class Client3:
    def __init__(self, name, email, dependents):# parameterised variables - declared within parameters
        self.name = name#expression - parameter value, passed in and assigned R-L to the prop name
        self.email = email
        self.dependents = dependents

    # custom function:
    def add_dependent(self, name):
        # there is little or no point 
        # in writing custom setter methods for fields 
        # if we do not implement business logic
        if name not in self.dependents:# business logic says no duplicate names
            self.dependents.append(name)
    
    def __str__(self):
            return f"""
Name: {self.name}, 
Email: {self.email}
dependents: {self.dependents}"""
    
client3 = Client3("Vance", "jd@hillbillyelogy.com", ["Maw", "Paw"])
client3.add_dependent("Gramma")
print(client3)
client3.add_dependent("Gramma")
print(client3)