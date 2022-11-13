# Code Smells Report - 5.0

## Code Smells

### Magic numbers
*   mbrot_fractals - line 115 - 117
*   '''
    z = 0  	    	       
    seven = 7.0  	    	       
    TWO = 2  
    '''
*   This code is a problem because it does not provide any context as to what those varibale names mean and represent. They are quite literally the numerical words for the numbers. This does not provide any context to help the person figuring out what the code means.
*   I could rename these variables with names so that they are more meaningful and provide more context

### Global Varibale
*   Phoenix_fractal.py - line 71 - right below getColorFromPallette function
    *   `global grad`
    *   This is a global variable. This is a problem because this could lead to side effects that are really difficult to detect and trouble shoot
    *   To fix this, I could pass the variable to the function as an argument rather than making it global

###   Poorly Named Variables
*   Main.py - line 91 - in the `# figure out if the comand line argument is one of the known fractals` section
    *  ` iter = 0 `
    *   `i = 0`
    *   These are obviously some kind of iteration varibale, but it is not extremely clear what they are really doing and why
    *   Rename this so it is more clear 
        *   Add a comment next to it to clarify why it represents zero

###   Comments that share too much information
*   mbrot_fractal.py
*   '''
            def pixelsWrittenSoFar(rows, cols):  	    	       
                pixels = 0  	    	       
                for r in range(rows + 1):  	    	       
                    pixels = pixels + cols  	    	       
                print(pixels, "pixels have been output so far", file=sys.stderr)  	    	       
                return pixels  	    	       



            These are the different views of the Mandelbrot set you can make with this  	    	       
            program.  	    	       
                            
            For convenience I have placed these into a dictionary so you may easily  	    	       
            switch between them by entering the name of the image you want to generate  	    	       
            into the variable 'image'.`
        '''

*   This code smell is a problem because it is too long of a comment and does not get right to the point. Not to mention that the comment actually has python code in it or near python code. It could also just confuse the reader more. Also, there's really no point in having python code in the comment if it is written just above or below (this is repetitive)
*   I could fix this by rewriting the description that it states the input(arguments) the output and what it is generally meant to do without writing any python code or anything similar.

### Comments that lie
*   Phoenix_fractal.py - line 109-122 - is the getFractalConfigurationDataFromFractalRepositoryDictionary function
    * def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):  	    	       
            """Make sure that the fractal configuration data repository dictionary  	    	       
            contains a key by the name of 'name'  	    	       

            When the key 'name' is present in the fractal configuration data repository  	    	       
            dictionary, return its value.  	    	       

            Return False otherwise  	    	       
            """  	
            '''    	       
            for key in dictionary:  	    	       
                if key in dictionary:  	    	       
                    if key == name:  	    	       
                        value = dictionary[key]  	    	       
                        return key  
            '''
    *   This is bad because the description does not  match the code. It says that it returns false otherwise, but obviously there is no return false statement in the line of code. This is missleading and could lead to a lot of confusion
    *   What I could do to fix it is either take out the returns false description or change the code to match the description

### Too Many Arguments
 *   mbrot_fractal.py - line 251 - the pixelsWrittenSoFar function
    *   '''
        def pixelsWrittenSoFar(rows, cols):  	    	       
            portion = (512 - rows) / 512  	    	       
            pixels = (512 - rows) * 512  	    	       
            status_percent = '{:>4.0%}'.format(portion)  	    	       
            status_bar_width = 34  	    	       
            status_bar = '=' * int(status_bar_width * portion)  	    	       
            status_bar = '{:<33}'.format(status_bar)  	    	       
            # print(f"{pixels} pixels have been output so far")  	    	       
            # return pixels  	    	       
            # return '[' + status_percent + ' ' + status_bar + ']'  	    	       
            return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
        '''
    *   This is bad because the `cols` variable is passed into the function but never used. This is just taking up space and creating more confusion about what is needed for the function to work.
    *   What I could do is remove the `cols` variable from the function arguments because it is not being used within the function

### Function/Method that is too long
*   phoenix_fractal.py - lines 128 - 211
*   `def makePictureOfFractal(f, i, e, w, g, p, W, s):`
    *   I am not putting the entire code here because it is really long.
    *   The point is that this function is too long
*   This is bad because the function can easily become too confusing and complex for someone to understand as well as fix. This also adds to the chance that this function will cause errors that will be hard to find and fix and reimplement.
*   I can break this up into at least 2 seperate functions that can be used and made simplier to avoid the chances that an error is caused.


### Complex Decision Trees
*   mbrot_fractal.py - lines 154 - 205
*   '''
    def colorOfThePixel(c, palette):  	    	       
        """Return the color of the current pixel within the Mandelbrot set"""  	    	       
        global z  	    	       
        z = complex(0, 0)  # z0  	    	       

        global MAX_ITERATIONS  	    	       
        global iter  	    	       

        len = MAX_ITERATIONS  	    	       
        for iter in range(len):  	    	       
            z = z * z + c  # Get z1, z2, ...  	    	       
            global TWO  	    	       
            if abs(z) > TWO:  	    	       
                z = float(TWO)  	    	       
                # XXX: the program used to crash with the error  	    	       
                #   TypeError: 'int' object is not callable  	    	       
                #  	    	       
                # maybe it had something to do with 'len' being an integer variable  	    	       
                # instead of a function variable.  	    	       
                # Somebody from StackOverflow suggested I do it this way  	    	       
                # IDK why, but it stopped crashing, and taht's all that matters!  	    	       
                import builtins  	    	       
                len = builtins.len  	    	       
                if iter >= len(palette):  	    	       
                    iter = len(palette) - 1  	    	       
                return palette[iter]  	    	       
            elif abs(z) < TWO:  	    	       
                continue  	    	       
            elif abs(z) > seven:  	    	       
                print("You should never see this message in production", file=sys.stderr)  	    	       
                continue  	    	       
                break  	    	       
            elif abs(z) < 0:  	    	       
                print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	    	       
                sys.exit(1)  	    	       
            else:  	    	       
                pass  	    	       

        # Code borrowed from StackOverflow, comment copied from above  	    	       
        #  	    	       
        # XXX: the program used to crash with the error  	    	       
        #   TypeError: 'int' object is not callable  	    	       
        #  	    	       
        # maybe it had something to do with 'len' being an integer variable  	    	       
        # instead of a function variable.  	    	       
        # Somebody from StackOverflow suggested I do it this way  	    	       
        # IDK why, but it stopped crashing, and taht's all that matters!  	    	       
        import builtins  	    	       
        len = builtins.len  	    	       
        if iter >= len(palette):  	    	       
            iter = len(palette) - 1  	    	       
        return palette[iter]  # The sequence is unbounded  
    '''
*   This has a lot of problems built into it. First, it could also fall under the too long of function or method code smell, but I think that it is highly relevant to the too complex logic tree code smell. The code has too many indentations using the `if` or `else`keywords and could very well be simplified.
*   This is a problem because there are too many places for the code to encounter and error and the logic is made too complex when it could be simplified and made easier to understand.
*   I can go through this and simplify the code so that it does not use the amount of conditional statements that it is currently using.
    *   I can combine them into one statement rather than multiple or rearragne the code.

### Spaghetti Code
*   main.py - lines 86 - 126 figures out if the command line argument is one of the known fractrals
*   '''
    if not arg_is_phoneix and sysargv1_not_mndlbrt_frctl == 0:  	    	       
        print("ERROR:", sys.argv[1], "is not a valid fractal")    #  	    	       
        print("Please choose one of the following:")             ###  	    	       
        quit = False                                           #######  	    	       
        next = ''                                              #######  	    	       
        iter = 0                                                #####  	    	       
        while not quit:                             #     ## ########### ###  	    	       
            next = PHOENX[iter]                      ### #################### ## #  	    	       
            print("\t%s" % next)                      ###########################  	    	       
                                                # ############################  	    	       
            if PHOENX[iter] == 'shrimp-cocktail': ################################  	    	       
                break                            ####################################  	    	       
                                #    ## #       ###################################  	    	       
            else:               ##########     ######################################  	    	       
                iter += 1     ##############   ####################################  	    	       
                        ########################################################  	    	       
                ######################################## CODE IS ART #########  	    	       
                        ########################################################  	    	       
        exit = None          ############################## (c) 2022 #############  	    	       
        i = 0                 ##############   #####################################  	    	       
        i = 0                   ##########     ####################################  	    	       
        fractal = ''            #    ## #       ####################################  	    	       
                                                #################################  	    	       
        while not exit:                          ################################  	    	       
            print("\t" + MBROTS[i])               #  ############################  	    	       
            if PHOENX[iter] =='shrimp-cocktail':    ######################### ####  	    	       
                if MBROTS[i]  == 'starfish':       ### #  ## ##############   #  	    	       
                                                #             #####  	    	       
                    i = i + 1                                  #######  	    	       
                    exit = PHOENX[iter] =='shrimp-cocktail'    #######  	    	       
                    i -= 1 #need to back off, else index error   ###  	    	       
                    exit = exit and MBROTS[i]  == 'starfish'      #  	    	       
            i = i + 1  	    	       
        # return 1  	    	       
        sys.exit(1)  	    	       
    else:  	    	       
        # Otherwise, quit with an error message to help the user learn how to run it  	    	       
        pass  	    	       
        fratcal = sys.argv[1]  	    	       
    #else:  	    	       
        # the fractal name is the 1st argument after the program name  	    	    
    '''
*   This code is bad because it uses double negatives and quite literally code vomits. This makes errors prone to occur and the reader very confused on what is happening. This also uses arguments in a weird way and does not clearly deifne what is happening. The description of the section of code makes it seem like it should just be a couple lines of code instead of that many.
*   I could reduce it so that it does not need to be that many lines and uses the arguments in a more efficient way. I could write it so that there is not a vomit of code written and rather actually makes sense as to what is going on.

### Redundant Code
*   mbrot_fractals.py - line 279 - the images dictionary
*   '''
    'spiral1': {  	    	       
            'centerX': -0.747,  	    	       
            'centerY': 0.1075,  	    	       
            'axisLen': 0.002,  	    	       
            },  	    	       

        'seahorse': {  	    	       
            'centerX': -0.748,  	    	       
            'centerY': -0.102,  	    	       
            'axisLen': 0.008,  	    	       
            },  	    	       

        'spiral1': {  	    	       
            'centerX': -0.747,  	    	       
            'centerY': 0.1075,  	    	       
            'axisLen': 0.002,  	    	       
            },  	    	      
    '''
*   The fact that spiral1 is in the dictionary twice is bad because it just takes up extra space and can confuse someone who is not paying super close attention to every name. This also just takes up more space and makes the code more confusing and serves no real purpose to the program besides wasting space and time writing it and in all honesty, I am unsure how it is even in the dictionary twice.
*   I could remove the redundant code so that there is only on occurance of the key in the dictionary.

### Dead Code
*   phoenix_fractals.py
*   '''
    ## This is some weird Python thing... but all of the tutorials do it, so here we go  	    	       
    # if __name__ == '__main__':  	    	       
    #    # Process command-line arguments, allowing the user to select their fractal  	    	       
    #    if len(sys.argv) < 2:  	    	       
    #        print("Please provide the name of a fractal as an argument", file=sys.stderr)  	    	       
    #        for i in f:  	    	       
    #            print(f"\t{i}", file=sys.stderr)  	    	       
    #        sys.exit(1)  	    	       
    #  	    	       
    #    elif sys.argv[1] not in f:  	    	       
    #        print(f"ERROR: {sys.argv[1]} is not a valid fractal", file=sys.stderr)  	    	       
    #        print("Please choose one of the following:", file=sys.stderr)  	    	       
    #        for i in f:  	    	       
    #            print(f"\t{i}", file=sys.stderr)  	    	       
    #        sys.exit(1)  	    	       
    #  	    	       
    #    else:  	    	       
    #        fratcal_config = getFractalConfigurationDataFromFractalRepositoryDictionary(f, sys.argv[1])  	    	       
    #        phoenix_main(fratcal_config)  	    	     
    '''
*   This code is a problem because it is dead, it is commented out and does not serves any purpose for what the program is doing. This block of obselete code does not actually do anything when the code it ran and executed.
*   I could fix this by removing all the obselete code from the programs so that it looks cleaner and easier to read.