# Software Development Plan

# Phase 0: Requirements Specification 

*   Creating a decryptor that takes a user defined text file (a path), checking to see if the file is real and acceptable. The decryptor then reads through the file containing a cryptic message and outputs it in plain English. If the file is invalid, the program should safely exit and give a message for why the programming is quiting. When reading through the text file, if the program reads a nonDuckieCrypt character, it should skip it over it and conintue deciphering the message. If no valid DuckieCrypt characters are given, then the program will only output the new line characters.



*   A good solution is one where there are no error, the program does not crash and it is 100 percent accurate in dichipering the DuckiCrypt message into plain English. The program can safely exit when not recieving a text file and can skip over the nonDuckieCrypt characters without changing the message of the real DuckieCrypt characters. The actual coding portion of the program does not have super repetive parts with a large number of variables that could be efficiently simplified while keeping the program readable and easy to understand from a outside developer's perspective. Ideally this program can be written in around 100 lines of code.

    *   I already know how to read through a file. print to the console and safely open a file.


    *   I can forsee the problem of handling reading through the DuckieCrypt and changing the characters into their appropriate values. 

    *   I believe skipping over the nonDuckieCrypt will be difficult

    *   Only opening and reading through text files, safely exiting for anything else might get difficult.

    *   I do not understand what the decryptLine(line) does opposed to the decryptCharacter(character) function


# Phase 1: System Analysis 

###   Input
*   A file
    *   Does not have to be a text file
    *   Should be a text file to decrypt

###   Output
*   A decrypted plain English version of the message from the inputed text file
*   An error message if the file is not a text file


###   Algorithms

*   getFile
    *   Takes in a file path as a string
    *   Safely checks whether or not the file can be opened
    *   Returns an opened file object or an error message saying the file path was invalid

*   decryptLine: Takes in a line from the file: Outputs decrypted line in plain English
    *   Takes in a line of DuckieCrypt
    *   Split at white space  
    *   Strip the white space -- > I am not sure if I need to do this
    *   Read through the line in a loop
        *   Call decryptCharacter on each DuckieCrypt character in the list
    *   Returns the decrypted line
    
*   decrpytCharacter: 
    *   if underscore in the first position of character code
        * call convertToLower
    *   if carrot in the first position of character code
        * call convertToUpper
    *   if plus sign in the first positon of character code
        *   call convertToSpecialChar
    *   else if the character does not match any of the ones listed above
        *   skip and continue reading through the string

*   convertToLower: Takes in a DuckieCrypt Character
    *   Remove underscore from string
    *   converts number to appropriate ascii value
        *   add 97 to the current number
    *   return the converted character

*   converToUpper: Takes in a DuckieCrypt Character
    *   Remove carrot from string
    *   converts number to appropriate ascii value
        *   add 65 to the inputed number
    *   return converted character

*   convertToSpecialChar: Takes in a Special DuckieCrypt Character
    * Remove plus sign from string
    *   Checks if the zero position is equal to A, B or C
    *   If equal to A
        *   Remove A from string
        *   Ascii value between (and including) 32 to 64
            *   convert string to integer
            *   Add 32 to number
    *   If equal to B
        *   Remove B from string
        * Ascii value between (and including) 91 to 96
            *   Convert string to integer
            *   Add 91 to number
    *   If equal to C
        *   Remove C from string
        *   Ascii value between (and including) 123 to 126
            *   Convert string to integer
            *   Add 123 to number
    *   If nothing matches (the if statement)
        *   Return nothing (this effectively skips the character)
    *   Return appropriate DuckieDeCrypted Special character


*   sendError
    * If the program encounters an error, safely exit and return a message saying that the program is quitting for a reason

*   main
    * Run the decrypter      


# Phase 2: Design 

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.


*   getFile(pathToFile): Returns file object or string error message
    *   Description: This take a file and checks whether or not it is a text file, returns a opened file object or an descriptive error message
    *   Parameters: The variable 'pathToFile' is a string, pathway to a file
        '''
            if os.access(pathToFile, os.R_OK) --> This checks whether the file is readable or not
                file equals to open(pathToFile, "r")
                return file
            else:  --> This is if the file is not readable, returns an error message
                return("File is not readable")
        '''

*   decryptLine(line): 
    *   Description: Takes in a line from the file: Outputs decrypted line in plain English
    *   Parameters: The variable 'line', it is a string containing the whole line of DuckieCrypt from the file
        '''
            output equals an empty string ("")  --> Creates a empty string to add the decrypted words to
            line equals line.strip() --> This removes the whitespace from the right and left side of the DuckieCrypt line
            line equals line.split() --> This automatically splits at everywhite space, turning it into a list
            for duckieCharacter in line:
                output equals output plus decryptCharacter(duckieCharacter)
            return output --> Returns the complete decrypted line

*   decrpytCharacter(character): 
    *   Description: Takes in a DukieCrypt Character and decrypts it into plain English
    *   Parameters: The variable 'character', it is a string containing both the DuckieCrypt flag and character code
    '''
        if character[0] (logical operator) is equal to '_': --> If the character in the zero position is equal to an underscore
            character equals character[1:] --> Keeps everything but the item in the zero position
            return convertToLower(character) --> Call the convertToLower with the variable 'character' as the argument
        elif character[0] (logical operator) is equal to  '^': --> If the character in the zero position is equal to a carrot
            character equals character[1:] --> Keeps everything but the item in the zero position
            return convertToUpper(character) --> Call the convertToUpper with the variable 'character' as the argument
        elif character[0] (logical operator) is equal to '+': --> If the character in the zero position is equal to a plus/addition sign
            character equals character[1:] --> Keeps everything but the item in the zero position
            return convertToSpecialChar(character) --> Call the convertToSpecialChar with the varibale 'character as the argument
        else:
            continue --> This continues but skips the character
    '''
    
*   convertToLower(charCode): 
    *   Description: Takes in a  string that is the DuckieCrypt Character Code
    *   Parameter: String that is the variable 'charCode' which is just the DuckieCrypt Character Code
    '''
        charCode equals a type casted charCode (from string to integer)
        charCode equals charChode plus 97
        return chr(charCode)
    '''

*   converToUpper: Takes in a DuckieCrypt Character
    *   Description: Takes in a  string that is the DuckieCrypt Character Code
    *   Parameter: String that is the variable 'charCode' which is just the DuckieCrypt Character Code
    '''
        charCode equals a type casted charCode (from string to integer)
        charCode equals charChode plus 65.
        return chr(charCode)
    '''

*   convertToSpecialChar: Takes in a Special DuckieCrypt Character
    *   If 'A' in charCode:
        *   charCode equals charCode[1:]
        *   charCode equal ord(charCode)
        *   charCode equals charCode plus 32
        *   Return chr(charCode)

    *   If 'B' in charCode:
        *   charCode equals charCode[1:]
        *   charCode equal ord(charCode)
        *   charCode equals charCode plus 91
        *   Return chr(charCode)

    *   If 'C' in charCode:
        *   charCode equals charCode[1:]
        *   charCode equal ord(charCode)
        *   charCode equals charCode plus 123
        *   Return chr(charCode)

    *   Else: --> If there is not a A, B or C in the charCode
        *   return "" --> Returns nothing


*   sendError()
    *  DESCRIPTION:  	    	       
        *   Exits the program after printing an error message.  	    	       

    *   PARAMETERS:  	    	       
        *   msg : None | str  	    	       
        *   The message to print in the error message.  	    	       
        *   If no `msg` is given, the default message becomes "Error! An error was encountered, so the program is quitting."  	    	       
    * exitCode : int  	    	       
        The exit code to exit the program with.  	    	       
        If no exitCode argument is given, it defaults to 1.  	    	       

*   RETURNS:  	    	       
    *   Nothing, program quits with exit code `exitCode`

    '''
    if msg is None:  	    	       
        msg = "ERROR! An error was encountered, so the program is quitting."  	    	       
    print(f"""\  	    	       
!!!QUACK!!!  	    	       
================================================================================  	    	       
{msg}  	    	       
================================================================================  	    	       
!!!QUACK!!!  	    	       
""")  	    	       
    sys.exit(exitCode) 
    '''

*   main()
    *   Description:  	    	       
        *   Run the main logic of the DuckieDecrypter program. Decrypts a given file, if it exists, printing out the result.  	    	       

        *   PARAMETERS:  	    	       
            *   filePath : str  	    	       
                *   The relative or absolute path to the file to decrypt  	    	       

        *    RETURNS:  	    	       
            *   Nothing. Just prints out the decrypted text.
        '''
        file equals getFile(filePath)  	    	       
        for line in file.readlines():  --> Loops over each line in the file   	       
            print(decryptLine(line))    --> Calls the decryptLine function with line as a parameter
        file.close() --> Closes the file after I am done with it
        '''

# Phase 3: Implementation 

* Things I learned was that I really need to read more of the directions and really think about all the variables that I need and the process my program needs to be successful.

* Breaking things down into smaller, more managable parts was significantly easier than trying to go from a larger concept to a smaller one.

* A lot of my planning paid off and there was only minor fixes rather than having to rewrite an entire program like I have had to do in the past.

* One thing that did not go according to plan was how I opened the file. Originally I had it set up to only read from text file and I did not notice this until I was debugging.


# Phase 4: Testing & Debugging 

* 09/12/2022 I tried to encrypt the msg0.txt but it was throwing an error because my filePath is not being convereted to a file object.
    *   One thing that I noticed was the line numbers kept changing for the error location but in the same general area
        * Although this might have been caused by me inputing lines of test statements
    * I tried running os.access(filePath, os.F_OK) to see if the path existed and it does not

*   09/15/2022
    *   Bug: My program could go out of bounds of the list
    *   How I ran the program: python.exe duckieDecrypter.py in WSL in cs1440-washburn-layton-assn1 directory 
    *   Input: ../data/msg0.txt
    *   Fixed by: Making sure that there is more than one element in a list
        * if len(charCode) < 2:
            return ""

    *   Bug: Invalid literal for int() with base 10:
    *   I ran the program ../data/msg1.txt
    *   How I ran the program: python.exe duckieDecrypter.py in WSL in cs1440-washburn-layton-assn1 directory
    *   Input: ../data/msg1.txt
    *   Fixed by: Making sure that int() was not being passed an empty string.
        * if charCode == "":
            return ""

    *   Bug: My program was not reading msg2 because it was not a text file and only printing newlines
    *   How I ran the program: python.exe duckieDecrypter.py in WSL in cs1440-washburn-layton-assn1 directory
    *   Input:  ../data/msg2
    *   Fixed by: Removing the "r" from the open() in the getFile function. This allowed me to return an opened file object and read from both txt files and non txt files
    

# Phase 5: Deployment  

*   Assignment 1 duckieDecyrpter has been varified and validated. It works when being run in a different location and after being cloned. I made sure of this and went to the CS tutor center to make sure that I was doing the steps correctly.

# Phase 6: Maintenance

*   The parts of my program that are sloppily written is probably the documentation Phase 0 and Phase 1 and the decryptChar function. I also think the program in general is organized in a weird and sloppy way. I should have arranged it better so that it flows smoother when someone is looking through it.
    *   I am unsure how the main function completely works. I am not familar with python command line arguments.
    *   If a bug was reported in a few months, I feel like it would take a decent amount of time to find the cause because there are so many parts of this program that are named the same thing and it can get very confusing. The program is not organized very well so to find a bug, someone would have to scroll up and down a lot to find the related sections.

* My documentation would make sense to someone else but I think it could be much cleaner. In six months time, I will definitely be confused by what I was tyring to say. I have a lot to work in for organizing my documentation.

*   I think that it will be easy to add a new feature into this program in a year because the code itself is relatively easy to understand and follow. I think that they hardest part will be switching between parts and keeping the variable names seperated because they are very similar.

* I think that this program would still work after upgrading the system's hardware as long as the functions can still operate and communicate as they usually do. I think if the operating system was changed, this program might have a hard time because it might interact differently and not all of the keyword might translate. If another version of python came out, there would be a significant chance that this program would not work because the keywords might differ, inbuilt functions might change and particualar aspects that are crucial to python 3 might change, making the program broken.

