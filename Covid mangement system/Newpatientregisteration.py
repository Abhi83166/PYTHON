def registeration():
        validvalue = False
        while not validvalue:
    
    
            vc = input("""Select your vaccination center:- 
            VC1 
            VC2
            :-""")
            if vc == "VC1" or vc == "VC2":
                validvalue = True
            else:
                print("Wrong input")
        valid_age = False
        while not valid_age:
            try:
                age = int(input("Enter your age:-"))

            except ValueError:
                print("Your age should be a number! Thats evident")
            if 0 < age < 110:
                    
                    valid_age = True   

                    if age >11:
                        validineer = False
                        while not validineer:
                            if age < 18:   
                                code = input(""" Select the Vaccination Code :-
                            Vaccine Code | Dosage Required | Interval Between Doses(weeeks) |
                                AF      |       2         |             2                  |
                                CZ      |       2         |             3                  |
                                DM      |       2         |             4                  |
                                :-""")
                                if (code == "AF" or code == "BV" or code == "CZ" or code == "DM" or code == "EC"):
                                    validineer = True
                                else:
                                    print("Wong code selected")
                            elif 11 < age < 45: 
                                code = input(""" Select the Vaccination Code :-
                            Vaccine Code | Dosage Required | Interval Between Doses(weeeks) |
                                AF      |       2         |             2                  |
                                BV      |       2         |             3                  |
                                CZ      |       2         |             3                  |
                                DM      |       2         |             4                  |
                                EC      |       1         |             0                  |
                                :-""")
                                if (code == "AF" or code == "BV" or code == "CZ" or code == "DM" or code == "EC"):
                                    validineer = True
                                else:
                                    print("Wong code selected")
                            else:
                                code = input(""" Select the Vaccination Code :-
                            Vaccine Code | Dosage Required | Interval Between Doses(weeeks) |
                                AF      |       2         |             2                  |
                                BV      |       2         |             3                  |
                                DM      |       2         |             4                  |
                                EC      |       1         |             0                  |
                                :-""")
                                if (code == "AF" or code == "BV" or code == "CZ" or code == "DM" or code == "EC"):
                                    validineer = True
                                else:
                                    print("Wong code selected")
                                                                                                        
            else:
                    valid_age = False
                    print("Sorry! Thats not a valid age. Maybe Thats a Typo")
        validphonenumber = False
        while not validphonenumber:
            try:
                phone_number = int(input("Enter your phone number"))
                str_phone_number = str(phone_number)
                if(len(str_phone_number) == 10 ):
                    validphonenumber = True
            except ValueError:
                print("Phone number itself means number! Please input a number") 

        

    

        return vc, age, code, phone_number
