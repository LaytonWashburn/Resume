# Software Development Plan

## Phase 0: Requirements Specification 

#### Cat Program

*   Requirements

    *   To write a program that recreates the basic cat Unix test processing program. This cat program takes a filename, or multiple file names and prints the contents to the terminal.

    *   The solution needs to have the contents printed out to the console.

    *   The program terminates when an inassessable file, invalid or non existant is given. There is no prescreening of the arguments.

    *   A good solution looks like the cat program printing out all assessible files to the console and raising an error and terminating for all invalid files.

*   Things I already Know How to Do

    *   I already know how to open and read through a file.

    *   I know how to print out the contents of a file line by line

*   Challenges I anticipate

    *   Read arguments from the Command Line

    *   Get the file names from the command life

#### Tac Program

*   Requirements

    *   To print out a file contents in reverse order. Working the same as cat, just in reverse. Takes as many files from the command line as arguments and prints out the contents in reverse order for the file that are able to be opened and raises an error for those that cannot be opened.

    *   The contents need to be printed out to the console in reverse order

    *   A good solution looks clean, meets all the requirements and crashes at the appropriate time.

*   Things I already Know How to Do

    *   Open a file

    *   Print the contents of a file line by line

*   Challenges I anticipate

    *   Printing the files's contents in reverse

##### Paste Program

*   Requirements

    *   Takes in arguments from the command line and stores the file objects in a list. It iterates over each file object, printing the values out, each files argument seperated by a comma. After all contents are printed, a newline character is printed. If only one file is given, then the paste program acts like the cat program. The output get stored in a CSV file using the redirection operator

    *   A good solution looks clean, meets all the requirements and crashes at the appropriate time.

    *   This can work hand in hand with the Cut program, they are basically opposites, one outputs info to a file and the other extracts it.

*   Thing I Know How to Do

    *   I know how to open a file

    *   Make File Objects

    *   Put items into lists

    *   Print the sdtout to another file

*   Challenges I anticipate

    *   Seperating the values of the different files with a comma

    *   Making sure that all values get printed

        *   The file prints as much as the longest file and the other files just print an empty string because they don't have values

#### Cut Program

*   Requirements

    *   The program extracts the specified data either assuming column 1 or using the -f to specify columns. The program then extracts the data and prints it to the console. The program correctly handles errors such as no -f argument and makes sure that when a file prints out values outside of it range in the case of cutting multiple files, blank lines are printed.

    *   A good solution looks clean, meets all the requirements and crashes at the appropriate time.

*   Things I Know How to Do

    *   Open and read through a file

    *   Get elements from a list

    *   Print the values

    *   Print a new line

    *   Ensure that -f is an argument if given no arguments

*   Challenges I anticipate

    *   Extracting the data

    *   Handling all errors correctly

#### Grep Program

*   Requirements

    *   Takes an argument (the value searching for) that is case sensitive and looks through the file(s) given as an arguement and prints out the lines containing the argument that it is searching for. If given the '-v' argument, then it prints out the lines not containing the argument that is inputed.

    *   A good solution looks clean, meets all the requirements and crashes at the appropriate time.

*   Things I Know How to Do

    *   Search for a specific value in an object, string or list

    *   How to print out the lines containing the value

    *   Print out the lines not containing the value

    *   Search for the '-v' argument

    *   Open and read through files line by line

*   Challenges I anticipate

    *   Handling all errors

    *   Handling all edge cases

#### Head Program

*   Requirements

    *   Takes in a file and opens it, printing out the first ten lines or less. If given the '-n' argument, then a different limit on the amount of lines printed can be set. If given multiple files, the program displays a banner above any printed file lines, specifying the file that is currently being printed.

    *   A good solution is one where it prints the appropriate number of lines and can display the banner for the appropriate file

    *   This works with files, and printing values to the console

*   Things I Know How to Do

    *   Open and read through a file line by line

    *   iterate a certain amount of times

    *   Search for the '-n' argument in the command line

    *   Type convert a string to an integer and vice versa

*   Challenges I anticipate

    *   Printing out the banners in the right place for the right file

    *   Handling all errors correctly

#### Tail Program

*   Requirements

    *   Prints the final 10 lines of a file or if given the '-n' flag, prints the newly specified length, meaning prints the N final lines of the file. The program crashes if a file cannot be opened, is invalid or accessable and crashes if the '-n' argument does not recieve an argument or a numerical argument. If given multiple files to work with, it displays a banner that allows the file to be identified in the printed information in the console.

    *   A good solution looks like one where the program prints out the last N lines of the file or crashes in an appropraite manner given errors.

*   Things I Know How to Do

    *   Open and loop through a file line by line

    *   Look for the '-n' argument in the command line

    *   Print to the console

*   Challenges I anticipate

    *   Printing a banner to the console to identify the file

    *   Handling all errors correctly

#### Sort Program

*   Requirements

    *   Takes in a file in the command line as an argument and then sorts the contents lexigraphically. If multiple files are given, then the output is a combination of all the content sorted lexigraphically. Sorting lexigraphically is using the Ascii values.

*   Things I Know How to Do

    *   import a module

    *   Read a file from the command line as an argument
    
    *   Print to the console the output

*   Challenges I anticipate

    *   Working with multiple files and sorting them so that is one big output that is sorted lexigraphically.

#### Word Count Program

*   Requirements

    *   Prints out the number of Lines, word and characters(bytes) in a file and then the file name/argument after the numbers in a single line. If given multiple files, then it lists each line, word and character(byte) count for each file in a seperate row and shows the total in a final line. The numbers are right justified while the file name/argument is left justified.

*   Things I Know How to Do

    *   Open and read through a file and keep track of counter variables

    *   Print out the name of the file/argument

    *   Sum up the total 

*   Challenges I anticipate

    *   Right and Left justifying things in the format

        *   Formatting in Python

    *   Handling all errors correctly

#### Usage

*   Requirements

    *   Shows the syntax and a brief description of all nine of the programs that can be called

*   Things I Know How to Do

    *   Call Usage

*   Challenges I anticipate

    *   Making sure that I do not need to do anything else with this file

#### tt.py

*   Requirements

    *   Imports all the files correctly and ensures that the command line is recieving the correct amount of arguments and then determines which program it needs to call.

*   Things I Know How to Do

    *   Determine which program/method is being used.

    *   Call a program/method

*   Challenges I anticipate

    *   Forwarding the command line arguments onto the program/method



## Phase 1: System Analysis 

#### Cat Program

*   Inputs

    *   Command Line Arguments (strings)

        *   python, pythonFileToRun, file, file,....

        *   Files will contain lines of text, numbers or empty strings

    *   Specifically looks at the files being passed in

*   Outputs

    *   The file's text to the Console

    *   Error message to the Console calling the Usage function if error

*   Key Functions

    *   Function's Name

        *   cat

    *   Function's Inputs

        *   Command line arguments (the system argv)

    *   Functions's Outputs

        *   Prints the file line by line

        *   call Usage function

    *   Function's Description-one sentence

        *   prints the file's entire content line by line to the console or an error message

#### Tac Program

*   Inputs

    *   Command Line Arguments (the system argv) (Strings)

    *   Specifically looks at the files being passed in as strings

*   Outputs

    *   The last 10 or last "N" number of lines or an error message to the console

*   Key Functions

    *   Function's Name

        *   tac

    *   Function's Inputs

        *   args - a single string(fileName) or a list of file names

    *   Functions's Outputs

        *   Strings of the lines from the file

        *   Error message printed to the Console

    *   Function's Description-one sentence

        *   This prints the last 10 or "N" lines or an error message to the Console

##### Paste Program

*   Inputs

    *   A single string or a list of the file names

*   Outputs

    *   Nothing to the Console
    
    *   A new CSV file containing the data seperated by commas

*   Key Functions

    *   Function's Name

        *   paste

    *   Function's Inputs

        *   args which is the list of file(s)

    *   Functions's Outputs

        *   Nothing

        *   CSV file containing the file's information seperated by commas

    *   Function's Description-one sentence

        *   Takes one file or multiple and returns the contents in a CSV file seperated by commas or an error message.

#### Cut Program

*   Inputs

    *   A single string or a list of the file names 

*   Outputs

    *   For one file: The specified information printed out

    *   For multiple filess: All the values printed out by specified colums

*   Key Functions

    *   Function's Name

        *   cut

    *   Function's Inputs

        *   Command line arguments that are the files

        *   -f: and the specified columns

    *   Functions's Outputs

        *   printed text of the specified file

        *   Error message if any errors

    *   Function's Description-one sentence: Cuts specified information from file(s) and prints it to the Console.

#### Grep Program

*   Inputs

    *   Command Line arguments

        *   the program name

        *   the word the user wants to look for

    *   Files that the user is inputing

*   Outputs

    *   prints the lines containing the specidied word in the command line arguments to the Console

    *   prints the lines not containing the specified word in the command line arguments to the Console if given a '-v'

    *   Prints an error message to the Console if there is an error

*   Key Functions

    *   Function's Name

        *   grep

    *   Function's Inputs

        *   args - the command line arguments that are the files, either in a single string or a list with multiple

    *   Functions's Outputs

        *   Strings that are printed to the Console line by line that contain the specified value

        *   Strings that are printed to the Console

        *   Error message printed to the Console 

    *   Function's Description-one sentence: Takes a value specified in the command line and returns the appropriate lines of the file or an error message.

#### Head Program

*   Inputs

    *   Command line arguments

*   Outputs

    *   printing out up to the first ten lines of a file: A String

    *   printing out up to the last ten lines of a file: String

    *   printing out the 'n' number for either the first or last side of the file: A String

*   Key Functions

    *   Function's Name

        *   Head

    *   Function's Inputs

        *   The command line arguments

            *   A list of strings or a single string

    *   Functions's Outputs

        *   printing out up to the first ten lines of a file: A String

        *   printing out the 'n' number from the beginning of the file: A String

    *   Function's Description-one sentence: Prints out up to the last 10 or 'n' lines of the file starting from either the start or the end of the file.

#### Tail Program

*   Inputs

    *   Command Line Arguments

        *   A list of strings or a sinlge string

*   Outputs

    *   Printing up to the last 10 or 'N' lines in the file

*   Key Functions

    *   Function's Name

        *   Tail

    *   Function's Inputs

        *   command line arguments

            *   The file to be read

            *   Optional '-n' argument to change the limit of lines

    *   Functions's Outputs

        *   Printing the string (lines) up to the last 10 lines or 'N' lines in the file

    *   Function's Description-one sentence

#### Sort Program

*   Inputs

    *   Command line arguments

        *   One or more files 

*   Outputs

    *   Printed text to the console sorted in lexigraphical order

    *   Error message is something went wrong and the program crashes

*   Key Functions

    *   Function's Name

        *   sort

    *   Function's Inputs

        *   A single string or a list of strings with the files to be sorted lexigraphically

    *   Functions's Outputs

        *   Printed text to the console sorted in lexigraphical order

        *   Printed error message if the program needs to crash or input was entered wrong

    *   Function's Description-one sentence: Takes in file(s) from the command line and then sorts all the content by lexigraphical order and prints the content to the console.

#### Word Count Program

*   Inputs

    *   Command line arguments either a single string in a list or a list of string

*   Outputs

    *   the word, line and character(byte) count for all the files printed on each line with the name of the file at the end of the line to identify the file

*   Key Functions

    *   Function's Name

        *   wc

    *   Function's Inputs

        *   Command line arguments, either a single string in a list or a list of strings containing the files to be read and counted

    *   Functions's Outputs

        *   The word, line and character(byte) count for each file on seperate lines for each file

        *   The total summed up if there are multiple files in the command line

    *   Function's Description-one sentence: Takes in file(s) and then iterates through each, counting the amount of words, lines and characters in each and prints the amount and the total (for multiple files) to the console.

#### Usage

*   Inputs

    *   none

*   Outputs

    *   the command and a brief definition of each printed to the console

*   Key Functions

    *   Function's Name

        *   Usage

    *   Function's Inputs

        *   None

    *   Functions's Outputs

        *   the command and a brief definition of each printed to the console

    *   Function's Description-one sentence: Prints out a error message with the functions and a brief definition for the program and safely exits.

#### tt.py

*   Inputs

    *   none

*   Outputs

    *   none

*   Key Functions

    *   Function's Name

        *   tt

    *   Function's Inputs

        * none

    *   Functions's Outputs

        *   none

    *   Function's Description-one sentence: This calls the correct program that is asked from the command line and runs it if the command line has more than two arguments in it.



## Phase 2: Design 

### cat

*   function name:   cat   

*   parameters: command line arguments
    *   args

*   Check if cat received enough arguments
    *   call usage is not enough arguments are given

*   splice the file names from the command line

*   Loop through the files in the command line argument list
    *   Open the file - making an open file object
    *   Loop through the file
        *   print each line making sure not to include the new line character
    *   close the file

### tac

*   function name:   tac

*   parameters: command line arguments
    *   args

*   Check whether tac was given enough arguments
    *   call usage if not given enough arguments

*   splice the file names from the command line

*   loop through the files in the command line argument list
    *   set variable "sentence" equal to an empty list
    *   Open the file - creates an opened file object
    *   Read through the file line by line
        *   remove the newline character
        *   append the list "sentence" with the line without the newline character
    *   Loop from the end of the file (the length of sentence) down to -1 because we need to include 0
        *   print the loops iteration indexed in sentence
    *   Close the file


### cut - not finished

*   function name:   cut

*   parameters: command line arguments
    *   args

*   Slices the command line to get the files
*   Checks whether cut recieved one or more arguments
    *   Call Usage if no file(s) are given
*   Checks whether '-f' is in cut
    *   Call Usage if '-f' is given no arguments
*   maxInt equals zero
*   if multiple files
    *   Loop through the command line determine which one is the longest (make a variable for the longest)
        *   Open files
        *   if current file's length is greater than the current value of largest, make the length of the file equal to largest
        *   Close files
    *   loop in the range from 0 to the maxInt plus one to include that value
*   If one file
    *   Iterate through the "list" of file
        *   open the file
        *   loop through the lines
            *   print each line out
        *   close the file


*   splice the file names from the command line


### paste

*   function name:   paste   

*   parameters: command line arguments
    *   args

*   Checks whether or not paste recieved one or more arguments
    *   Call Usage if no file(s) are given

*   splice the file names from the command line

*   If only one file is given, paste behaves like cat but prints to a cvs file instead of the console

*   Create empty list 'fileList'
*   Loop through the command line arguments
    *   Open file and make file object
    *   store file object in a list

*   Loop over the list of file objects
    *   if within the range of the file
        *   print the first line of each and add a comma
    *   If out of range
        *   print an empty string
    *   if last file in list
        *   print newline at the end

*   Loop over the list of file objects
    *   close the files


*   Declare variable 'largest' equal to zero
*   Loop through the command line determine which one is the longest (make a variable for the longest)
    *   Open files
    *   if current file's length is greater than the current value of largest, make the length of the file equal to largest
    *   Close files
*   Loops in the range of 0 to the length of the longest file plus one
    *   loop through the list of files
        *   Open the file
        *   Check whether the index is out of range
            *   If it is
                *   Print an empty string
            *   else
                *   Print the file (index of the outer loop)
        *   Close the file


### grep

*   function name:   grep  

*   parameters: command line arguments
    *   args
*   check if grep received any arguments
    * if not 
        *   call usage
*   splice the file names from the command line
*   Get the word that is being searched for
*   Check if '-v' is in the command line arguments
    *   if '-v' 
        *   Make sure that '-v' has arguments given to it
        *   if '-v' has arguments
            *   loop through the files
                *   open the files
                *   Loop through the lines of the file
                    *   If the word is not in the sentence
                        *   print out the line
                    *   else
                        *   skip over it
                *   close the file
        *   If '-v' has no arguments
            *   call usage
*   If '-v' not in command line arguments
    *   Loop through the files
        *   open the file
        *   Loop through the lines of the file
            *   if the word is in the line
                *   print our the line
            *   else
                *   skip
        *   close the file

### head 

*   function name:   head   

*   parameters: command line arguments
    *   args

*   maxIt variable equals ten
*   splice the file names from the command line
*   Check if head was given the '-n' argument
*   if '-n' is there
    *   if '-n' recieved a number (an argument after '-n')
        *   then maxIt variable equals the argument after '-n' in the command lines
    *   else ('-n' did not recieve and argument)
        *   call Usage to raise an error
*   else '-n' is not there
    *   continue on throughout the program (maxIt is already ten)
*   Check whether there are multiple files
    *   If there is more than one file
    *   iterate through the list of files
        *   open the file
        *   Print the banner of the file name
        *   Iterate from 1 to maxIt or EOF
            *   open file
            *   Check to make sure that the file can print another line
            *   print one line of the file excluding the newline character at the end of the line
        *   close the file
    *   Else (if there is only one file)
        *   open the file
        *   Iterate from 1 to maxIt or EOF
            *   open file
            *   Check to make sure that the file can print another line
            *   print one line of the file excluding the newline character at the end of the line
        *   close the file


### tail

*   function name:   tail   

*   parameters: command line arguments
    *   args

*   Create variable 'lineAmount' equal to ten
*   splice the file names from the command line
*   Check whether or not tail got file
    *   if not
        *   call Usage
*   Check whether or not '-n' is in the command line
    *   check to see if the '-n' flag got a numerical argument
        *   if it did
            *   set 'lineAmount' equal to the numerical argument
        *   else (if it did not)
            *   call Usage
*   Loop through the command line arguments (the file list)
    *   Create an empty list named 'list'
    *   if list is greater than one argument
        *   print a banner to identify the file
    *   if the list only has one file, no banner
    *   Loop through the lines of the file
        *   append the lines to the empty list
    *   print the list from the negative 'lineAmount' to the end
    *   print a newline at the end of the last printed line

### sort

*   function name:   sort   

*   parameters: command line arguments
    *   args

*   splice the file names from the command line
*   Create an empty list with the name allContents
*   Loop through the command line arguments
    *   open the file
    *   use sort function on the file
    *   close the file
*   Use sort function on the command line arguments
*   Loop through the command line arguments
    *   Open the file
    *   Loop through the lines
        *   print each line to the console
    *   
### wc

*   function name:   wc   

*   parameters: command line arguments
    *   args

*   splice the file names from the command line
*   Check whether wc got arguments
    *   If not
        *   call Usage to raise an error
*   Create variables
    *   lineCount equal to 0
    *   wordCount equal to 0
    *   characterCount equal to 0
*   Loop through the command line arguments (the files)
    *   Set the file cursor to the front of the file and iterates by one character/byte at a time
    *   Loop over the lines until the EOF
        *   If character is not '\r\n' or ' ' (a white space)
            *   add one to characterCount
        *   if character is ' ' (a white space)
            *   add one to wordCount
        *   if character is '\r\n' and is not EOF
            *   add one to lineCount
    *   Print out the line, word and charcter count alond with the name of the file(command line argument)

### Usage

*   function name:   Usage  

*   parameters: None

*   I do not need to do anything to this program, it was one of the ones that were built in

### tt

*   function name:   tt   

*   parameters: None

*   Use a if, elif, else statements, default statements to detect what program is being called
    *   call the program
*   Raise an error message is no arguments are given


## Phase 3: Implementation


### Cat and tac
*   I did not have usage anywhere in cut to handle errors and then I put usage in the appropriate place in the function to handle any time arguments are not inputed.

*   Most things in these went as according to plan. The only thing was implementing 'usage()' into the functions.

### Cut

*   The actual work part of my code that cut the lines from the file was wrong and did not work because there were too many errors.
    * I I learned that a while loop is really useful to control the loop and may be better than a for loop in some cases.

    *   Handling errors did not go according to plan. I was going to have to write a lot of 'if' statements to handle all the errors

    *   I learned that I needed to write a section that handles the different cases and then another section that does the work instead of writing one section for a specifc case that does the work and then for another case and the work inside. 
        *   This allows me to condense the code and not be redundant.

    *   I needed to rethink the loop control because I was having a hard time determining when I was at the end of the file list using a for loop without writing a bunch of extra code.

### Paste

*   I needed to reset the file back to the start after reading through it to get the longest file. And it took debugging to figure this out.
    *   I learned how to use 'seek()' a little more.

*   I stripped out the newlines and then needed to add some back in which did not go according to plan.

*   I needed to close all the files in a seperate loop to make sure that all the files get closed.

*   Most everything went according to plan. I did have to rewrite the pseudocode for this program last minute.
    *   I learned that I need to read the directions more thouroughly before I try to plan it.



### Grep

*   Most things went well here.
*   I did forget to add the usage function to handle errors.
*   I learned that I really need to divide my code more efficiently so that I don't have to write huge if else statements

*   A lot of what changed what the index of the search word and when I cut the command linie argument list. I needed to do this because things got jumbled around and it was throwing an indexing out of range error.

### Head

*   I ran into a lot of errors for handling errors.
*   I made major changes to the placement of the usage function calls to handle errors
*   type casting did not go according to plan because I did not plan that area of programming well.

*   I also did not account for having to use fstrings in this but I figured it out because I needed to make banners for the different files.
    *   I learned how easy it is to implement fstrings into my code and that it was not as hard as I thought.

*   Most of the program went according to plan except for the handling errors because I had a decent plan

### Tail

*   I had to change how I got the last lines of the file
*   I learned that I can use list slicing to ge the last lines of the files

*   I needed to change this because it allows me to more efficiently control how I get the last amount of lines.

### Sort

* most of the implimentation went according to plan. I had to adjust the indexes and move some logic around but that was about it.

### WC
*   The indentation took some creativity but I was able to impliment it using python's fstrings
*   It took a while to figure out how to count the words, but I was able to figure it out by splitting on white space and then checking the length of the list and then adding that to the word count variable.



## Phase 4: Testing & Debugging

### cat
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py cat'
    * This should make the program call usage because there is no file given to the program
    
    *   Error: Too few arguments

        tt.py cut [-f LIST] FILENAME...
    Remove comma-separated sections from each line of files
    -f  List of comma-separated integers indicating fields to output (default is LIST=1)

*   I did not have many errors because we worked this in class

### tac
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py tac'
    * This should make the program call usage because there is no file given to the program
    *   Error: Not enough arguments

        tt.py cat|tac FILENAME...
    Concatenate and print files in order or in reverse

*   I did not have very many errors because this one was well thought out. planned and implimented

### cut
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py cut'
    * This should make the program call usage because there is no file given to the program

    *   Error: Too few arguments

        tt.py cut [-f LIST] FILENAME...
    Remove comma-separated sections from each line of files
    -f  List of comma-separated integers indicating fields to output (default is LIST=1)

    *   The smae error is thrown in -f is not given any arguemtns
        * 'python.exe src/tt.py cut -f'

        *   Error: Too few arguments

        tt.py cut [-f LIST] FILENAME...
    Remove comma-separated sections from each line of files
    -f  List of comma-separated integers indicating fields to output (default is LIST=1)

    *   There was a bug where my program would run and not crash, but would not work
        * The remedy to this was to change the len of the command line argument list and call usage if below that number

    *   I had a bug where the loop did not know where to end, the index went out of range and the file would cut wrong.
        *   The remedy to this was using a 'while' loop instead of tyring to use for loops to iterate over the file and range
        *   Another remedy was to use boolean values to be the controller of the 'while' loop so that it could terminate at the end of the file list.

    *   I found out that I had done the program wrong and I needed to rewrite it.
        * it ended up looking like the plan more but there were still major tweeks to it.

### paste
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py paste'
    * This should make the program call usage because there is no file given to the program

    *   Error: Not enough arguments

        tt.py paste FILENAME...
    Merge lines of files into one comma-separated text

* One of the main errors that I had was not getting the first line of the file and printing everything else.
    *   The remedy of this was to seek back to the beginning of the file before moving onto the main portion of the program

### grep
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py grep'
    * This should make the program call usage because there is no file given to the program

    *   Error: Please provide a pattern and at least one filename

        tt.py grep [-v] PATTERN FILENAME...
    Print lines of files matching PATTERN
    -v  Invert matching; print lines which DO NOT match PATTERN

*   The most prone error was going out of range with the index.
    *   An easy fix to this was to print out the list and see where everything was located and then adjust the index number and where to slice at.

*   I did not have a lot of errors. I planned and implimented the program well

### head
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py head'
    * This should make the program call usage because there is no file given to the program

    *   Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
    Output the first or last part of files
    -n  Number of lines to print (default is N=10)

*   I got a lot of out of index errors for this
    *   I fixed this by adjusting the index integers to match what they were suppose to be in order for the program to work

*   Overall this program was well planned out and implimentated well

### tail
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py tail'
    * This should make the program call usage because there is no file given to the program

    *   Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
    Output the first or last part of files
    -n  Number of lines to print (default is N=10)

*   There were a couple times where my usage for handling errors was not good enough to handle all the edge cases that I could think of
    *   I fixed this by adding a few 'if' statements to handle specific cases that were occuring.

### sort
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py sort'
    * This should make the program call usage because there is no file given to the program

    *   Error: Not enough arguments

        tt.py sort FILENAME...
    Output lines of text file in sorted order


### wc
*   Bad inputs --> open(file)
    *   This will crash if the argument trying to be opened is not a file
    *   also if len(args) is less than a value
        *   This will crash if not enough variables are given to the program
*   Exact command 'python.exe src/tt.py wc'
    * This should make the program call usage because there is no file given to the program

    *   Error: Not enough arguments

        tt.py wc FILENAME...
    Print newline, word, and byte counts for each file
*   I kept getting the count wrong on some of them.
    *   I fixed this by rearranging where my counter variables were.



## Phase 5: Deployment *(5%)*

* Completed validation



## Phase 6: Maintenance

### What was sloppily Written?

*   There is a lot of my code that could be condensed and made more efficient. Cut and Paste could be much more efficient becasue they have huge indentations.

*   Head and Tail could both be rewritten to handle the parameters and different arguments first and then use one section of code to actually do the work for the program instead of having two differet sections that both handle arguments and to the work for the program

*   Head and Tail have a lot of if else statements for error handling instead of having one or two calls for it. This means that I could condense my code as specified in the bullet point above which would make it easier to handle the errors my program needs to.

### Will My Documentation make Sense

*   My documentation will probably not make sense to someone else who looks at it because the plan is much different than the actual code which means that the code does not represent a good pseudocode and design plan. This also means that it will be harder to add to this and understand what is going on without actually looking at the code. In short, my code does not reflect a lot of my planning because I did not think the problem out as much of I should have beforehand.

* My documentation barely makes sense to me so I expect that it will not make sense to anyone else. If I can't read it, no one else will be able to.

### New Features in a Year

*   It will be really hard to impliment new features into my code in a year because most of my functions are not divided efficiently and are extremely error prone. This means that I would have to make major changes to the entire body of code to impliment a new feature because a lot of my code is very specific rather than being generalized which would be much more effiecent short term and long term.

### Continue to Work After a Year

*   If the hardware got changed, I believe that my programs would still work as long as the command line stays the same and the way things in memory are stored.

*   If the software got changed, my code would not work. If the command line got changed, then my indexing and slicing would fall apart and make the program crash because of a out of range error or it would try to read a word as a number and vice versa.

*   As long as the next version of python stays the same with lists, the command line then my program should stay the same  and work well.