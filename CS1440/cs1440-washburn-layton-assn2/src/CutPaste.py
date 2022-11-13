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

def cut(args):  	       
    args = args [2:]
    if len(args) < 1:
        usage(error="Too few arguments",tool="cut")
    columns = ["1"]
    files = []
    if args[0] == '-f':
        if len(args) < 3:
            usage(error="Too few arguments",tool="cut")
        columns = []
        columns = args[1].split(',')
        for column in columns:
            if column.isnumeric() and int(column) > 0:
                pass
            else:
                columns.remove(column)
        if len(columns) == 0:
            usage(error="A comma-separated field specification is required", tool="cut")
        for arg in args[2:]:
            files.append(open(arg))
    else:  
        for arg in args[0:]:
            files.append(open(arg)) 
    columns.sort()
    
    for file in files:
        for line in file.readlines():
            line = line.replace("\n","")
            line = line.split(',')
            for column in range(0, len(columns)):
                if int(columns[column]) == 0:
                    usage(error="A comma-separated field specification is required", tool="cut")
                if len(line) < int(columns[column]):
                    print('')
                else:
                    if column == len(columns) -1:
                        print(line[int(columns[column])-1])
                    else:
                        print(line[int(columns[column])-1] +',', end='')


def paste(args):  	    	
    if len(args) < 1:       
        usage(error = "Not enough arguments", tool="paste")       
    fileList = []
    longest = 0
    for filePath in args:
        count = 0
        file = open(filePath)
        for line in file.readlines():
            count += 1
        if count > longest:
            longest = count
        fileList.append(file)
        file.seek(0)
    for i in range(0, longest):
        for file in fileList:
            line = file.readline()
            line = line.replace('\n', '')
            if fileList[-1] == file:
                print(line + '\n', end='')        
            else:
                print(line + ',', end='')
    for file in fileList:
        file.close()




