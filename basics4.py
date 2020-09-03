
# ---------------------------------------------------------
# https://en.wikipedia.org/wiki/Object-oriented_programming
print('OBJECT ORIENTED PROGRAMMING')
print('---')

# https://www.w3schools.com/python/python_classes.asp
print('Example 1: Classes\n')


# This is a "Class", it is a blueprint for building "Objects"
class NumberCounterObject:

    # Evrything inside this class will become the created "Object"'s properties

        # Almost all classes will have the __init__ property,
            # It will set other properties with values passed into it upon creation of a new object

    def __init__(self, startingNumber, countByNumber):
        self.currentNumber = startingNumber # Here we are creating and assigning a variable property
        self.countByNumber = countByNumber


    # We can define functions as properties, which can then be referred to as "methods"
    def getNumber(self):
        return self.currentNumber

    def incrementNumber(self): 
        self.currentNumber += self.countByNumber 
        return self.currentNumber

# Create an actual object based on our blueprint above
countsBy2 = NumberCounterObject(0, 2)

print(countsBy2.getNumber()) # Get the number just to show it's at 0
print(countsBy2.incrementNumber())
print('Count by 2 a few times')
print(countsBy2.incrementNumber())
print(countsBy2.incrementNumber())


print('---')


# https://www.w3schools.com/python/python_classes.asp
print('Example 2: Objects\n')

# Python is an object oriented programming language.
    # As such almost everything in Python is an object

        # String, Int, Boolean, etc.. are all object types,
            # Any variable that stores a string will become a String object,
            # as such it will have access to all the functions of the global String object


# An object in programming at it's most basic is a list of properties.
    # These properties can contain functions or information the object has access to


# To create an object we first need to define a "Class"
    # A Class is like a blueprint for creating objects.

# To create a "Class", use the keyword "class":

class aNewClass:
    # Here we are giving our class a "property" that will be set on all object of this class
    varInNewClass = 'A preset property of an object'

# Even without an init property we still need to invoke() the class function to make a new object
objectOfNewClass = aNewClass(); 

# To access a property of an object we add a "." to the end of the object and then the property to access
objectProperty = objectOfNewClass.varInNewClass

print("Property assigned to var =" + objectProperty)
print("Direct accessed property =" + objectOfNewClass.varInNewClass)


print('---')
# https://www.w3schools.com/python/gloss_python_class_init.asp
print('Example 3: __init__ Property\n')

# All classes have a built in function called __init__()
# __init__ is always executed when a class is being initiated, although it can be empty


class classWithInit:
    
    def __init__(self, aValueWeWant, aStringWeWant): # We give init a series of values we want to use to set other properties
        self.aNewValue = aValueWeWant
        self.aNewString = aStringWeWant

        # The name of the property will be the self.<propName>, not the argument name 
        self.propWithCombinedValues = [aValueWeWant, aStringWeWant]
    

# Init is useful because we can create multiple objects of the same class with different values in them
    # Objects holding their own values is called "encapsulation"
weWant3andSomthing = classWithInit(3, "somthing")
iNeed17andNothing = classWithInit(17, "Nothing")

print("weWant3andSomthing newValue =" + str(weWant3andSomthing.aNewValue))
print("weWant3andSomthing newString =" + weWant3andSomthing.aNewString)
print('')
print("iNeed17andNothing newValue =" + str(iNeed17andNothing.aNewValue))
print("iNeed17andNothing newString =" + iNeed17andNothing.aNewString)



print('---')
# https://www.w3schools.com/python/gloss_python_class_init.asp
print('Example 4: Self\n')

# When we define a class we pass the "self" keyword as the first argument to all functions
    # "self" refers to the object that is calling the function at that moment

class classAboutSelf:

    def __init__(self, inputVal1, inputVal2):

        self.prop = inputVal1 
        # Here we're saying the object calling this init function,
            # The new object being created; or init'd, 
            # Should create a property called "prop1" and set it to the value passed in as "inputVal1"


    # Self helps us access an individual object's "encapsulated" properties
    def getSelfProp(self):
        return self.prop

    # Self can be called something else if you wish but it will always be the first argument
        # "this" is a similar keyword in some languages
    # def getThisProp(this):
    #     return this.prop

    # Since self is always the first argument, 
        # If we want to pass arguments to the method call they will be the second, third and so on
        # Self will be automatically input by the object, so the method call here will only expect 3 arguments
    def printSelfValPlusInput(self, methodNumInput, anotherMethodInput, asManyAsYouNeed): 
        
        print('self.inputVal1 + methodNumInput = ' + str(self.prop + methodNumInput))


objectAboutSelf = classAboutSelf( 1, "input value 2")

print('getSelfProp =' + str(objectAboutSelf.getSelfProp()) ) # Don't forget to invoke your object's methods
# print('getThisProp =' + str(objectAboutSelf.getThisProp()) )

objectAboutSelf.printSelfValPlusInput(3, 'anotherMethodInput (not used)', 'asManyAsYouNeed (unused)')

# ! ! ! HOMEWORK ! ! ! 

# Define a class to create bank account objects

# The bank account object should:
    # Take an argument for an initial account balance
    # Have a property to keep track of it's balance
    # Have a method for getting the current balance (return the value)
    # Have methods for depositing and withdrawing (adding and subtracting to the balance)

# Desired:

# newAccount = bankAccountClass(1000)
# print( newAccount.getCurrentBalance() ) # Should return 1000
# newAccount.deposit(100)
# newAccount.withdraw(400)
# print( newAccount.getCurrentBalance() ) # Should return 700 if both worked