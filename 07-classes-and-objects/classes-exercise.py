# Objects and Classes
# In this exercise you will create a class to model a Training Course object. 

# Use TrainingCourse naming style NOT training_course!

# The class will contain both data and method attributes. 
# The data attributes will consist of 
# a course title,
# a duration ( in days - just a number, int, will do), 
# a course daily rate price (another number, float) and 
# a list of delegate names. 

# The Training Course
# object will also require methods: 
# a method to add a name to the delegate list and 
# a method to display the total revenue generated for the Training Course object.
# hint: the number of delegates will be returned by the built-in len() function

# 1. Create a script called classes_exercise.py.
# 2. Create a class called TrainingCourse
# 3. Add a dunder __init__ method to ensure that a TrainingCourse object is created
# with the following data attributes: title, duration, pricePerPersonPerDay and an empty list
# called delegates.
# 4. Add a method called add_delegates that will accept a delegate name as a parameter
# and then append it to the delegates list i.e. self.delegates.append(name).
# 5. Add method called get_total_revenue which will return the total revenue generated for
# the Training Course object i.e. number of delegates * pricePerPersonPerDay.

# TEST YOUR Classes
# 6. Create a TrainingCourse object with the data attributes set to the following values:
# title: Python Programming 1
# duration: 4
# price per person per day: 500
# delegates: [ ]
# 7. Use the addDelegate method to assign some names to the Training Course
# object’s delegates list.
# 8. Display to the console the total revenue generated for the TrainingCourse object.

# time permitting, move your procedural testing code to a separate script and import TrainingCourse from a module
# NOTE: in order for this eaxmple to work you DO NOT need to implement __str__
# NOTE: the code you will write should take up less lines than this spec!

class TrainingCourse:
    def __init__(self, title, duration, price_per_person):
        self.title = title
        self.duration = duration
        self.price_per_person = price_per_person
        self.delegates = []

    def add_delegates(self, delegate_name: str) -> None:
        self.delegates.append(delegate_name)

    def get_total_revenue(self) -> float:
        return self.price_per_person * len(self.delegates)

if __name__ == "__main__":
    python1 = TrainingCourse("Python 1", 4, 2_000)
    python1.add_delegates("Akheela")
    python1.add_delegates("Edwin")
    python1.add_delegates("Euan")
    print(python1.get_total_revenue())#expected: 6000
    