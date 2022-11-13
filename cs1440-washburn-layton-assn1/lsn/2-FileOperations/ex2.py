import os
import sys


def printContents1(file):
    '''
    This function will print the contents of a file object using one of the
    methods for reading the contents of files.

    `file` is an opened file object
    '''
    file.seek(0)
    print(file.read(), end = '')


def printContents2(file):
    '''
    This function will print the contents of a file object using one of the
    other methods for reading the contents of files.

    `file` is an opened file object
    '''
    file.seek(0)
    for line in file:
        print(line, end = '')
    


def printTwice(filename):
    ''' 
    TODO:
        1:  Open the file object *safely*.
            * Why don't I reuse something I've made before?
    f = a file object
        2:  Print it the first time
    printContents1(f)
        3:  Rewind the file
        4:  Print the file a second time
    printContents2(f)
        5:  Close the file
    f.close()
    '''
    if os.access(filename, os.R_OK):
        f = open(filename, "r")
        printContents1(f)
        printContents2(f)
    else:
        print("file provided could not be accessed, look before you leap!")
        sys.exit(1)
    f.close()


    
if __name__ == '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    printTwice(filename)
