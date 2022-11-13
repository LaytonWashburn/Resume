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
from Phoenix import phoenixIterationCounter
from Mandelbrot import mandelbrotIterationCounter	
from FractalInformation import allFractalNames 
from Palette import phoenixColorPalette   	       
	    	       

class TestPhoenix(unittest.TestCase):  	    	       
    def test_PhoenxIterationCounter(self):  	    	       
        self.assertEqual(phoenixIterationCounter(complex(0, 0), len(phoenixColorPalette) - 9),5)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.751, 1.1075),len(phoenixColorPalette) - 9),0)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.2, 1.1075),len(phoenixColorPalette) - 9),1)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.750, 0.1075),len(phoenixColorPalette) - 9),34)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.748, -0.1075),len(phoenixColorPalette) - 9),101)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.75625, 0.078125),len(phoenixColorPalette) - 9),101)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.75625, -0.234375),len(phoenixColorPalette) - 9),32)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(0.33749, -0.625),len(phoenixColorPalette) - 9),2)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.678125, -0.46875),len(phoenixColorPalette) - 9),101)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.406, -0.837),len(phoenixColorPalette) - 9),1)  	    	       
        self.assertEqual(phoenixIterationCounter(complex(-0.186, -0.685),len(phoenixColorPalette) - 9),2)
    	    	       

    def test_Dictionary_Names(self):
        self.assertFalse('leaves' in allFractalNames.keys())
        self.assertFalse('phoenixs' in allFractalNames.keys())
        self.assertFalse('monkey--knife-fight'in allFractalNames.keys())
        self.assertTrue('leaf' in allFractalNames.keys())
        self.assertTrue('mandelbrot' in allFractalNames.keys())
        self.assertTrue('elephants' in allFractalNames.keys())    	    	       


    def test_Phoenix_Palettelength(self):  	    	       
        self.assertEqual(len(phoenixColorPalette), 111)
        self.assertNotEqual(len(phoenixColorPalette), 110) 
        self.assertNotEqual(len(phoenixColorPalette), 112) 
        self.assertNotEqual(len(phoenixColorPalette), 0) 
        self.assertNotEqual(len(phoenixColorPalette), -1)   	
            	       
                    
    def test_PhoenixColors(self):
        self.assertEqual(phoenixColorPalette[110],'#002277')
        self.assertEqual(phoenixColorPalette[0], '#FFE4B5')
        self.assertEqual(phoenixColorPalette[90],'#0095B1')
        self.assertEqual(phoenixColorPalette[91],'#008EAE')
        self.assertEqual(phoenixColorPalette[-1],'#002277')
        self.assertEqual(phoenixColorPalette[54],'#19FF3B')
        self.assertEqual(phoenixColorPalette[76],'#00D9A5')
        self.assertEqual(phoenixColorPalette[35],'#93FF50')
        self.assertEqual(phoenixColorPalette[12],'#FFFC92')
        self.assertEqual(phoenixColorPalette[101],'#004E91') 

if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
