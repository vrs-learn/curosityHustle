# This is the second Notes for the Python and Flask Bootcamp.
# This file will contain more python codes thats readable and understandable.
#
#
#
# Classes , methods and objects..
#
# Below is how to declare class.
# A class can have its own attributes and methods.

class Dog():

    # Class Object Attributes
    species = 'mammal'  

    def __init__(self,breed,name):  # This is the initializer method which is invoked everytime an object of the class is created.
        self.breed = breed          # This is an attribute which is created as part of the object.
        self.name = name


sam = Dog('Lab','Frankie')          # sam is an object of the class Dog. As soon this statement is executed, the initializer method of the class is also executed.

########################
# Creating a class with its own methods.
########################

class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):                 # A new function created for the class Circle.
        return self.radius**2 * self.pi     

mycircle = Circle(10)
print(mycircle.area())              # Calling the area function of the class Circle. This prints the area of the circle.

########################
# Creating class that inherits another class.
# With inheritance, we also inherit all the methods of the inherited class.
#
#
# Below is example of an individual class and then another class that inherits the previous class
########################

class Animal():

    def __init__(self,fur):
        print('Animal Created')
        self.fur = fur
    
    def eat(self):
        print('Eating !!')
    
    def report(self):
        print('Animal')

class Dog(Animal):          # Animal class is inherited. With this, all the methods of the Animal class are also inherited.

    def __init__(self,fur):
        Animal.__init__(self,fur)   # Animal initializer method is called.
        print('Dog Created')
    
    def report(self):        # Note we are using a method of the same name as in the Animal class. But this method will overwrite the Animal class when object of the Dog class is created.
        print('I am a dog.')


d = Dog('Fuzzy')
d.eat()          # Note. This method is not created as part of the Dog class. But since Animal class in inherited in the Dog class, the methods of Animal class are also inherited.
d.report()       # Note we are using a method of the same name as in the Animal class. But in this scenario the report method of Dog class will be called as it overwrites the Animal class.
print(d.fur)


#######################
#
# Python classes also have in built functions that can be used and modified as desired.
# This section will take a look at some of those.
#
#######################

#
# Adding a representation method in a class.
#

class Book():

    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self):                         # This is a represntation method. This allows use to modify the default behaviour whenever one wants to check about the Book object.
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self):                      # This method is used to overwrite the inbuilt len() function. We can now call a len function on object of Book class.
        return self.pages


mybook = Book("Python Rocks!!", "Jose", 250)
print(mybook)           # Notice how this message is different from the usual message. This prints the message which the Class object returns from __repr__ method.
print(len(mybook))      # Notice how the __len__ method is used to return the len() method call for the mybook object.


#####################################
### D E C O R A T O R - S T A R T ###
#####################################
#
# Decorators 
# Python has decorators that allow you to tack on extra funtionality to an already existing function.
# They use @ operator and are then placed on top of the original function.
#
# Functions within functions.
# Returning Functions.
# Passing functions as argument.
#

def new_decorator(func):

    def wrap_func():
        print("some code before executing func()")

        func()

        print("Code here, after executing func()")
    
    return wrap_func


def func_needs_decorator():
    print("Please decorate me !!")


func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

##########################
# Above code can be replaced by same as below.
# and this is what decorator is all about.
###########################

def new_decorator(func):

    def wrap_func():
        print("some code before executing func()")

        func()

        print("Code here, after executing func()")
    
    return wrap_func

@new_decorator                  # This line replaces the -> func_needs_decorator = new_decorator(func_needs_decorator) . This is also called as decorator.
def func_needs_decorator():
    print("Please decorate me !!")


func_needs_decorator()


#################################
### D E C O R A T O R - E N D ###
#################################

#
# PyPI is a repository for open-source third-party Python packages.
# Its similar to RubyGems in the Ruby world, PHP's packagist, CPAN for Perl and NPN form Node.js
#
# We will use "pip install" to install packages.
#
# Python packages can be created by creating a __init__.py file inside the directory where the script is placed.
#