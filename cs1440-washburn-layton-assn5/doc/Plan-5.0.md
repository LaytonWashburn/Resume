# Software Development Plan

## Phase 0: Requirements Specification 

### Instructions in My Own Words
*   Rewrite/Refactor the program into a clean and easy to understand program
    *   All code smells should be removed
        *   Redundant code
        *   Useless code
        *   Confusing code
        *   Could be simplified code
        *   etc...
    *   Organize the program into six modules
        *   main.py
        *   FractalInformation.py
        *   Mandelbrot.py
        *   Phoenix.py
        *   Palette.py
        *   ImagePainter.py
*   Write a User Manuel
    *   Short but concise
*   Create  a UML
    *   Shows how everything is connected
*   Improve and write Unit Tests
    *   Write and refactor the unit test so they go through the program thoroughly.


### Things I already know how to do
*   I know how to change variable names and delete code that is useless.
*   Condense code
*   Put code that is similar into the modules
*   Import a module into another one to use
*   Create UML
*   Create a User Manuel
*   How to work with dictionaries
*   Check input from the command line


### Things I Do Not know how to do
*   Read through someone's messy code and understand everything
*   Understand fractals
*   Draw UMLs for someone else's messy code
*   Unscramble code


## Phase 1: System Analysis 

*   Input from the command line
    *   A string that clarifies what picture to draw
*   The Output will take the form of a picture(.png) file saved to the directory
    *   There is also checking to make sure that the amount of arguments given over the command line are enough and if not then exit the program.
        *   The output is a a 640x640 pixel sized photoImage canvas that has different colors calculated with numbers.
        *   It is a photoImage canvas
        *   In a TKinter window

*   There will be a function that determines the color of the pixel
*   A paint function that paints the fractal image on the TKinter PhotoImage canvas
*   A function that sets up the fractal image and the GUI
*   A color that gets the color from the palette
*   A function that makes sure that the data is stored correctly and returns values.

*   There is a formula which calculate what color the pixel needs to be and where it is in accordance with the grid. It uses rational and imaginary numbers to perform the caluclations as well as utilizing a color palette.  



## Phase 2: Design

###   main.py
'''
    if len(sys.argv) is less than 2:  	    	       
        print error message saying not enough arguments to console	    	        	    	        	    	       
        loop through the known fractals dictionary  	    	       
            print fractal (key) to console  	    	       
        gracefully exit the program  	    	        	    	       

    if the second command line argument is not in the dictionary of known fractals
        print error message stating the input was not a known fractal to console      	    	       
        print message to console saying to choose on of the following 
        loop through the dictionary keys of known fractals
            print key name to the console
        gracefully exit the program
                                    
    assign the second command line argument to the variable 'fractal'  	    	       
    call the 'makeFractal' method from the ImagePainter module passing in the data for the fractal from the dictionary 
'''

###   FractalInformation.py
'''
create a dictionary with the name allFractalNames, with the folllowing data fields
    key: Name of fractal
        centerX: int
        centerY: int
        axisLen: int
        type: String
        name: String
'''

###   Mandelbrot.py
'''
create method named mandelbrotMainDriver taking a complex number as the parameter	    	         	    	 	      
    set/initialize a variable named 'newComplex' equal to a  complex number parts 0 real, 0 imaginary    	       
    set/initailize a variable named 'maxIterations' equal to 111 (the size of the mandelbrot color palette)	    
     	       
    Loop the number of times 111 ('maxIterations' variable) with an iteration variable named 'iter'     	       
        set varibale named 'newComplex' equal to 'newComplex' times 'newComplex' plus 'complexNumber' 	    	       	    	       
        if absolute value of the variable 'newComplex' is greater than 2  	    	       
            assign the varibale 'newComplex' equal to the typecasted float value 2     	         	    	         	    	       
            return varible 'iter' which is the current iteration of the loop
    return variable 'maxIterations' minus 1

'''

###   Phoenix.py
'''
create method named 'phoenixIterationCounter' parameters a complex number named 'complexNumber'  	    	       
 	set/initialize a variable named 'juliaConstant' equal to the value of the complex number 0.5667 real, 00 imaginary	    	       	       
    set/initialize a variable named 'pheonixConstant' equal to the value of the complex number -0.5 real, 0.0 imaginary  	    	              
    set/initialize a variable named 'compflipped' equal to the value of the complex number variable 'complexNumber.imag', 'complexNumber.real' this flips the values  	    	       
    set/ initialize a varibale named 'zPrev' equal to  0 part real 0 imaginary  	    	        	    	       
    set/ initialize a varibale named 'maxIterations' equal to the numerical value of 102 which is the size of the Phoenix color palette  	    	       
    loop through the size of the phoenix color palette with the variable named 'iter' as the variable	    	       
        set/initialize the variable named 'zSave' equal to the variable named 'compflipped' variable     	             
        set the varibale named 'compflipped' equal to the varibale 'compflipped' times 'compflipped' plus 'juliaConstant' plus the sum of  'pheonixConstant times 'zPrev'	       
        set variable named 'zPrev' equal to  'zSave' variable   	    	       
        if the absolute value of the variable 'comflipped' is greater than the numerical value of 2:  	    	       
            return the variable named 'iter'     	            	              
    return the variable named 'maxIterations' minus the numerical value of 1
'''


###   Palette.py
'''
create a list named 'mandelbrotcolorPalette' with all the associated colors inside.
There should be 111 colors

create a list named 'phoenixColorPalette' with all the associated colors for the phoenix fractals inside
There should be 111 colors
'''

###   ImagePainter.py
'''
create method named 'makeFractal' with the parameters 'fractal' variable which is the data in from in the dictionary  	    	       
    	       
    set/initialize a varible named 'screenSize'  equal to the numerical value of 512
    
    print rendering message to the conosle with the fractal name in the message  	    	       
    set/varible 'before' equal to the time module's time method  	    	         	    	       
    set veriable 'window' equal to a TKinter window  	    	       
    create a varibale named 'img' equal to a PhotoImage object with the dimensions with width equal to screenSize (512), height equal to screenSize(512))  	    	        	    	       
     	    	       
	    	       
    set/initialize a variable 'minx' equal to to the fractal's 'centerX' data field minus the fractal's 'axisLen' data field divided by 2.0  	    	       
    set/initialize a variable 'maxx' equal to fractal's data field'centerX'  plus the fractal's data field 'axisLen' divided by 2.0)  	    	       
    set/initialize a variable 'miny' equal to the fractal's data field 'centerY' minus the fractal's 'axisLen' divided by 2.0)  	    	       
    set/initialize a variable 'maxy' equal to fractal's data field 'centerY' plus the fractal's data field 'axisLen' divided by 2.0)  	    	       

        	       
    create/ initialize the varibale 'canvas' equal to a  Canvas object with the parameter s 'window', 'width equal to screenSize', ;height equal to screenSize', 'bg' equal to the color'#000000' (Dark grey, almost black)  	    	       
    pack the canvas object  	    	       
    call the canvas object's create_image method with the parameters 'screenSize divided by 2', 'screenSize divided by 2', 'image' equal 'img', 'state equal to "normal"  	    	       

     	       
    set/initialize variable 'pixelsize' equal to the absolute value of 'maxx' minus 'minx' divided by 'screensize' 

    set/initialize varibale 'portion' equal to the numerical value of 0  	    	       
    set/initialize variable 'total_pixels' equal to 'screenSize squared'  	    	       
    Iterate over the range of the 'screenSize' stepping down one eachtime until 0 	    	       
        create 'cc' equal to an empty list  	    	       
        iteratie over the 'screenSize' using the variable 'col'    	       
            set the variable 'x' equal to  'minx' plus 'col' plus 'pixelsize'  	    	       
            set 'y' equal to 'miny' plus 'row' multiplied by 'pixelsize'
            if the fractals' data field is equal to the String 'phoenix'     	       
                set 'index' equal to the method call phoenixIterationCounter parameters complex(numerical values 'x', 'y' 
                append the color based on the index to the 'cc' list   	  
            else
                set 'indexToColor'  equal to the method 'mandelbrotMainDriver parameters complex number 'x', 'y'  	    	       
                append the madelbrot color to the 'cc' list  
                
        call the 'img's'  put method with parameters (String, 'cc' lists, and String size  	    	       
        the window object's update method  	    	       
        portion = screenSize - row / screenSize  	    	           	       
        print(pixelsWrittenSoFar(row), end='\r', file=sys.stderr)    	

  	    	       
    set 'after' equal to the time module's time method   	    	       
    print a message saying done with the amount of time it took 	    	       
    call the 'img's' write method with the fractal's name and a .png on the end  	    	       
    print a message saying wrote the picture  	    	       	    	       
    print a message to the console telling them to quit the program by exiting the TKinter's window
    call the mainloop method so that the window stays open 
    
create a method called 'pixelsWrittenSoFar' with the parameters 'rows'
    set/initialize the variable 'screenSize' equal to the numerical value of 512  	    	       
    set/initialize the varaible 'portion' equal to the  'screenSize' minus 'rows' divided by 'screenSize'  	    	       
    set/initialize the variable 'pixels' equal to 'screenSize' minus 'rows' multiplied 'screenSize'  	    	       
    set/initalize the variable the varibale 'status_percent equal to a String for the status bar	    	       
    set/initialize the varibale the 'status_bar_width' eqaul to the numerical of 34  	    	       
    set the variable 'status_bar'  equal to the symbol '=' mulitpied by the variables typecaste to int 'status_bar_width multiplied by 'portion'   	       
    set the variable 'status_bar' equal to a formatted string 	    	        	    	       
    return a String of '=' symbols

'''

## Phase 3: Implementation

*   When writing the code, I was very surprised to see how many lines I could plainly take out without affecting the program. I would take out a couple lines of code and then find out that it did not affect the program at all.
*   Things that didn't go according to plan was the fact that I did not see the requirements until I had already started implementing code. So I had to go back and rewrite my documentation and what each module had and needed.
*   I think this project would have been significantly easier if I had started much earlier. A lot of my problems could have been avoided with more time.
*   I could get rid of global variables by passing them as parameters rather than using the global keyword.
*   How effective unittest actually are in finding bugs in the program.
*   I did not realize how effective UMLs are in putting the modules/classes relationships together. It really helps visualize what is going on.
*   Somethings that I deviated from in my original plan was how I got the iterations for the loops in Phoenix.py and Mandelbrot.py. I had to go back and change it so that the methods took more parameters and did not have magic numbers.


## Phase 4: Testing & Debugging 

*   Traceback (most recent call last):
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\main.py", line 81, in <module>
    if not arg_is_phoneix and sysargv1_not_mndlbrt_frctl == 0:
NameError: name 'arg_is_phoneix' is not defined
*   I tried to run the command 'python src/main.py phoenix' and it threw this error
*   This was attempting to draw a fractal
*   I fixed this by removing and renaming variable (specifically the arg_is_phoenix)

*     File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\main.py", line 106, in <module>
    makeFractal(allFractalNames[fractal])
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\ImagePainter.py", line 11, in makeFractal
    print("Rendering {} fractal".format(fractal['name']), file=sys.stderr)
NameError: name 'sys' is not defined
*   I think I ran something like 'python src/main.py spiral0
*   I accidentally changed the import statement for the sys module

*   Rendering leaf fractal
Traceback (most recent call last):
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\main.py", line 106, in <module>
    makeFractal(allFractalNames[fractal])
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\ImagePainter.py", line 13, in makeFractal
    before = time.time()
NameError: name 'time' is not defined
*   I ran 'python src/main.py leaf' 
*   I forgot to import the time module into ImagePainter.py
*   I coded in the import statement

*   Traceback (most recent call last):
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\main.py", line 106, in <module>
    makeFractal(allFractalNames[fractal])
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\ImagePainter.py", line 15, in makeFractal
    window = Tk()
NameError: name 'Tk' is not defined
*   I ran 'python src/main.py mandelbrot'
*   I tried to run the mandelbrot fractal
*   I forgot to import the correct methods from TKinter
*   I coded in the appropriate methods from TKs

*   Rendering spiral0 fractal
Traceback (most recent call last):
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\main.py", line 78, in <module>
    makeFractal(allFractalNames[fractal])
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn5\src\ImagePainter.py", line 50, in makeFractal
    cc.append(mandelbrotcolorPalette[indexToColor])
IndexError: list index out of range
*   I ran 'python src/main.py spiral0'
*   I tried to have the program paint the spiral0 fractal
*   This was due to me not using the correct iterations and an off by one error
*   I changed the amount of times the loop would iterate

*   Rendering phoenix fractal
    [100% =================================]
    Done in 2.255 seconds!
    Wrote picture phoenix.png
    Close the image window to exit the program
*   While this might look right, the fractal was not the same as the original which mean that something was off
*   I ran 'python src/main.py phoenix'
*   I tried to have the program make the phoenix fractal
*   This error was due to me not using the correct variables in the phoenix fractal calculations.

### Unit Tests

#### Mandelbrot Tests
*   test_iterationCounter
    *   Tests to make sure that given a complex number, mandelbrotIterationCounter returns the correct iteration integer

*   test_ImagePainter_pixelsWrittenSoFar
    *   Tests to make sure that when given the a row (int) that the correct status bar is returned

*    test_palleteLength
    *   Ensures that the mandelbrot Palette is the correct length

*   test_Palette_Colors
    *   Ensures that when a element of the mandelbrot Palette is accessed, the right color is returned

#### Phoenix Tests
*   test_PhoenxIterationCounter
    *   Ensures that the correct number is returned when the PhoenixIterationCounter method is given a complex number

*   test_Dictionary_Names
    *   Makes sure that the dictionary names can be correctly accessed and contains the correct keys

*   test_Phoenix_Palettelength
    *   Ensures that the Phoenix color palette is the correct length

*   test_PhoenixColors
    *   Ensures that the correct color is returned when accessing a specifc element of the Phoenix color palette

## Phase 5: Deployment 

* verified and works like it is suppose to.


## Phase 6: Maintenance

*   I think that the ImagePainter.py is sloppily written. There is undoubtedly a better way to this instead of the way I implemented.
    *   I am not quite sure how the complex numbers work and what is really happening inorder to get each fractal painted a certian color.
    *   I think it would be hard to find a bug if it had to do with the computations, but if it was almost anything else, I think that it would be relatively easy. Each module is small and would not take long to find the source of error in the code.
*   My documentation should make sense to other people besides myself. I also think that my documentation should still make sense after 6 months because the program is realitively small and not complex.
*   It would be really easy to imlement a new feature into the program because of how simple the code is right now. There is not a lot of extra work going on so adding a new feature should be easy.
*   If my computer's hardware got upgraded, the program should still work fine.
*   If the operating system got upgraded, it should still be fine as long as the way python functions on the machine is the same.
*   If the next version of python came out, there is a chance that my program would not work, but it depends on what new features python implements.
