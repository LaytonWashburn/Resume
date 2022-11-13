#!/usr/bin/env python  	    	       

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


import time  	    	       
import sys  	    	       
from Report import Report  	    	       


rpt = Report(year=2021)  	    	       

if __name__ == '__main__':  
    FIPS= {}	 
    lineTrack = True
    if len(sys.argv) != 2:
        print("Usage: src/bigData.py DATA_DIRECTORY")
        sys.exit() 
    datadir = sys.argv[1]
    f = open(f"{datadir}/area-titles.csv")
    for line in f.readlines():
        line = line.replace('"','') 
        line = line.replace('\n', '')
        line = line.split(",", maxsplit=1)  
        if line[0].isnumeric() and not line[0].endswith('000'):
            FIPS[line[0]] = line[1]	
        else:
            continue
    largeFile = open(f"{datadir}/2021.annual.singlefile.csv") 
    while(lineTrack): 
        line = largeFile.readline()
        if line == '':
            lineTrack = False
        else:
            line = line.replace('"', '')
            line = line.replace('\n', '')
            line = line.split(',', maxsplit= 42) 
            if line[0] in FIPS.keys():
                if line[1] == '0' and line[2] == '10':
                    rpt.all.num_areas += 1
                    temp = int(line[10])       
                    rpt.all.total_annual_wages += temp
                    if int(line[10]) > rpt.all.max_annual_wage[1]:
                        rpt.all.max_annual_wage[0] = FIPS[line[0]]
                        rpt.all.max_annual_wage[1] = int(line[10])
                    if line[8].isnumeric():       
                        temp = int(line[8])
                        rpt.all.total_estab += temp
                    if line[8].isnumeric() and int(line[8]) > rpt.all.max_estab[1]: 
                        rpt.all.max_estab[0] = FIPS[line[0]]
                        rpt.all.max_estab[1] = int(line[8])
                    if line[9].isnumeric():
                        temp = int(line[9])
                        rpt.all.total_empl += temp
                    if line[9].isnumeric() and int(line[9]) > rpt.all.max_empl[1]:
                        rpt.all.max_empl[0] = FIPS[line[0]]
                        rpt.all.max_empl[1] = int(line[9])
                    
                elif line[1] == '5' and line[2] == '5112':
                    rpt.soft.num_areas += 1
                    temp = int(line[10])       
                    rpt.soft.total_annual_wages += temp
                    if int(line[10]) > rpt.soft.max_annual_wage[1]:
                        rpt.soft.max_annual_wage[0] = FIPS[line[0]]
                        rpt.soft.max_annual_wage[1] = int(line[10])
                    if line[8].isnumeric():       
                        temp = int(line[8])
                        rpt.soft.total_estab += temp
                    if line[8].isnumeric() and int(line[8]) > rpt.soft.max_estab[1]: 
                        rpt.soft.max_estab[0] = FIPS[line[0]]
                        rpt.soft.max_estab[1] = int(line[8])
                    if line[9].isnumeric():
                        temp = int(line[9])
                        rpt.soft.total_empl += temp
                    if line[9].isnumeric() and int(line[9]) > rpt.soft.max_empl[1]:
                        rpt.soft.max_empl[0] = FIPS[line[0]]
                        rpt.soft.max_empl[1] = int(line[9])    
                else:
                    continue   
            else:
                continue
    print(rpt)
    f.close()
    largeFile.close()
          
    	       
