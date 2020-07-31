

# ---------------------------------------------------------
print('---')
print('Example 1: While Loop\n')
# When printing a string you can use \n for a "_n_ew line"

# Loops
    # Loops allows us to create a set of instructions to be repeated over and over
    # Usually until a certain condition is met.

    # A While Loop repeats itself *while* something is true, until it's not,
        # Be careful with these and be sure they will exit at some point

i = 0 # i for index here
while i <= 4:
    print('while loop ' + str(i))
    i += 1 # Don't forget to increment your counter or bad things will happen


# Variable Scope
    # Variables can be grouped into "scopes" that define where they can be accessed from
    # If a variable is declared inside a function it's "scope" is limited to that function
    # If you'll need to use a variable in multiple places, you can declare it at a global scope
    # Variables at the global scale can be accessed in a function


def someFunc():
    newVar = 42 # newVar will have no meaning outside of this function ('s context)

print('---')
# ---------------------------------------------------------
print('===')
print('Example 2: Nested Loops\n')

# Nested Loops
    # A loop inside of another loop is refered to as "nested"

# we'll re-use "i" as our variable name, but we can't forget to reset it's value

        # And as I learned while making this lesson, Python will not let a function change a global var without declaring it inside the function as well
i = 0
def nestedWhiles(innerLoops):
    global i # allowing access to the global var i
    while i < 3:
        print('- outer loop i is at ' + str(i) + ' -')
        x = 0
        while x < innerLoops:
            print('nested loop x is at ' + str(x))
            x +=1     
        i += 1
# x as a var no longer exists!

nestedWhiles(3)


print('===')
# ---------------------------------------------------------
# https://www.w3schools.com/python/python_lists.asp
print('~~~')
print('Example 3: Arrays\n')

# Another Data Type: Lists 
    # "A List is a collection which is ordered and changeable."

    # A list is a collection of comma-separated values, usually related that are all part of the same object
        # Python has a few variations of arrays, but we're talking specifically about "lists"

    # To define a new list, wrap your values in brackets and put commas between them

ourList = ["First Item", 2, "Three", 45, 6, "Last Item"]

print(ourList)

# To use a single value out of our array we need to pass in an index number in brackets
    # Python (as with most languages) refers to the first item as index 0
print(ourList[0])

# Python also allows you to use a negative number to begin from the end
print(ourList[-1])


print('~~~')
# ---------------------------------------------------------
# https://www.w3schools.com/python/python_for_loops.asp
print('___')
print('Example 4: For Loop\n')


# A For Loop will repeat itself as many time as it needs to "for" each item in an array

aNewList = ['One', 2, "three", 4, "FIVE"]
for thing in aNewList:
    print('thing in array: ' + str(thing)) 
        # we wrap "thing" in the toString function here incase it's not a string











print('___')
# ---------------------------------------------------------



# ! ! ! HOMEWORK ! ! ! 

# Write a while loop nested in a for loop

    # The while loop should print out the value of the item the for loop is on 3 times
        # *For* bonus points nest another loop in there that counts to 3 between each For value


# Desired Output:

    # First Item
    # First Item
    # First Item
    # Second Item
    # Second Item
    # Second Item
    # Third Item
    # Third Item
    # Third Item


# Bonus Output:

    # First Item
    # 1
    # 2
    # 3
    # First Item
    # 1
    # 2
    # 3
    # First Item
    # 1
    # 2
    # 3
    # Second Item
    # 1
    # 2
    # 3
    # Second Item
    # 1
    # 2
    # 3
    # Second Item
    # 1
    # 2
    # 3
    # Third Item
    # 1
    # 2
    # 3
    # Third Item
    # 1
    # 2
    # 3
    # Third Item
    # 1
    # 2
    # 3