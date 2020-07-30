

# Don't worry if you don't understand a few of the things being used for now, we'll get to them,
# Or do some research yourself.. you might learn more
    # (maybe google "python concatenate" [..also, w3schools.com is a really good resource...])


# ---------------------------------------------------------
print('---')
print('example 1:')
print('')

# Variables
    # Variables are used to store information for later re-use
    # You can give them basically any name that will help label the represented data
        # Although they generally need to be one word, but can be connected by -'s and _'s


# In python variables don't need to be defined by a keyword



varName = "varValue" # Python also doesn't require semicolons at the end of every line
print('varName is equal to :::' + varName + ':::')

    # Where in JS we defined a variable by using the var keyword:
        # var varName = 'varValue';
print('')



# Variables can be reassigned 
print('The same variable reassigned:')
varName = "New var value"
print('varName is equal to :::' + varName + ':::')

print('---')
# ---------------------------------------------------------
print('===')
print('example 2:')
print('')

# Data Types
    # There are a lot of data types, but for now we'll just focus on 2
        # Integers or int's
        # And Strings or... strings..




# We'll define a string
myString = "This is a string"
print('var myString is equal to :::' + myString + ':::')

    # anything wrapped in qoutes will be registered as a string
myNotInt = '32145'
alsoNotInt="45135"


print('')

# We'll define an int
myInt = 35413

# but since it's an int if we tried to add it to a string it would take it literally:
# print('var myInt is equal to :::' + myInt + ':::')
    # and it would throw an error, 
    # your welcome to "un-comment" it by deleting the pound sign, saving, and re-running it


    # So in order to print out our int variables we need to make them into string type objects
myIntAsString = str(myInt)
print('var myIntAsString is equal to :::' + myIntAsString + ':::')

    # We can also do this inline without creating a new variable

print('var myInt is equal to :::' + str(myInt) + ':::')


# Just remember that functions expect certain data types as input, and can break otherwise

print('===')
# ---------------------------------------------------------
print('___')
print('example 3:')
print('')

# Functions
    # A function is basically a re-usable set of instructions to perform
    # It's useful to define a function when you'll need to do the same thing multiple times
    # (Although you can run code inline without defining functions)
    # (Sometimes a one use function can make your code a lot more understandable later though)

    # ALL programming is basically functions on functions inside functions



# To define a function in Python

def myFunction():
    print('Hello World!')


# To make that function run or to "call it" / "invoke it"
myFunction()
print('')
    # The parenthesis are basically the go button on your functions
        # They are also how we pass parameters for it to operate with

# Indentation
    # Python requires indentation as part of it's syntax
    # If something is indented in Python you can know that it is nested in something else


# Arguments
    # Arguments are the inputs for a function
    # They allow the same function to operate with different values

def myInputFunction(someInput):
    print(someInput)

myInputFunction('The input into our function')
print('')

    # We can also pass in variables
myInputVar = 'we\'ll pass this into the function'
        # to use a qoute mark inside of qoutes we can "escape" it with a backslash
            # (backslashes sometimes need to be escaped as well)
myInputFunction(myInputVar)

print('___')
# ---------------------------------------------------------
print('###')
print('example 4:')
print('')

# Conditionals
    # Conditionals let your program decide whether it should execute a block of code or not
    # They will always require some sort of input to gauge whether it is "truthy"

    # Booleans
        # True or False....
        # bool(1) / (0)

if True:
    print('of course True is True..')

print('')


    # Operators:
        # Equals: a == b
        # Not Equals: a != b
        # Less than: a < b

        # Less than or equal to: a <= b
        # Greater than: a > b
        # Greater than or equal to: a >= b

if 10 > 3 :
    print('10 is > 3 which is "truthy"')

print('')


print('Well Done! :)')
print('###')

# The homework for this lesson is to install python, and maybe even run this file
