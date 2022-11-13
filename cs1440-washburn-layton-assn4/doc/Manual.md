# Bingo! User Manual  	         	  

## Running The Program

*   The User should type the following 'python src/bingo.py' in into their terminal from the project's directory to run the bingo program.


## Menu And Functionality

*   There are two menus

    *   Main menu
        *   This is the menu the User will see after running the program
        *   The User will be prompted with Two options to choose from
            *   User will see the Create a new deck prompt
                *   User will see the prompt 'C - Create a new deck'
                    *   To create a new deck type 'C' or 'c'
                    *   Does not matter if 'C' is uppercase or lowercase
                *   After the user types 'C' or 'c' hit enter
                *   This will bring the User to a series of prompts asking them to create a deck (This is the Deck Creation Process)
                    *   Prompts User for the size of the card
                        *   The User will see a message saying that the appropriate input ranges from 3 to 16
                        *   User will be prompted to Enter the desired size of card
                        *   User should hit enter after inputting size of card
                        *   User will see the prompt repeated until a valid input has been entered
                    *   Prompts User for the number of cards in the deck
                        *   Displays a message sayinf the appropriate input ranges from 2 to 8192
                        *   Enter the desired size of card and hit enter
                        *   User will see the prompt repeated until a valid input has been entered
                    *   The user will then see the Deck Menu pop up

            *   Exit the program
                *   To exit the program type 'X' or 'x'
                    *   Does not matter is 'X' is uppercase or lowercase
                *   After typing 'X' or 'x' hit enter
                *   The program will exit after hitting enter

    *   Deck Menu
        *   The User will see three options
            *   View their cards
                *   Shows a list of all the cards
                    *   Prompts User to Print all cards or a singular card
                        *   User will see the Bingo cards printed out one right after the other to the console
                        *   User will be prompted to input which card they want to print out
                            *   User will see desired Bingo card printed out to the console
                            *   User will see the prompt repeated until valid input is given
            *   Save the Deck to a file
                *   The User will see a prompt asking where the User wants to save the deck
                    *   The User will enter a file name/directory/path and hit enter
                        *   After hitting enter, the User will see a message saying that the deck was saved to the file
                    *   The User will see the prompt repeated until correct input is given
            *   Return to Main Menu
                *   The user will see a message asking them if they want to return to the main menu
                    *   A prompt with two options will be given
                        *   Y or N
                            *   User will hit 'Y' or 'y' to return to main menu
                                *   User will see prompt repeated until correct input is given
                            *   User will hit 'N' or 'n' to return to the Deck Menu
                                *   User will see prompt repeated until correct input is given


## Common Errors and How to Fix Them
*   User may encounter the prompts being repeated 
    *   User should verify their input is correct
        *   Common mistakes that cause the prompt to be repeated
            *   The prompt asks for an integer and an integer is not given
            *   The prompt asks for an integer within certain ranges and the integer inputted is outside the range
*   User recieves a defualt error messages from Python
    *   User should check that the file they entered is correct and a valid, exsisting file
    *   User typed the wrong name when running the program
        *   User should verify that they are typing in 'python src/bingo.py' into their terminal to run the program


