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

from Usage import usage

def wc(files):  	    	       
    files = files[2:]
    if len(files) < 1:
        usage(error="Not enough arguments", tool="wc")
    totalCharacter = 0
    totalWords = 0
    totalLines = 0
    total = 'total'
    for filePath in files:
        characterCount = 0
        wordCount = 0
        lineCount = 0
        file = open(filePath)
        for line in file.readlines():
            list =[]
            for character in line:
                if character == '\n':
                    lineCount += 1
                characterCount += 1
            line = line.replace('\n', '')
            line = line.replace(',', '')
            line = line.split(' ')
            for i in line:
                if i != ' ' and i != '':
                    list.append(i)
            wordCount += len(list)
        totalWords += wordCount
        totalCharacter += characterCount
        totalLines += lineCount
        print(f"{lineCount: <5}   {wordCount: <5}   {characterCount: <5}   {filePath}")
    if len(files) > 1:
        print(f"{totalLines: <5}   {totalWords: <5}   {totalCharacter: <5}   {total}")
      	       
