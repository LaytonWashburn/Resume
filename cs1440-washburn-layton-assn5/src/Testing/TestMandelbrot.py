#!/usr/bin/env python3  	    	       


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

import unittest  	    	       
from Mandelbrot import mandelbrotIterationCounter
from Palette import mandelbrotcolorPalette	    	
from ImagePainter import pixelsWrittenSoFar       

class TestMandelbrot(unittest.TestCase):  	    	       
    def test_iterationCounter(self):  	   	       
        self.assertEqual(mandelbrotIterationCounter(complex(0, 0), len(mandelbrotcolorPalette)), 110)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(-0.751, 1.1075), len(mandelbrotcolorPalette)), 2)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(-0.2, 1.1075), len(mandelbrotcolorPalette)), 9)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(-0.75, 0.1075), len(mandelbrotcolorPalette)), 30)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(-0.748, 0.1075), len(mandelbrotcolorPalette)), 56)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(-0.7562500000000001, 0.078125), len(mandelbrotcolorPalette)), 38)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(-0.7562500000000001, -0.234375), len(mandelbrotcolorPalette)), 12)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(0.3374999999999999, -0.625), len(mandelbrotcolorPalette)), 10)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(-0.6781250000000001, -0.46875),len(mandelbrotcolorPalette)), 29)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(0.4937499999999999, -0.234375), len(mandelbrotcolorPalette)), 4)  	    	       
        self.assertEqual(mandelbrotIterationCounter(complex(0.3374999999999999, 0.546875), len(mandelbrotcolorPalette)), 22)	    	       


    def test_ImagePainter_pixelsWrittenSoFar(self):  	    	       
        self.assertEqual(pixelsWrittenSoFar(1,(512 - 1) / 512,512), '[100% =================================]')  	    	       
        self.assertEqual(pixelsWrittenSoFar(7, (512 -7) /512 ,512), '[ 99% =================================]')  	    	       
        self.assertEqual(pixelsWrittenSoFar(257, (512 - 257) / 512 ,512), '[ 50% ================                 ]')  	    	       
        self.assertEqual(pixelsWrittenSoFar(256, (512 - 256) / 512 ,512), '[ 50% =================                ]')  	    	       
        self.assertEqual(pixelsWrittenSoFar(100, (512 - 100) / 512 ,512), '[ 80% ===========================      ]')  	    	       
        self.assertEqual(pixelsWrittenSoFar(640, (512 - 640) / 512 ,512), '[-25%                                  ]')  	    	       
        self.assertEqual(pixelsWrittenSoFar(137, (512 - 137) / 512,512), '[ 73% ========================         ]')  	    	       
        self.assertEqual(pixelsWrittenSoFar(512, (512 - 512) / 512 ,512), '[  0%                                  ]')  	    	       


    def test_palleteLength(self):  	    	       
        self.assertEqual(111, len(mandelbrotcolorPalette))
        self.assertNotEqual(112, len(mandelbrotcolorPalette))
        self.assertNotEqual(110, len(mandelbrotcolorPalette))
        self.assertNotEqual(0, len(mandelbrotcolorPalette))
        self.assertNotEqual(109, len(mandelbrotcolorPalette))
        self.assertNotEqual(-1, len(mandelbrotcolorPalette))
          
        
    def test_Palette_Colors(self):
      self.assertEqual(mandelbrotcolorPalette[110],'#e8283f')
      self.assertEqual(mandelbrotcolorPalette[0], '#89ff00')
      self.assertEqual(mandelbrotcolorPalette[90],'#8fa7da' )
      self.assertEqual(mandelbrotcolorPalette[91],'#8480db' )
      self.assertEqual(mandelbrotcolorPalette[-1],'#e8283f' )
      self.assertEqual(mandelbrotcolorPalette[54], '#e0c6bd' )
      self.assertEqual(mandelbrotcolorPalette[76], '#e6dad7' )
      self.assertEqual(mandelbrotcolorPalette[35], '#eccd43' )
      self.assertEqual(mandelbrotcolorPalette[12],'#e7ddd7' )
      self.assertEqual(mandelbrotcolorPalette[101],'#c8e1cb' )  	    	       


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
