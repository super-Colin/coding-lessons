try:
    open('./basics5_read.txt', 'x').write('Greetings from basics5_read.txt file :)')
except:
    pass
# ^The code above just creates a demo file and does nothing if it exists already^
print('\n--------------------------------------------------------')
# https://www.w3schools.com/python/python_file_handling.asp
print('Working With Files')
print('---\n')

    # The key function for working with files in Python is the open() function.

        # The open() function takes two parameters; filename, and mode.
        # There are 4 "modes" total, here for reference.

            # "r" - Read - Default value. Opens a file for reading, error if the file does not exist

            # "a" - Append - Opens a file for appending, creates the file if it does not exist

            # "w" - Write - Opens a file for writing, creates the file if it does not exist

            # "x" - Create - Creates the specified file, returns an error if the file exists


print('\n----------------------------')
# https://www.w3schools.com/python/python_file_open.asp
print('Example 1: Opening A File')
print('---\n')

# This script went ahead and made a small txt file for us to read
ourReadFile = open('./basics5_read.txt', 'r')# The "./" means in the current directory, 'r' is for Read
print('ourReadFile.read() = ' + ourReadFile.read()) # .read() returns the content so we run it in a print statement to see it


ourReadFile.close() # Always close the file when your done working with it!!!
# !!!! Not closing a file can become a "resource leak", that is very bad !!!!


# Let's make a function to print out the second line of a file and then close it so we don't forget to
def printFile(filePath):
    fileObject = open(filePath, 'r')
    print('\n_______\nPrinting file: ' + filePath + '---\n' + fileObject.readline() + '\n_______')
    fileObject.close()


printFile('./basics5_read.txt')


print('\n----------------------------')
# https://www.w3schools.com/python/python_file_remove.asp
print('Example 2: Creating And Deleting A File')
print('---\n')


# Let's start by deleting the file this script made for us
input('\nNotice the basics5_read.txt file that will be in the same folder and press enter') #just to pause the script

# To actually remove it from the computer we need to import the "os" module
import os   # Imports normally go at the top of a script, ( you must import before you can invoke() )
                # This is only here to make you aware of it

os.remove('basics5_read.txt')

input('\nNotice the basics5_read.txt file is gone and press enter')

# To create a file we will use the open() function again,
    # With the the "x" or "create" mode to throw an error if the file already exists

createFile = open('basics5_create.txt', 'x') # We went ahead and assigned it as a variable so we can close it later
    # Now we have a new file but it's empty
print('\nNotice the basics5_create.txt file that open("file.txt","x") created')
input('press enter to delete it and continue')
createFile.close()
os.remove('basics5_create.txt')



print('\n----------------------------')
print('Example 3: Writing To A File')
print('---\n')


# First let's make a new file in write mode which won't throw an error if the file already exists
    # Creating a new file in write mode will overwrite a previous file with the same name
        # And since it was newly created it will also be blank, so careful not to overwrite a useful file
writeFile = open('basics5_write.txt', 'w')


# Now that we have a file open in write mode we can write to it,
    # To do that we'll use the file object's write() function
writeFile.write('Writing some text into our file for the first time!')


# And print it out 
    # But to print it out we need to open it in read mode
writeFile = open('basics5_write.txt', 'r')
print('The inside of our new file says ---' + writeFile.read())
writeFile.close()


# Now if we re-opened in it write mode to add more to it, anything in the old file would be overwritten
    # So instead we'll open it in Append mode to add on to the end
writeFile = open('basics5_write.txt', 'a') 

writeFile.write('Here\'s an appended line inside the write file')
writeFile = open('basics5_write.txt', 'r')
print(writeFile.read())




# --------------------------------------------------------
# ! ! ! HOMEWORK ! ! ! 
#  https://www.w3schools.com/python/ref_func_range.asp  <<< may be helpful


# Create a script that, when run, asks the user for:
    # A File Name
    # Some text content to put into the file
        # it will prompt the user from the terminal when the python file is executed

# Then the script should append a custom line of text to the end of the file
        # e.g. "This file was made by a script"



