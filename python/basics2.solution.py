

# Write a while loop nested in a for loop

    # The while loop should print out the value of the item the for loop is on 3 times
        # *For* bonus points nest another loop in there that counts to 3 between each for value



myList = ["First Item", "Second Item", "Third Item"]

# BASIC

# for item in myList:
#     x = 0

#     while x < 3:
#         print(item)

#         x +=1






# BONUS

for item in myList:
    x = 1

    while x <= 3:
        print(item)
        innerX = 1
        

        while innerX <= 3:

            print(innerX)
            innerX += 1

        x +=1



# EXTRA

# for item in myList:
#     x = 1

#     while x <= 3:
#         print(item)
#         innerX = 1

#         while innerX <= 3:

#             if x != 3: # Don't count to three after the last time the value is printed
#                 print(innerX)

#             innerX += 1

#         x +=1
