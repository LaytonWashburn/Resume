# Fractal Visualizer User Manual

*   This program is simple for the users. The user will type 'python src/main.py' into the command line after navigating to the correct directory containing the project, staying outside the 'src' directory. 'main.py' is where the program is ran from. The user will then hit enter. This will print an error message that says 
'''
Please provide the name of a fractal as an argument
        phoenix
        peacock
        monkey-knife-fight
        shrimp-cocktail
        mandelbrot
        mandelbrot-zoomed
        spiral0
        spiral1
        seahorse
        elephants
        leaf
        starfish
'''

This is one of the easiest ways to see the names of all the fractal names the user can enter. The user will then retype 'python src/main.py. The user will hit the space bar and then type the name of fractal they want to produce, it should look like this 'src/main.py name of the fractal'. This will then draw the fractal and tell you which one it drew and the amount of time it took for it to be drawn. The user can enter multiple names, but the first name will only be drawn if it is in the list of known fractals, otherwise an error message will print.

This is what a correct input should produce for the phoenix fractal
'''
Rendering phoenix fractal
[100% =================================]
Done in 2.632 seconds!
Wrote picture phoenix.png
Close the image window to exit the program

'''

*   This Correct output will also produce a TK widget/window that pops up with the fractal drawn. The user will havve to close this to exit the program.

Incorrect output
'''
ERROR: phoeni is not a valid fractal
Please choose one of the following:
        phoenix
        peacock
        monkey-knife-fight
        shrimp-cocktail
        mandelbrot
        mandelbrot-zoomed
        spiral0
        spiral1
        seahorse
        elephants
        leaf
        starfish
'''