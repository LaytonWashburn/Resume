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

from Card import Card  	    	       
from RandNumberSet import RandNumberSet  	    	       


class TestCard(unittest.TestCase):  	    	       

    def setUp(self):  	    	       
        """  	    	       
        Create no fewer than 5 Card objects to test  	    	       

        Create a mixture of odd and even-sized cards  	    	       
        """  	    	       
        self.card1 = Card(0, RandNumberSet(3, 10)) 
        self.card2 = Card(1, RandNumberSet(4, 20))
        self.card3 = Card(2, RandNumberSet(6, 37))
        self.card4 = Card(3, RandNumberSet(15, 250))
        self.card5 = Card(4, RandNumberSet(2, 11)) 	    	       


    def test_len(self):  	    	       
        """Assert that each card's size is as expected"""  	    	       
        self.assertEqual(len(self.card1), 3)  	
        self.assertEqual(len(self.card2), 4)    	       
        self.assertEqual(len(self.card3), 6)  
        self.assertEqual(len(self.card4), 15)   
        self.assertEqual(len(self.card5), 2) 
        
           
    def test_id(self):  	    	       
        """Assert that each card's ID number is as expected"""  	    	       
        self.assertEqual(self.card1.idnum, 0)  	
        self.assertEqual(self.card2.idnum, 1)  
        self.assertEqual(self.card3.idnum, 2)  
        self.assertEqual(self.card4.idnum, 3)  
        self.assertEqual(self.card5.idnum, 4)      	       

    def test_freeSquares(self):  	
        """Assert that each odd card has the FREE! string in the middle"""    	       
        self.assertEqual(self.card1.number_at(int(len(self.card1)/2), int((len(self.card1)/2))), -1) 
        self.assertNotEqual(self.card2.number_at(int(len(self.card2)/2), int((len(self.card2)/2))), -1)
        self.assertNotEqual(self.card3.number_at(int(len(self.card3)/2), int((len(self.card3)/2))), -1)
        self.assertEqual(self.card4.number_at(int(len(self.card4)/2), int((len(self.card4)/2))), -1)
        self.assertNotEqual(self.card5.number_at(int(len(self.card5)/2), int((len(self.card5)/2))), -1)	    	       

    def test_no_duplicates(self):  	    	       
        """Ensure that Cards do not contain duplicate numbers"""  	 
        cardList = [self.card1, self.card2, self.card3, self.card4, self.card5]
        for card in cardList:
            for i in range(len(card.returns_CardList())):
                self.assertLessEqual(card.returns_CardList().count(i), 1)
        
                       
if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
