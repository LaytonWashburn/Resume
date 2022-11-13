from Palette import phoenixColorPalette, mandelbrotcolorPalette
from Phoenix import phoenixIterationCounter
from Mandelbrot import mandelbrotIterationCounter
import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop 


def makeFractal(fractal):  	    	       
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	    	       
    This code creates an image which is 640x640 pixels in size."""  	    	       

    screenSize = 512
    
    print("Rendering {} fractal".format(fractal['name']), file=sys.stderr)  	    	       
    before = time.time()  	    	         	    	       
    window = Tk()  	    	       
    img = PhotoImage(width=screenSize, height=screenSize)  	    	        	    	       
     	    	       	    	       
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)  	    	       
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)  	    	       
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)  	    	       
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)  	    	       
 	    	       
    canvas = Canvas(window, width=screenSize, height=screenSize, bg='#000000')  	    	       
    canvas.pack()  	    	       
    canvas.create_image((screenSize/2, screenSize/2), image=img, state="normal")  	    	       
	    	       
    pixelsize = abs(maxx - minx) / screenSize  	    	       
	    	       
    total_pixels = screenSize**2 	    	       
    for row in range(screenSize, 0, -1):  	    	       
        cc = []  	    	       
        for col in range(screenSize):  	    	       
            x = minx + col * pixelsize  	    	       
            y = miny + row * pixelsize
            if (fractal['type'] == 'phoenix'):  	    	       
                indexToColor = phoenixIterationCounter(complex(x, y), len(phoenixColorPalette)-9)  	    	       
                cc.append(phoenixColorPalette[indexToColor])  	  
            else:
                indexToColor = mandelbrotIterationCounter(complex(x, y), len(mandelbrotcolorPalette))  	    	       
                cc.append(mandelbrotcolorPalette[indexToColor])  
                
        img.put('{' + ' '.join(cc) + '}', to=(0, screenSize-row))  	    	       
        window.update()    	    	       
        portion = (screenSize - row) / screenSize  	    	           	       
        print(pixelsWrittenSoFar(row, portion, screenSize), end='\r', file=sys.stderr)   	
 	    	       
    after = time.time()  	    	       
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)  	    	       
    img.write(f"{fractal['name']}.png")  	    	       
    print(f"Wrote picture {fractal['name']}.png", file=sys.stderr)  	    	         	    	       
    print("Close the image window to exit the program", file=sys.stderr) 
    mainloop() 
    
def pixelsWrittenSoFar(rows, portion, screenSize): 	    	         	    	       
    pixels = (screenSize - rows) * screenSize  	    	       
    status_percent = '{:>4.0%}'.format(portion)  	    	       
    status_bar_width = 34  	    	       
    status_bar = '=' * int(status_bar_width * portion)  	    	       
    status_bar = '{:<33}'.format(status_bar)  	    	        	    	       
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
    
    



























