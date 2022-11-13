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

class Card():  	    	       
    COLUMN_NAMES = list("BINGODARLYZEMPUX") 	    	       

    def __init__(self, idnum, ns):  	    	       
        """  	    	       
        Initialize a Bingo! card  	    	       
        """  	    	    
        self.__bingoCard = []    
        self.idnum = idnum 
        ns.shuffle()
        while(len(self.__bingoCard) <= len(ns)-1):
            self.__bingoCard.append(ns.next_row())
        if len(self.__bingoCard) % 2 != 0:
            self.__bingoCard[(int(len(self.__bingoCard)/2))][int((len(self.__bingoCard)/2))] = -1 # If i pass "FREE!" instead it works
   
            
    def id(self):  	    	       
        """  	    	       
        Return an integer: the ID number of the card  	    	       
        """  	    	       
        return self.idnum  	       

    def number_at(self, row, col):  	    	       
        """  	    	       
        Return an integer or a string: the value in the Bingo square at (row, col)  	    	       
        """  	    
        if (0 <= row < len(self) and 0 <= col < len(self) ) :	       
            return self.__bingoCard[row][col]  
        else:
            return None

    def __len__(self):  	    	       
        """  	    	       
        Return an integer: the length of one dimension of the card.  	    	       
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	    	       

        This method was called `size` in the C++ version  	    	       
        """  	    	       
        return len(self.__bingoCard) 

    def __str__(self):  	    	       
        """  	    	       
        Return a string: a neatly formatted, square bingo card  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """  
        output_String = ""
        title = ""	 
        title+=(f"Card #{self.idnum}\n") 
        for i in range(len(self.__bingoCard)):
            title += (f" {self.COLUMN_NAMES[i]:^5}")        
        output_String += (title + '\n')
        output_String+=("+-----"*len(self.__bingoCard)+"+\n")
        for row in self.__bingoCard:
            rowString = ""
            for bingoNumbers in row:
                if bingoNumbers < 0:
                    bingoNumbers = "FREE!"
                rowString += (f"|{bingoNumbers:^5}")
    
            output_String+=(rowString+"|\n")
            output_String+=("+-----"*len(self.__bingoCard)+"+\n")       
        return output_String


    def returns_CardList(self):
        new = []
        for i in self.__bingoCard:
            for j in i:
                new.append(j)
        return new