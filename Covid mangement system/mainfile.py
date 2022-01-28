# main file of the system This file is the one which is required to be run
#header file
import os
from Newpatientregisteration import registeration 
from vaccineadministration import vaccineadministration
from readfile import reading_file
from statistics import statistic_file


#The menu function accepts only integer between the range 1 to 5
def menu():
    try:
        menu_selection = int(input("""
        ------------------MENU SELECTION------------------
        1]= NEW PATIENT REGISTERATION                     ]
        2]= VACCINE ADMINISTRATION                        ]      
        3]= SEARCH PATEINT RECORD                         ]
        4]= SATISTICS AS PER VACCINE CENTER               ]
        5]= EXIT                                          ]
        ---------------------------------------------------
        :-"""))
        return menu_selection
    except ValueError:
        print("Input can only be number form 1 to 5")

#This loop will work until the user enters 5
while True:

    selected_menu = menu()
  

#for patient registeration function
    if selected_menu == 1:
        id_file = open(r"D:\WORK\Python Programming\Covid mangement system\unique_id.txt", "r+")
        id = int(id_file.read())
        id_file.seek(0)
        id= int(id) +1 #incrementing the user id by one
        id_file.write(str(id))
        id_file.truncate()
        #id_file.write("\n")
        id_file.close()
        vc, age, code, phone_number = registeration() # storing the return value form the registeration function
        pateints_file = open("D:\WORK\Python Programming\Covid mangement system\patients.txt", "a+")# appened mode 
        pateints_file.write(str(id)+","+str(vc) +"," + str(age) + "," + str(code) + "," + str(phone_number)+"\n")#for new line using \n
        pateints_file.close()
        input("Press Enter to continue...")   
    #for vaccine administration function
    elif selected_menu ==2:
        menu2input = input("Enter the patient id:- ")
        vaccineadministration(menu2input)

            
        input("Press Enter to continue...")
#for satistics of individual patient
    elif selected_menu == 3:

        menu2input = input("Enter the patient id:- ")
        patientidfound, patient_line = reading_file(menu2input,"patients.txt") 
        vaccination_center, vaccine_type = [patient_line[i] for i in (1, 2)]#returning the index 1 and index 2 value of list returend from teh reading file function
        if patientidfound == 0:
           print("Patient not found")
           
        else:
            patientidfound, patient_line = reading_file(menu2input,"vaccination.txt") 
            #if patient is registered but not yet vaccination 
            if patientidfound == 0:
                print("NEW")
                
            else:    
                vaccine_type, Dose = [patient_line[i] for i in (1, 2)]
                print("Hello " + menu2input + "\nYour vaccination Center is :-" + vaccination_center + "\nYou have selected vaccine type:-" + vaccine_type )
                if(Dose == "D"):
                    print( "Your Vaccination is COMPLETED")
                elif(Dose == "D1"):
                    print("COMPLETED D1")
                else:
                    print("Your Vaccination is COMPLETED")
        input("Press Enter to continue...")
#for stastics based on the vaccination center
    elif selected_menu == 4:
        VC1D1, VC1D2, VC2D1, VC2D2 = statistic_file()
        print("""
        
        
|-------------Number of patient Waiting For Dose 2 From Vaccination Center 1 :""", VC1D1)
        print("|-------------Number of patient Completed their Dose From Vaccination Center 1 :", VC1D2)
        print("|-------------Number of patient Waiting For Dose 2 From Vaccination Center 2 :", VC2D1)
        print("|-------------Number of patient Completed their Dose From Vaccination Center 2 :", VC2D2)
        
        input("Press Enter to continue...")


    elif selected_menu == 5:
        print("""
        
        
        
        
        |-------------------DON'T FORGET TO SANITIZE! THANK YOU--------------
        
        
        
        """)
        exit(0)
    else:
        print("Wrong selection Please enter number from 1 to 5")
        
        