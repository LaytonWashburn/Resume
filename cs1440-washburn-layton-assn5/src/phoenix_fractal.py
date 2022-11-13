#!/usr/bin/env python3  	    	       
# Phoenix Fractal Visualizer - a variation of the Julia Fractal  	    	       

#                         _  	    	       
#                        (o)<  DuckieCorp Software License  	    	       
#                   .____//  	    	       
#                    \ <' )   Copyright (c) 2022 Erik Falor  	    	       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	    	       
#  	    	       
# Permission is granted, to any person who is EITHER an employee OR  	    	       
# customer of DuckieCorp, to deal in the Software without restriction,  	    	       
# including without limitation the rights to use, copy, modify, merge,  	    	       
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	    	       
# permit persons to whom the Software is furnished to do so, subject to the  	    	       
# following conditions:  	    	       
#  	    	       
# The above copyright notice and this permission notice shall be included in  	    	       
# all copies or substantial portions of the Software.  	    	       
#  	    	       
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	    	       
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	    	       
# FITNESS FOR A PARTICULAR PURPOSE, EDUCATIONAL VALUE AND NONINFRINGEMENT. IN  	    	       
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  	    	       
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  	    	       
# OTHERWISE, ARISING FROM INDIGNATION, INDIGESTION, INDIFFERENCE, INDECENCY,  	    	       
# INDENTATION, INDETERMINATION, INTOXICATION, INDOCTRINATION, INTOLERANCE,  	    	       
# INDULGENCE, INDELICATENESS, INDISCRETION, INEFFECTIVENESS OR IN CONNECTION  	    	       
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  	    	       

# These are the imports that I usually import  	    	       
#import turtle  	    	       
#import os  	    	       
#import os.path  	    	       
import sys  	    	       
import time  	    	       

 	    	         	    	       
# these ones are the ones that i'm using in this program  	    	       
from tkinter import Tk, Canvas, PhotoImage, mainloop  	    	       
from time import time  	    	       


def getColorFromPalette(z, phoenxColors, win):  	    	       
    """  	    	       
    Return the index of the color of the current pixel  	    	       
    within the Phoenix fractal in the palette array  	    	       
    """  	    	       

    # I feel bad about all of the global variables I'm using.  	    	       
    # There must be a better way...  	    	       
    #global phoenixColors  	    	       
    #global win  	    	       

    # c is the Julia Constant; varying this value gives rise to a variety of variated images  	    	       
    c = complex(0.5667, 0.0)  	    	       

    # phoenix is the Phonix Constant; same deal as above - adjust this to get different results  	    	       
    pheonix = complex(-0.5, 0.0)  	    	       

    # The first thing we do to the complex number Z is reflect its components,  	    	       
    # so the imaginary part becomes the real part, and vice versa  	    	       
    zFlipped = complex(z.imag, z.real)  	    	       
    ## if we don't do this, the image comes out SIDEWAYS!!!  	    	       

    # zPrevious is the PREVIOUS Z value, except the 1st time through the  	    	       
    # function, when it starts out as Complex Zero (which is actually the  	    	       
    # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!  	    	       
    zPrev = 0+0j  	    	       
    z = zFlipped  	    	       

    # Use 101 here because that's the number of colors in the palette  	    	       
    # Except range() wants its number to be one more than the number  	    	       
    # that YOU want.  	    	       
    for i in range(102):# <--not cool, PYTHON WHY CAN'T YOU BE BEAUTIFUL LIKE MATH?  	    	       

        zSave = z  # save the current Z value before we overwrite it  	    	       
        # compute the new Z value from the current and previous Zs  	    	       
        z = z * z + c + (pheonix * zPrev)  	    	       
        zPrev = zSave  # Set the prevZ value for the next iteration  	    	       

        if abs(z) > 2:  	    	       
            return phoenixColors[i]  # The sequence is unbounded  	    	       
            z = z * z + c  # + zPrev * pheonix  	    	       
    # TODO: One of these returns occasionally makes the program crash sometimes  	    	       
    return phoenixColors[101]         # Else this is a bounded sequence  	    	         	    	       


def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):  	    	       
    """Make sure that the fractal configuration data repository dictionary  	    	       
    contains a key by the name of 'name'  	    	       

    When the key 'name' is present in the fractal configuration data repository  	    	       
    dictionary, return its value.  	    	       

    Return False otherwise  	    	       
    """  	    	       
    for key in dictionary:  	    	        	    	       
        if key == name:  	    	         	    	       
            return key  
    # if name in dictionary:
    #   return name	    	       
 	    	       
#tkPhotoImage = None  	    	       

def makePictureOfFractal(f, i, e, w, g, p, W, s, win):  	    	       
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	    	       
    Assumes the image is 640x640 pixels."""  	    	       

    # Correlate the boundaries of the PhotoImage object to the complex  	    	       
    # coordinates of the imaginary plane  	    	       

    # Compute the minimum coordinate of the picture  	    	       
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),  	    	       
           (f['centerY'] - (f['axisLength'] / 2.0)))  	    	       

    # Compute the maximum coordinate of the picture  	    	       
    # The program has only one axisLength because the images are square  	    	       
    # Squares are basically rectangles except the sides are equal instead of different  	    	       
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),  	    	       
           (f['centerY'] + (f['axisLength'] / 2.0)))  	    	       

    # Display the image on the screen  	    	       
    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=s, height=s, bg=W)  	    	       

    # pack the canvas object into its parent widget  	    	       
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  	    	       
    # TODO: Sometimes I wonder whether some of my functions are trying to do  	    	       
    #       too many different things... this is the correct part of the  	    	       
    #       program to create a GUI window, right?  	    	       

    # Create the TK PhotoImage object that backs the Canvas Objcet  	    	       
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals  	    	       
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")  	    	       
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive  	    	       
 	    	       
    # Total number of pixels in the image, AKA the area of the image, in pixels  	    	       
    area_in_pixels = 640 * 640  	    	       

    # pack the canvas object into its parent widget  	    	       
     	       
    # At this scale, how much length and height of the  	    	       
    # imaginary plane does one pixel cover?  	    	       
    size = abs(max[0] - min[0]) / s  	    	       

    # pack the canvas object into its parent widget  	    	       
   	    	       

    # Keep track of the fraction of pixels that have been written up to this point in the program  	    	       
    fraction_of_pixels_writtenSoFar = int(s // 640)  	    	       

    # for r (where r means "row") in the range of the size of the square image,  	    	       
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"  	    	       
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to  	    	       
    # but I have to here because we're actually going BACKWARDS, which took me  	    	       
    # a long time to figure out, so don't change it, or else the picture won't  	    	       
    # come out right  	    	       
    r = s  	    	       
    while r in range(s, 0, -1):  	    	       
        # for c (c == column) in the range of pixels in a square of size s  	    	       
        cs = []  	    	       
        for c in range(s):  	    	       
            # calculate the X value in the complex plane (I guess that's  	    	       
            # actually the REAL number part, but we call it X because  	    	       
            # GRAPHICS... whatev)  	    	       
            x = min[0] + c * size  	    	       
            y = 0  	    	       
            # get the color of the pixel at this point in the complex plain  	    	       
 	    	       
            # calculate the X value in the complex plane (but I know this is  	    	       
            # really the IMAGINARY axis that we're talking about here...)  	    	       
            y = min[1] + r * size  	    	       
            # TODO: do I really need to call getColorFromPalette() twice?  	    	       
            #       It seems like this should be slow...  	    	       
            #       But, if it aint broken, don't repair it, right?  	    	       
            cp = getColorFromPalette(complex(x, y), phoenixColors, win)  	    	       
            cs.append(cp)  	    	       
        pixls = '{' + ' '.join(cs) + '}'  	    	       
        p.put(pixls, (0, s - r))  	    	       
        w.update()  # display a row of pixels  	    	       
        fraction_of_pixels_writtenSoFar = (s - r) / s # update the number of pixels output so far  	    	       
        # print a statusbar on the console  	    	       
        print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"  	    	       
                + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",  	    	       
                end="\r"  # the end  	    	       
                , file=sys.stderr)  	    	       
        r -= 1  	    	       


# This is the color palette, which defines the palette that images are drawn  	    	       
# in as well as limiting the number of iterations the escape-time algorithm uses  	    	       
#  	    	       
# TODO: It would be nice to add more or different colors to this list, but it's  	    	       
# just so much work to calculate all of the in-between shades!  	    	       
phoenixColors = [  	    	       
        '#FFE4B5', '#FFE5B2', '#FFE6AF', '#FFE8AC', '#FFE9A9', '#FFEBA7',  	    	       
        '#FFEDA4', '#FFEFA1', '#FFF19E', '#FFF49B', '#FFF698', '#FFF995',  	    	       
        '#FFFC92', '#FFFF90', '#FCFF8D', '#F9FF8A', '#F5FF87', '#F1FF84',  	    	       
        '#EEFF81', '#E9FF7E', '#E5FF7B', '#E1FF78', '#DDFF76', '#D8FF73',  	    	       
        '#D3FF70', '#CEFF6D', '#C9FF6A', '#C4FF67', '#BEFF64', '#B9FF61',  	    	       
        '#B3FF5F', '#ADFF5C', '#A7FF59', '#A0FF56', '#9AFF53', '#93FF50',  	    	       
        '#8DFF4D', '#86FF4A', '#7FFF47', '#78FF45', '#70FF42', '#69FF3F',  	    	       
        '#61FF3C', '#59FF39', '#51FF36', '#49FF33', '#40FF30', '#38FF2E',  	    	       
        '#2FFF2B', '#28FF29', '#25FF2C', '#22FF30', '#1FFF33', '#1CFF37',  	    	       
        '#19FF3B', '#16FF3F', '#14FF43', '#11FF48', '#0EFF4C', '#0BFF51',  	    	       
        '#08FF56', '#05FF5B', '#02FF60', '#00FE65', '#00FC6B', '#00F971',  	    	       
        '#00F677', '#00F37C', '#00F081', '#00ED86', '#00EA8B', '#00E790',  	    	       
        '#00E595', '#00E299', '#00DF9D', '#00DCA2', '#00D9A5', '#00D6A9',  	    	       
        '#00D3AD', '#00D0B0', '#00CDB4', '#00CBB7', '#00C8BA', '#00C5BD',  	    	       
        '#00C2BF', '#00BCBF', '#00B4BC', '#00ACB9', '#00A4B6', '#009DB4',  	    	       
        '#0095B1', '#008EAE', '#0087AB', '#0080A8', '#0079A5', '#0072A2',  	    	       
        '#006C9F', '#00669C', '#005F9A', '#005997', '#005494', '#004E91',  	    	       
        '#00488E', '#00438B', '#003E88', '#003985', '#003483', '#002F80',  	    	       
        '#002B7D', '#00267A', '#002277'  	    	       
        ]  	    	       



# This dictionary contains the different views of the Phoenix set you can make  	    	       
# with this program.  	    	       
#  	    	       
# For convenience I have placed these into a dictionary so you may easily  	    	       
# switch between them by entering the name of the image you want to generate  	    	       
# into the variable 'i'.  	    	       
#  	    	       
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into  	    	       
# this configuration dictionary instead of hardcoding it into this program.  	    	       
# But I don't have time for this right now, too busy.  I'll just keep doing it  	    	       
# the way I know how.  	    	       
f = {  	    	       
        # The full Phoneix set  	    	       
        'phoenix': {  	    	       
            'centerX':     0.0,  	    	       
            'centerY':     0.0,  	    	       
            'axisLength':  3.25,  	    	       
            },  	    	       

        # This one looks like a peacock's tail to me  	    	       
        'peacock': {  	    	       
            'centerX':     -0.363287878200906,  	    	       
            'centerY':     0.381197981824009,  	    	       
            'axisLength':  0.0840187115019564,  	    	       
        },  	    	       

        # Two or more monkeys having a scuffle  	    	       
        'monkey-knife-fight': {  	    	       
            'centerX':    -0.945542168674699,  	    	       
            'centerY':    0.232234726688103,  	    	       
            'axisLength': 0.136626506024096,  	    	       
            },  	    	       

        # This one makes me hungry to look at  	    	       
        'shrimp-cocktail': {  	    	       
            'centerX': 0.529156626506024,  	    	       
            'centerY': -0.3516077170418,  	    	       
            'axisLength': 0.221204819277108,  	    	       
            },  	    	       
        }  	    	       


# This is how you write colors for computers  	    	        	    	       
# GREY0 = '#000000'  # gray 0 - basically the same as black  	    	        	    	       


def phoenix_main(i):  	    	       
    """The main entry-point for the Phoenix fractal generator"""  	    	       

    # Look, I  know globals are bad, but I don't know how else to use those  	    	       
    # variables in here if I don't do it this way.  I didn't take any fancy CS  	    	       
    # classes, sue me  	    	       
    #global tkPhotoImage  	    	       
    #global win  	  
    GREY0 = '#000000'  # gray 0 - basically the same as black    	       

    # Note the time of when we started so we can measure performance improvements  	    	       
    beforeTime = time()  	    	       
    # Set up the GUI so that we can display the fractal image on the screen  	    	       
    win = Tk()  	    	       

    print("Rendering %s fractal" % i, file=sys.stderr)  	    	       
    # the size of the image we will create is 512x512 pixels  	    	       
    sizeOfImage = 512  	    	       
    # construct a new TK PhotoImage object that is 512 pixels square...  	    	       
    tkPhotoImage = PhotoImage(width=sizeOfImage, height=sizeOfImage)  	    	       
    # ... and use it to make a picture of a fractal  	    	       
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?  	    	       
    makePictureOfFractal(f[i], i, ".png", win, phoenixColors, tkPhotoImage, GREY0, sizeOfImage, win)  	    	       

	    	       
    # Output the Fractal into a .png image  	    	       
    tkPhotoImage.write(f"{i}.png")  	    	       
    print("Wrote picture " + i + ".png", file=sys.stderr)
    print(f"\nDone in {time() - beforeTime:.3f} seconds!", file=sys.stderr)  	    	       	    	       

    # print a message telling the user how to quit or exit the program  	    	       
    print("Close the image window to exit the program", file=sys.stderr)  	    	       
    # Call tkinter.mainloop so the GUI remains open  	    	       
    mainloop()  	    	       
