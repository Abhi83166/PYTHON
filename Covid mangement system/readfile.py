import os

def reading_file(input_patient_id, filename):
    working_directory = "D:\WORK\Python Programming\Covid mangement system\\"
    file_path = working_directory + filename
    with open(file_path) as get_code:
        lines = [line.rstrip().split(",") for line in get_code]#reading the file and stripping the file by , delimeter
        get_code.close()
    id_found = False
    break_out_flag = False
#below code read the data from the lines list and check each first index if the index matches it breaks out of the loop
    for rows, columns in enumerate(lines):
        for j in columns:
            if lines[rows][0] == input_patient_id:
               
                searched_line = columns
                break_out_flag = True #attaching a break flag to stop the outer loop execution once the id is found
                id_found = True
                break
        if break_out_flag:
            break
    if id_found:
        
        return  True, searched_line
    else:
        return False, 0

