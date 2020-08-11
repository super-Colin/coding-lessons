
# ---------------------------------------------------------
# https://www.w3schools.com/python/gloss_python_function_arguments.asp
print('---')
print('Example 1: Function Arguments\n')

# When defining a function you can also define parameters that the function expects

def printInput(inputParameter):
    # The defined parameters become the name of a local variable in the function
    print(inputParameter) # Will print out whatever you put in

# To be able to pass in multiple seperate parameters, seperate them with commas
def printTwoInputs(param1, anotherParam, abother, banana):
    print(param1)
    print(anotherParam)

def printMoreInputs(argument1, someNameVar, couldBeArray):
        # using str() command to make sure input is a string
    print(str(argument1))
    print(str(someNameVar))
    print(str(couldBeArray))

# Notice that this function is being invoked at a global level,
    # The print command is also INSIDE the function

    # *** The other functions are not being called so are not actually printing anything ***
printMoreInputs(42, ["A", "List"], "Third argument") # Where print is actually used

# While the above can take information in and manipulate it,
    # There is currently no way to access the information after it's manipulated

print('---')
# ---------------------------------------------------------
# https://www.w3schools.com/python/ref_keyword_return.asp
print('===')
print('Example 2: Function Returns\n')



# To access the values after they've been manipulated, we need to "return" them
    # To return a value we just need to use the "return" keyword

def returnFourFunction():
    # There is no print command in this function
    return 2 + 2 # Only the return statement

# We can call the function but nothing is there to take the returned value
returnFourFunction()

# If we pass it as an argument to print(), print will recive the "return"ed value
print( returnFourFunction() )

print('returnFourFunction is returning: ' + str(returnFourFunction()) + ' to the print() command')
    # It may help to think of a function in this case as simply it's returned value

# The return keyword also ends the execution of a function
def wontPrint():
    print("You WILL see this printed in the console, but..")
    return # just using return to end the function
    print("You won't see this printed in the console")

wontPrint()

print('===')
# ---------------------------------------------------------
# https://www.w3schools.com/python/python_conditions.asp
print('___')
print('Example 3: More Conditionals\n')

# Truthy is basically anything that isn't 0 or null or undefined(which will throw error) 
    # chalkboard for more info

# If you need more fine grain control than a single if statement you can add another if using "elif"(else if)
        # you can add as many elif statements as you need
        
if 2 > 7:
    print('2 > 7 is truthy.?..?')

elif 3 > 7:
    print('3 > 7 is truthy.?..?')

elif 5 > 7:
    print('5 > 7 is truthy.?..?')
    
elif 7 > 2:
    print('elif fired because 7 > 2 is "truthy"')


    # The if statement also has an else clause that can be use to catch anything not "truthy" by any above if statement

if 15 > 17:
    print('15 > 17 is truthy')
else:
    print('15 > 17 is NOT truthy, so else was fired')

print('\n')

    # We can also use expressions, variables and even functions in our conditional statement

def condFunction():
    return 22 # So we can think of this function as simply the returned value of 22

condVar = 10

if condFunction() > condVar:
    # print('\nfunction inside conditional: ')
    print("condFunction = " + str(condFunction()) + ", while condVar = " + str(condVar))
    print("So " + str(condFunction()) + " > " + str(condVar)  + " is truthy")


print('___')
# ---------------------------------------------------------
# https://www.w3schools.com/python/python_operators.asp
print('###')
print('Example 4: Handy Operators\n')


print('> Equal To "==" <')
# Equal to or "==" checks if 2 things are equal

if 2 == 2:
    print('2 == 2 is truthy, so if fires')
else:
    print('2 == 2 is not truthy') # won't print

# The equal to operator can also be used on strings

if "Hello" == "World":
    print('Hello == World') # won't print

elif "Hello World" == "Hello World":
    print('Hello World == Hello World')



print('\n> Not Equal "!=" <')
# Not equal or "!=" comparison operator is the opposite of the equal to "comparison operator"
    # It checks that 2 things are NOT equal, sort of like a mini else

if 2 != 2:
    print('2 != 2')
else:
    print('2 != 2 is not truthy, so else fires') # won't print

if "Hello World" != "Hello World":
    print('Hello World != Hello World') # won't print

elif "Hello" != "World":
    print('Hello != World is truthy')



print('\n> Modulus "%" <')

# Modulus
    # The modulus operator performs a division operation and returns the remainder
        # This is a lot more useful than it sounds at first


    # Modulus can be used to see if a number is odd or even easily
def isNumEven(num):
    print(str(num) + " % 2 = " + str(num % 2) )

    if num % 2 == 0: # think that 10 % 2 = 0 (so modulus returns 0)
        print("So " + str(num) +  " is Even")
        # We return True if the number is even, incase we want to use it somewhere else
        return True
    else:
        print(str(num) + " isn't even, so " + str(num) + " must be Odd")
        # And we can return False if the number is not even
        return False



isNumEven(2)
print('-')
isNumEven(3)
print('-')
isNumEven(487)







# ! ! ! HOMEWORK ! ! ! 
#  https://www.w3schools.com/python/ref_func_range.asp  <<< may be helpful

# The FizzBuzz challenge
    # Create a function that will print out a series of numbers of a given range
    # If the number is divisible by 3, print Fizz instead of the number
    # If the number is divisible by 5, print Buzz instead of the number
    # If the number is divisible by 3 and 5 both, print FizzBuzz instead of the number

        # For extra credit make it accept an argument for what number it should start at


# Desired Output:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz