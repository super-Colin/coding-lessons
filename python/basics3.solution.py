
# The FizzBuzz challenge
    # Create a function that will print out a series of numbers of an rangenum length
    # If the number is divisible by 3, print Fizz instead of the number
    # If the number is divisible by 5, print Buzz instead of the number
    # If the number is divisible by 3 and 5 both, print FizzBuzz instead of the number



# This was my solution, it took me a little bit longer than I thought it would
# and it could definitely be done better, but it works and that's what matters most


def fizzBuzzFor(input):

    for x in range(input + 1): # I had to research to find the range function
        print(x)
        if x % 15 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)



# It could also be done the same way but using a while loop instead of a for loop

def fizzBuzzWhile(input):
    x = 1
    while x <= input:

        if x % 15 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)

        x += 1 # Don't forget to increment your counter or bad things will happen
    

# fizzBuzzFor(20)
fizzBuzzWhile(20)