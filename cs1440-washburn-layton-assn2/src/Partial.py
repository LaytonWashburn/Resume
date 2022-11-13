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

def head(args):  	    	       
    lineAmount = 10
    args = args[2:]
    if len(args) < 1:
        usage(error="Number of lines is required", tool='head')
    if args [0] =='-n':
        if len(args) < 3:
            usage(error="Number of lines is required", tool='head')
        if args[1].isnumeric(): 
            lineAmount = int(args[1])
            args = args[2:]
            for filePath in args:
                file = open(filePath)
                if len(args) > 1:
                    print(f"==> {filePath} <==")
                for i in range (0, lineAmount):
                    print(file.readline(), end = "")
                if filePath != args[len(args) -1]:
                    print('\n')
                file.close()
        else:
            usage(error="Number of lines is required", tool="head")
    
    else:	
        if len(args) > 0:    	    
            for filePath in args:
                    file = open(filePath)
                    if len(args) > 1:
                        print(f"==> {filePath} <==")
                    for i in range (0, lineAmount):
                        print(file.readline(), end = "")
                    if filePath != args[len(args) -1]:
                        print('\n')
                    file.close()
        else:
            usage(error="Number of lines is required", tool="head")



def tail(args):  	    	       
    lineAmount = 10
    args = args[2:]
    if len(args) < 1:
        usage(error="Number of lines is required", tool='head')
    if args[0] == '-n' and len(args) < 3:
        usage(error="Number of lines is required", tool='head')
    if args[0] == '-n': 
        if args[1].isnumeric(): 
            lineAmount = int(args[1])
            args = args[2:]
            for filePath in args:
                list = []
                file = open(filePath)
                if len(args) > 1:
                    print(f"==> {filePath} <==")
                for line in file.readlines():
                    line = line.replace('\n', '')
                    list.append(line)
                list = list[-lineAmount:] 
                for i in list:
                    print(i)
                if filePath != args[len(args) -1]:
                    print('\n')	   
                file.close()
        else:
            usage(error="Number of lines is required", tool='tail')   
    else:
        for filePath in args:
            list = []
            file = open(filePath)
            if len(args) > 1:
                print(f"==> {filePath} <==")
            for line in file.readlines():
                line = line.replace('\n', '')
                list.append(line)
            list = list[-lineAmount:] 
            for i in list:
                print(i)
            if filePath != args[len(args) -1]:
                print('\n')	  
            file.close()	    	  

   
