import os
from typing import ClassVar

def statistic_file():
    working_directory = "D:\WORK\Python Programming\Covid mangement system\patients.txt"
    
    with open(working_directory) as get_code:
        lines = [line.rstrip().split(",") for line in get_code]#reading the file and stripping the file by , delimeter
        get_code.close()
    
    totalvc1d1, totalvc1d2, totalvc2d1, totalvc2d2 = 0, 0, 0, 0
    WD1, WD2 = 0, 0
    
#below code read the data from the lines list and check each first index if the index matches it breaks out of the loop
    for rows, columns in enumerate(lines):
        
        if(columns[1] == "VC1"):
            WD1,WD2 = reading_status(rows)
            
            totalvc1d1 = totalvc1d1 + WD1
            totalvc1d2 = totalvc1d2 + WD2
        if(columns[1] == "VC2"):
           
            WD1,WD2 = reading_status(rows)
            totalvc2d1 = totalvc2d1 + WD1
            totalvc2d2 = totalvc2d2 + WD2
        # for j in columns:
        #     print(columns)
    return totalvc1d1, totalvc1d2, totalvc2d1, totalvc2d2
    
    
def reading_status(linenumbers):
    d1, d2 = 0, 0
    try:
        working_directory = "D:\WORK\Python Programming\Covid mangement system\\vaccination.txt"
        with open(working_directory) as get_code:
            innerlines = [line.rstrip().split(",") for line in get_code]#reading the file and stripping the file by , delimeter
            get_code.close()
        
        if(innerlines[linenumbers][2] == "D1"):
           
            d1 = 1
        if(innerlines[linenumbers][2] == "D2" or innerlines[linenumbers][2] == "D"):
            d2 = 1
       

    except(IndexError):
        d = 0
    return d1, d2

v1,v2,v3,v4 = statistic_file()


