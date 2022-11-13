# Software Development Plan

## Phase 0: Requirements Specification 

###   Instructions

*   To write a python program that summarizes/pulls the Bureau of Laborstatistics employment data for 2021 and prints it to the console in a report. 
    *   A good solution needs to be able to loop through the 2021.annual.singlefile.csv getting valid information for area_fips, industry_code, and own_code and keep it for the report.
    *   Work at a resonable time
    *   Storing items in a dictionary
    *   Mathes all the data output.txt files
    *   Needs to crash at appropriate times
        *   If a file is not given
    *   Needs to call the usage if nothing is given
    *   Needs to have two sections
        *   One that summarizes all industries
        *   One that summarizes the software publishing industry

###   I already Know How to 
*   loop through a file
    *   Read one line at a time
*   Get elements from the command line
*   Redirect output to a desired location
*   Hard code a filepath
*   Use Python's built in String methods
*   Place the correct information in the right place in the report
*   Keep count of certain items using variables
*   Type convert data

###   Challenges that I anticipate
*   Getting the right information
    *   What to exclude 
    *   What to NOT exclude
*   Putting the information in a dictionary
*   Making the program able to run from any directory
*   Figuring out what Python String method to use
*   Keep one line of a file in memory at a time
*   Display FIP codes as the country, state rather than the actual FIP code
*   Figuring out how the FIPS codes work
*   Condensing the code so that I am not being repetitive



## Phase 1: System Analysis

### Overal Program

*   Input by the Program
    * A single directory containing CSV files

*   Describe What Form the Output will Take
    *   The output will be a report containing the following
        *   Data From All of the 50 States, The District of Columbia, and Territories of the United States of America
            *   Must Include
                *   Oversees Locations
                *   Multicounty, not statewide
                *   Out-of-State
                *   Unknown or Undefined Locations
                *   MORE EXACT DEFINITIONS OF WHAT TO INCLUDE
                    *   Puerto Rico
                    *   Washington, D.C.
                    *   Virgin Islands
            *   Report only considers data from counties and county-equivalent divisions
            *   Must NOT include
                *   US Aggregate Data
                *   per-state aggregate data
                *   Metropolitan Areas
                *   MORE EXACT DEFINITIONS OF WHAT TO NOT INCLUDE
                    *   U.S. Combined and Total FIPS Areas
                    *   All Areas labled 'statewide'
                    *   MicroSAs
                    *   MSAs
                    *   CSAs
                    *   Federal Bureau of Investigation - undesignated

### Brief Description of *some* key functions my Program May Need
*   Functions Names 
    *   The main script for bidData.py
*   Function Inputs
    *   A singular csv file
*   Function Outputs
    *   A report consisting of two elements
        *   Statistics Over All Industries
        *   Statistics Over The Software Publishing Industry
*   One Sentence What Each Function Will Do
    *   This main script will walk over the file, picking relevant data and adding to the statistics for the reports.




## Phase 2: Design 

### Pseudocode

*   If the name of the directory is not given print an error message
*   If opening the file area-titles fails, let the program crash
    *   Concatenate the directory with a '/' and then concatenate that to the name of 'area-titles' so that it can run from any directory
*   Loop through the area-titles file line by line
    *   Split the csv file by comma into 2 columns 
        *   split on commas and set the 'maxsplit' to 2
    *   If conditional the first element of the line (the 0 index) is equal to any of the following -- This discards anywanted FIPS
        *   Any code with the the 3 county FIPS digits all zero
        *   Any code with the first two digits 'US'
        *   Any code with the first digit a 'C'
        *   Any code with the first two digits with a 'CS'
        *   Any code with the first digit a 'M'
        *   Any code with the first two digits a 'CM'
    *   Else conditional -- This puts all other codes into a dicitonary
        *   The FIPs codes are the 'key' and the name is the 'value'
        *   There should be 3,463 codes after sifting through them 
*   Loop through the 2021.annual.singlefile
    *   split on commas into 43 different sections
    *   If the 'area_fips' (index 0) is in the dictionary containing all 3,463 valid fips codes
        *   If the 'own_code' (index 1) is equal to '0'(string) and 'industry_code' (index 2) is equal to '10'(string)

            *   Add one to the rpt.all.num_areas variable
            *   Convert the line's 'total_annual_wages' field (index 10) to an integer
            *   Add the total annual wages to the rpt.all.total_annual_wages variable

            *   If the current line's total_annual_wage (index 10) is greater than the rpt.all.max_annual_wage field (index 1) than reaassign the rpt.allmax_annual_wages field.
                *   rpt.all.max_annual_wages field (index 0) set equal to the Dicitonary FIP code's value -- should be a name
                *   rpt.all.max_annual_wages field (index 1) set equal to the lines's total_annual_wage (index 10)

            *    Convert the line's annual_avg_estabs (index 8) from string to integer if string is numeric and not empty
            *    Add line's annual_avg_estabs to the rpt.all.total_estabs variable

            *    if the line's  annual_avg_estabs is greater than what is in the rpt.all.max_estabs list (index 1)
                *   rpt.all.max_estabs (index 0) equals the Dictionary FIP code value -- should be a name
                *   rpt.all.max_estabs (index 1) equals the line's annual_avg_estabs value (index 8)

            *   Convert the line's annual_avg_emplvl (index 9) from string to integer if string is numeric and not empty
            *   Add converted annual_avg_emplvl to the rpt.all.total_empl

            *   if the line's annual_avg_emplvl is greater than what is in the rpt.all.max_empl list (index 1)
                *   rpt.all.max_empl (index 0) equals the Dictionary FIP code value -- should be a name
                *   rpt.all.max_empl (index 1) equals the annual_avg_emplvl value (index 9) 

        *   If the 'own_code' (index 1) is equal to '5'(string) and 'industry_code' (index 2) is equal to '5112'(string)
            *   Add one to the rpt.soft.num_areas variable
            *   Convert the line's 'total_annual_wages' field (index 10) to an integer
            *   Add the total annual wages to the rpt.soft.total_annual_wages variable

            *   If the current line's total_annual_wage (index 10) is greater than the rpt.soft.max_annual_wage field (index 1) than reaassign the rpt.soft.max_annual_wages field.
                *   rpt.soft.max_annual_wages field (index 0) set equal to the Dicitonary FIP code's value -- should be a name
                *   rpt.soft.max_annual_wages field (index 1) set equal to the lines's total_annual_wage (index 10)

            *    Convert the line's annual_avg_estabs (index 8) from string to integer if string is numeric and not empty
            *    Add line's annual_avg_estabs to the rpt.all.total_estabs variable

            *    if the line's  annual_avg_estabs is greater than what is in the rpt.soft.max_estabs list (index 1)
                *   rpt.soft.max_estabs (index 0) equals the Dictionary FIP code value -- should be a name
                *   rpt.soft.max_estabs (index 1) equals the line's annual_avg_estabs value (index 8)

            *   Convert the line's annual_avg_emplvl (index 9) from string to integer if string is numeric and not empty
            *   Add converted annual_avg_emplvl to the rpt.soft.total_empl

            *   if the line's annual_avg_emplvl is greater than what is in the rpt.soft.max_empl list (index 1)
                *   rpt.soft.max_empl (index 0) equals the Dictionary FIP code value -- should be a name
                *   rpt.soft.max_empl (index 1) equals the annual_avg_emplvl value (index 9) 

        *  Else conditional -- if none of the fields match for any section of the report
            *   skip the line -- this should just be -- 'continune'

    *   else conditional (area_fips did not match any in the dictionary)
        *   Skip the line -- this should just be -- 'continue'

*   Print the Report
    *   There is a pregiven line of code in the starter code
        *   'print(rpt)'
            *   This should workd without any modifications


*   In bad inputs, the program will either crash or skip over the lines of code.
*   In good inputs, the program will read over the lines and take the appropriate data if the FIPs code match and add them to the report



## Phase 3: Implementation

### Problems not forseen earlier
*   The main thing that I had to change was my logic for the loop for the FIPS file.
    *   I was accidently using putting the first line into my dictionary and I had one more value than I should have had
        *   I fixed this by using the opposite logic and looked for things that I needed to put into the dictionary
*   I did not consider the need to remove the quotation marks from the file when I read it line by line
    *   Gave me an error that had too many quotation marks in the error message
*   Most of my indexes needed to be one lower in value
    *   I got the wrong things
        *   Moved the index down one to get the correct information and stay within bounds
*   I took out the condition checking for an empty string because it was useless
*   I added checking if what was being passed in was numeric so that I was not type casting an empty string
    *   This would prevent me from getting an error from trying to parse something that can't be
*   I needed to change the cases that I used an error message so that it exactly takes 2 arguments

*   Most everything else went accorinding to plan because my planned was well thought out
*   I used a while loop using a boolean value
    *   I did not think that this would work well, but it ended well



## Phase 4: Testing & Debugging 

*   Bad inputs
    *   Test cases
        *   'python src/bigData.py'
            *   This ran as expected, outputting an error message and safely exiting
*   I ran the test cases 'python src/bigData.py data/DC_complete' and a some other directories in data.
    *   I opened the output.txt file and compared them

*   I ran the test cases 'python src/bigData.py' to make sure that it crashed appropriately
    *   I got 'Usage: src/bigData.py DATA_DIRECTORY' error message

*   I ran the test case 'python src/bigData.py data/DC_complet'
    *   This gave me an error message
        '''
        Traceback (most recent call last):
  File "C:\Users\layto\OneDrive\Fall 2022 Classes\CS 1440\cs1440-washburn-layton-assn3\src\bigData.py", line 44, in <module>
    f = open(f"{datadir}/area-titles.csv")
FileNotFoundError: [Errno 2] No such file or directory: 'data/DC_complet/area-titles.csv'
        '''
*   The main bugs that I had was having one extra item in my dictionary 
    *   Changing my logic to get what I wanted rather than filtering out what I did not need.

*   The other bug was that nothing was going into my dicitonary 
    *   I removed the extra quotation marks in the line 
    *   This made it so that I could extract the data that I wanted


## Phase 5: Deployment 

*   Validated



## Phase 6: Maintenance

*   In all honesty, I do not think that there is a part of my program that is sloppily written.
    *   The main body of my program could definitely be more efficient, but that is outside of my skillset right now
    *   I have reused code sort of.
        *   I had to change the indexes to reflect the data I wanted to pull, but I could have put more time and written the code in a different way to make it modularized to simplify the code.

*   I If there were a bug in a few months, a bug would be easy to fix becasue the logic in my code is straight forward and does not use a lot of logic that could be simplified. It would probably take 30 mins to 1 hr because of the simplicity of the code.

*   My code would make sense to other people by myself. I took the time to write well thought out plan and work out bugs in there without having to worry about syntax and just the problem.
*   Documentation would make sense to myself in six months because it is well written out and reflects what actually happened in the program.

*   Given a new feature in a year, my code would be easy to impliment because the code does not depend on itself a lot and the complexity of the code is very simple and would be easy to put a new feature into the code.

*   After upgrading software, I think that my program would still work because I did a good job writing the plan.
    *   If the command line argument syntax changed, then my program would not work well because I do use indexes of the command line arugments.
*   If my operating system got upgrading, I think that my code would still work well
*   If the next version of python came out, then I think that my program might still run but depends highly on the new features and the features taken out in python.
