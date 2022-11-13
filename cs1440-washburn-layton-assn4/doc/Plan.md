# Software Development Plan

## Phase 0: Requirements Specification 


### Detailed Written Description

*   Creating a program that interactively generates a Deck of Bingo Cards. This program will walk the user through a series of menus and options. The User will have the opportunity to create a deck of Bingo cards. Each Bingo card will have be at least 3x3 up to and including 16x16, this size of card will be specified by the user. The user will then have the options of printing a card out or all of the cards out to either the terminal or a user specified file. This project aims to have robust code that can be easily modified and is soley user interactive and does not take any command line arguments.

### A Good Solution

*   Will have Two Menu options at the starts
    *   Create a Deck
        *    Walks the user through the process of creating a deck if 'C' or 'c' is hit
            *   Takes input such as the number of cards the user wants to create
                *   Valid number of cards ranges from 2 to 8192
                *   All inputs should be integers
            *   The size of the cards the user wants to create
                *   Asks for size N
                    *   The card will be created of size N x N
                *   Valid ranges for N will be 3 to 16
            *   The program repeats the prompt until valid input is given
        *   The main menu for Create a deck will be given until valid input is given
    *   Exit the program
        *   Exits the program when 'X' or 'x' is hit
        *   Repeats prompt until valid input is given
*   Will have another menu for Deck options
    * This will let the user view their cards, save their deck to a file or return to the main menu

### Things I Already Know How to Do
*   Check for valid input
*   Run a method when valid input is given
*   Prompt the user for card size and number of cards
*   Print out to the console
*   Make sure that the input is not case sensitive
*   Print patterns to the screen

### Things I Think Will Be a Challenge
*   Printing to a file
*   Making methods call eachother correctly
*   Finding the one error in the RandNumberSet method
*   Finding how to print the Free Square in the direct middle of the card


## Phase 1: System Analysis 

### Data Used By the Program
*   Integers will be taken in from the following positions
    *   The Card Creating Process
        *   Number of Cards
        *   Size of the cards
*   Character from the following locations
    *   The First menu whether or not to choose to create a deck or exit
        *   Either a 'C' or 'X'
    *   Whether or not to view deck/cards
    *   Whether or not to print the deck/cards to a file
    *   To return to the main menu
### Output 
*   Menus and Prompts
    *   Prints out the word Bingo
    *   Prints out the options in the menu
*   Bingo Cards
    *   Format of the Bingo card is the correct size
    *   Cards are numbered by position in deck
    *   Cells are printed in plus, minus and pipe signs
    *   Cards are printed one at a time or all at once
    *   Printed Bingo Card either to the console or to a specified file
    *   This is text in the form of a string
*   

### Algorithms and Formulae
*   Create a list of numbers from 1 to M in order and then randomize it
    *   This ensures that no number will be used twice
*   By creating a list of numbers from 1 to M and then randomizing it `N` times, the first column gets the first $\frac{1}{N}$ of numbers, then second column gets numbers in the $\frac{2}{N}$ range of numbers, the third column $\frac{3}{N}$, and so on until all column are exhausted.


## Phase 2: Design 

### MenuOption Class
*   The `MenuOption` has a constructor that will take only two parameters, the character (character datatype) and description string (string datatype). These parameters will be stored in private member variables, and provided are public accessor methods.
*   Represents an option (character) the user has to select from and a string representing what it does. This is part of the menu
*   When a `MenuOption` object is printed to the console, it displays like to the user like this: `A) This is option A`.
*   There are three functions
    *   Returns just the character
    *   Returns just the description
    *   Returns both the character and the description in the form
        * Character - Description

### `Menu` class

This class contains a collection of `MenuOption` objects (most likely a `std::vector`).  In order to keep the constructor simple, these options will be added/appended to this collection after the `Menu` object is instantiated.  A `Menu` will have a title or header (string) to indicate the purpose of the menu.

To keep the code consistent, the `Menu` will be written to behave like a familiar collection (again, a `std::vector` feels like the right choice) so that the programmer can just treat this like any other collection from the standard library.  This means the `Menu` will implement the addition operation for "append", and the subscript operator `[]` allowing direct access to a `MenuOption` at a specified location.  The `Menu` will also support the `length()` operation to retrieve the number of `MenuOption`s contained within.

This object also has a `prompt()` operation, which displays the menu and awaits user input.  The first character of the string entered by the user is compared, case-insensitively, against the `MenuOption`s.  If a match is found, the character of the option is returned to the caller so it can determine which option was picked.  Otherwise, the menu is repeated forever until the user picks a valid option.


### `UserInterface` class

This class ties the whole app together.

There will be only one `UserInterface` object at a time in the program.

Initially, it will print the program logo and present the main `Menu`.  From the main menu the user can exit the program, or proceed to create a Deck. When the user chooses to proceed, the `Deck` creation menu is created and presented.  The `UserInterface` will then hold on to the `Deck` object until the user returns back to the main `Menu`; at that time the `Deck` is discarded.

This class also contains private methods that facilitate input/output for the user.

*   `string get_str(string prompt)` - Prompt the user with a `prompt`, then collect their input.  Return the `string` the user typed
*   `int get_int(string prompt, int lo, int hi)` - Prompt the user with a `prompt`, then collect their input.  If the input is not numeric, show the prompt again.  Repeat the prompt if the input is an integer but less than `lo` or greater than `hi`.
*   `create_deck()` - Guide the user through the questions that constrain how they create a Deck of Bingo Cards.
    *   Specifically, the user is asked for
        *   Size of Card $[ 3 \ldots 16 ]$ (use `get_int`)
        *   Max number to appear on Card $[ 2 * N^2 \ldots floor(3.9 * N^2) ]$ (use `get_int`)
        *   Size of Deck $[ 2 \ldots 8192 ]$ (use `get_int`)
*   `print_card()` - Prompt the user for a `Card` ID number to print.
    *   Use `get_int`
    *   Check that input is not greater than number of Cards in Deck
*   `save_deck()` - Prompt the user for a filename in which to save the current `Deck`.
    *   Uses `get_str` to ask the user for a filename
    *   The requirements don't ask us to validate the user's input - just trust that they know what they're doing and crash if something goes wrong.
    *   Printing a `Deck` to a file is just the same as printing it to the screen - the difference is that a file object is provided instead of `STDOUT`



### Layton's Plan For UserInterFace

*   Print the logo and present the main `menu`
*   If the user chooses to preceed :input is uppercase or lowercase C
    *   Guide the user through creating the deck
        *   prompt the user for the card dimensions
            *   'Enter Card Size [3 : 16]'
        *   prompt the user for the max number to appear on Card
            *   'Enter max size [x : y]'
        *   prompt the user for the number of cards they want in the deck
            *   'Enter number of cards [2 : 8192]'
        *   Check to make sure that the user input is numeric --> This should be done by the prompt 
    *   Create Deck Menu and present it
        *   P) Print
            *   'ID of card to print [x : y]'
        *   D) Display whole deck to screen
        *   S) Save whole deck to file
            * 'Enter output file name:'
                *   'Deck saved to {file name}!'
        *   X) Return to Main Menu
    *   The UserInterface will then hold on to the Deck object until user returns back to the main `Menu` and the `Deck` is discarded

*   method  __get_str(prompt)
    *   Takes a prompt string as input
    *   Repeat prompt until non-empty string prompt is given

*   method __get_int(prompt, lo, hi)
    *   takes a prompt string as parameter
    *   prompt user for integer input
    *   repeat prompt until input is integer and within bounds

*   method __print_card()
    *   prompt user for card ID
    *   Loop through card container 
    *   Print ID of card from card container

*   method __save_deck()
    *   prompt user for file to save to
    *   open file
    *   Loop through card container
    *   print each card to the file
    *   close file
    *   print success message



### `RandNumberSet` class

The requirements for Cards are strict and require careful consideration to get right.  After going back and forth on this, it has been decided to keep the Bingo Card as simple as possible by treating it as a simple 2D array of numbers.  The complex logic needed to fill it in correctly will be sequestered into this class.

One requirement on `Card`s is that no number can be duplicated on a `Card`.  The most elegant solution we can come up with is to make one list of numbers running from 1 to the maximum number on the `Card`, and to shuffle it like a deck of cards, then draw numbers from the top until the Bingo `Card` is filled.  This requirement only holds within one `Card`: it is okay if the same number is shared among `Card`s within the `Deck`.

There is a requirement that numbers within columns of the Bingo `Card` be drawn from increasing subsets of numbers such that the leftmost column contains the smallest numbers, and increase toward the right side of the `Card`.  These subsets cannot overlap.  This seemed difficult at first, but is easily solved by dividing the `Card` into $N$ segments, and applying the "shuffle a set of numbers" idea to each segment individually.

*   Thus, the `RandNumberSet` will support a public `shuffle` operation which shuffles each segment and resets the object so that a new `Card` can be created.
    *   Reusing the object will conserve resources in the computer
*   Numbers for an entire row of a `Card` will be provided by the public `next_row()` method.
    *   The `RandNumberSet` will have a private data member `nRowPos` which keeps track of which row is the next to be returned by `next_row()`
*   The `RandNumberSet` constructor will need to know the size of `Card` it is being used to create (so it can know how many segments to divide its numbers into), as well as the maximum number that may appear on the card.
    *   This class relies on its caller to validate its input.
*   The `Card` size, maximum number and array of segments are stored in private members.
*   For testing purposes, `operator<<` will be overloaded to enable programmers to get a look at this object
*   The size of the `RandomNumberSet` is defined to be the size of the `Card` it can create.  This value will be given by the public `size()` method.
*   A specific row of Bingo numbers can be accessed by `operator[]`


### `Deck` class

This class is essentially a container of `Card` objects (kinda like real life!).  Will possibly use a plain array, since the size of the `Deck` is known at the time of initialization.

The constructor will create each `Card` it will contain.  It will initialize a `RandNumberSet` to help with this process.  The constructor will take these parameters:

*   `int card_size` - the size of a `Card`, from 3 to 16
*   `int num_cards` - number of cards in the `Deck`, from 2 to 8192
*   `int max_num` - the highest number that may appear on a card, needed by the `RandNumberSet`

The usual assortment of public methods/overloads will be provided:

*   `__len()_` returns the number of `Cards` contained within
*   `__getitem_()` returns a specific `Card`
*   `__size_` prints each `Card` in the `Deck`.  This method will rely on the `Card` object also overloading `operator<<`


### Layton's Plan for Deck

*   Constructor
    *   Create a list to hold the Card objects/instances
    *   Create a RandNumberSet object taking the parameters passed into Deck: card_size, num_cards and max_num
    *   Iterate `num_cards` times
        *   Create an instance of Card 
        *   Append the Card to the container

*   __len_ function: None
    *   return the length of the deck

*   __getitem_ function: None
    *   return the specified card to the console

*   __str_ function: None
    *   Prints each card to the screen


### `Card` class

This object will have private data members to hold:

*   `int id` - the `Card`'s ID number, needed when it prints itself out
*   `int size` - the number of rows in the `Card`, needed when determining whether the center square is **Free**
*   `int rows[][]` - the 2D array that holds on the numbers
    *   The **Free** square will contain a negative value; when the Card is printed the string `"FREE!"` will be printed instead.

All of the interesting work of instantiating this object is handled by the `RandNumberSet`.  The algorithm for creating the card goes like this:

```
0.  Shuffle the RandNumberSet to ensure that fresh numbers are at the top
1.  Until the card is full
    *   Grab the next row of numbers from the RandNumberSet
    *   Copy into the Card
2.  If the size of the Card is odd, replace the center square with the value `-1` to represent **Free**
```

*   A public `id()` method provides read-only access to the private `id` member
*   `int number_at(row, col)` returns the number stored at cell `(row, col)`

The usual assortment of public methods/overloads will be provided:

*   `size()` returns the size of the `Card`
*   `operator<<` prints the `Card`.
    *   The ID # of the card is displayed above the `Card` itself
    *   ASCII-art rows and columns are drawn with dashes `-`, plus signs `+` and pipes `|`, according to the requirements
    *   Each number is centered within its cell
    *   It is easy to print the card to the screen or to a file by directing the output to `STDOUT` or to a file stream object.
   

### Layton's Plan For Card

*   Constuctor - Initialize a Bingo Card
    *   set `idnum` to self
    *   set `ns` to self
    *   Shuffle the RandNumberSet 
    *   loop through the length of the RandNumber Set
        *   Until the card is full
            *   Grab the next row of numbers from RandNumberSet
            *   Copy the row into the Card
        *   if the card is even, put a negative one integer in the middle

*   `id` function: None
    *   return the id of the card - this is the position of the card within `ns`

*   `number-at` function: None
    *   returns value of the square of (row, col) on bingo card

*   `__len_` function: None
    *   returns length of one of the dimensions of the card

*   `__str_` function: None
    *   Print the column letters
    *   Loop through the lines of the card 
        *   Print `+-----` * n (n being the number of letters in the column)
            * Except for the last letter - print `+-----+`
        *   printing the value inside the `|   |`
    *   return the bingo card



## Phase 3: Implementation 

*   I changed a lot of my loops to while loops in the function
*   I changed the card list in Card to private and made a method that returns an list of all the sublists combined
*   Most of the logic that I had was right, I just needed to tweek it so that it worked
*   I learned how to unit test
*   I was really surprised when my menu options finally came through and started working
*   I There was a lot of 'out of index errors' that I had to fix
    *   This was relatively easy, just following the trail of errors
*   I forgot about on of the hints in the hint.md file that ended up being super helpful


## Phase 4: Testing & Debugging 

*   I ran the command python src/bingo.py
*   I tested running the program from the very beginning to make sure that I was getting the correct prompts and values
    *   Bugs
        *   Traceback (most recent call last):
    File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn4\src\bingo.py", line 32, in <module>
        UserInterface().run()
    File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn4\src\UserInterface.py", line 69, in run
        self.__create_deck()
    File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn4\src\UserInterface.py", line 96, in __create_deck
        userDeck = Deck(card_Size, number_Of_Cards, max_Size)  # Creates the deck based on user input
    File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn4\src\Deck.py", line 40, in __init__
        bingoCard = Card(i, bingoCardNumSet)
    File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn4\src\Card.py", line 46, in __init__
        self.bingoCard[i] = ns.next_row()
    IndexError: list assignment index out of range
    *   Cause   
        *   I was tyring to access an index of the empty list 
    *   Remedy
        *   I used the .append() to add to the list

*   I simplified my code intentionally so that it would not do everything that I need it to do and I realized that there were two of the same number in the randNumberSet
    *   python src/bingo.py is the command I ran
    *  I printed out a row of the randNumberSet using the next_row() method and put another print statement in 
    *   '''[2, 10, 19]
            Hello
            [6, 12, 18]
            Hello
            [1, 13, 16]
            Hello
            [1, 12, 16]
            Hello
            [7, 8, 19]
            Hello
            [3, 10, 18]
            Hello
            [6, 14, 17]
            Hello
            [4, 10, 15]
            Hello
            [5, 12, 19]
            Hello'''
    *   Cause
        *   I had a off by one error that was causing this
    *   Remedy
        *   I removed the shuffle() from Card.py and it eneded up printing the same thing three times

    *   I ran even versus odd cards to make sure that the "FREE!" square ended up just in the middle of the odd cards


*   I continually ran test that gave me an off by one error. The error was looping over the deck twice, one in the deck and t he card file.
    *   I ran python src/bingo.py

*   There were  a lof of formatting errors when trying to print out the card, like the letters being print out line by line instead of on the same line. 
    *   The fix to this was putting new line characters in the right places.

*   I also had the __str_() method directly printing instead of returning a string
    *   I made a string that the output was continually made from a string.

    ### My Unit Tests

#### Cards
*   I created a list of cards (1-5)
    *   Checked to make sure their ID's matched
    *   Checked that their sizes matched
    *   Checked that the FREE! value was on the odd cards in the middle
    *   Checked that there were no duplicates on the card

### Deck
*   I created three decks
    *   Sizes
        *   7
        *   16
    *   Number of cards
        *   2
        *   16
        *   8192

*   I tested length
*   Tested getting items were the same

*   I ran python src/runTests.py to run the tests


## Phase 5: Deployment *(5%)*
*   Verified


## Phase 6: Maintenance

*   The parts of my program that are sloppily written is the card and deck classes. I coule have made more getter and setter methods, making more of the attribute private and harder to access.
    *   This means that a user can potentially delete parts of the bingo card directly where as they should not have access to any of the attributes beside what is prompted in the menu.   
    *   I am still not quite sure how the randNumberSet works because I did not really go line over line looking what it did.
        *   The varibale names were also really hard to understand because of all the underscores and double underscores.
        *   If a bug gets reported, I believe it will be relatively easy to find because the classes depend on eachtother and I could just trace the bug back.
    *   My documentation will make sense to other people besides me bause I looked at the C++ plus and translated it into my own words so I could understand it more.
    *   I think my documentation might not make sense to me in six months because of all the weird naming conventions used in this project. I think I could understand it after reading over it multiple times, but not the first time over.
    *   Adding a new feature will be relatively easy because my code is decently written and easy to understnad. The parts work together well and adding a new feature would be easy to integrate.
    *   After upgrading the hardware, I think that my program would still work well and up to the standard.
    *   After upgrading the operating system, I think that my program might have a decent chance of working well because it does not take any command line arguments and is just an interactive program designed to print out bingo cards.
    *   I think that if the next version of python came out, that my program would work well except if something was changed in the way python stores variables or how it works. But overall, the ocde is simple and easy to understand.
