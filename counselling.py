import pandas as pd
import math
import os
import sys
import random as r
from datetime import date

# Verification of whether the E-mail created is Valid or not

def validEmail(mail):
    veri_count1 = 0
    veri_count2 = 0

    if "@" not in mail:
        return False
    
    (name , domain) = mail.split("@")

    for e in range(0,len(name)):
        if e == 0:
            if (ord(name[e]) >= 97 and ord(name[e]) <= 122): 
                veri_count1 += 1
                continue
                
            else:
                return False
                break
                
        else:
            if (ord(name[e]) >= 97 and ord(name[e]) <= 122):
                veri_count1 += 1 
                continue
            elif name[e] in [0,1,2,3,4,5,6,7,8,9]:
                veri_count1 += 1
                continue
            else:
                return False
                break
        
    (dc , co) = domain.split(".")
    
    for h in range(0,len(dc)):

        if (ord(dc[h]) >= 97 and ord(dc[h]) <= 122):
            veri_count2 += 1 
            continue
        elif dc[h] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            veri_count2 += 1
            continue
        else:
            return False
            break
    
    if co == "com" and veri_count1 == len(name) and veri_count2 == len(dc):
        return True
    return False


# Verifications of choices made by the user

def validChoice(choice):
    if len(choice) != 5:
        return False
    
    elif "_" not in choice:
        return False
    
    else:       
        veri_choice_count = 0

        for n in range(0, 5):
            if n == 0 or n == 1:
                if (ord(choice[n]) >= 65 and ord(choice[n]) <= 90):
                    veri_choice_count += 1
                    continue
                else:
                    print("\n  Input status : INVALID \u2718")
                    return False
                    break

            elif n == 2:
                if choice[n] == "_":
                    veri_choice_count += 1
                    continue
                else:
                    return False
                    break

            else:
                if choice[n] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    veri_choice_count += 1
                    continue
                else:
                    return False
                    break
    
    if veri_choice_count == 5:
        (branch , campus) = choice.split("_")
        if branch in ["CS", "IT", "AD", "AM", "CB", "BS", "EC", "ES", "EV", "EE", "EI", "MC", "ME", "RA", "AE", "MR", "MT", "PR", "CV", "GI", "CH", "MS", "TE", "BM", "BT", "FD", "EV"] and campus in ["01", "02", "03", "04", "05", "06"]:
            return True
        return False
    else:
        return False

    



while True:

    print("===========================================================================================================================================================")
    print("                                                                    IXGVA UNIVERSITY ") 
    print("===========================================================================================================================================================")
    print("                                               | Counselling Portal for Engineering and Technology (B.E/B.Tech) |")
    print("                                               ------------------------------------------------------------------\n")

    print("                                                              *****************************")
    print("                                                              |   1 - LOGIN               |")
    print("                                                              |---------------------------|")
    print("                                                              |   2 - FORGET PASSWORD     |") 
    print("                                                              |---------------------------|")  
    print("                                                              |   3 - REGISTER            |")       
    print("                                                              |---------------------------|")
    print("                                                              |   4 - EXIT PORTAL         |")
    print("                                                              *****************************")

    log_input = str(input("\n\n  ENTER YOUR INPUT : "))
                
    if log_input == "1":
    
        print("\n-----LOGIN-----")
        email = str(input("\n  Enter your E-Mail Address: "))
        pw = str(input("\n  Enter your Password: "))

        df = pd.read_excel(r'C:\Users\jmjee\Downloads\ixgva_university_master_updated_v2.xlsx')

        log_try = 1
        stu = df[(df["EMAIL ID"].astype(str).str.lower() == email.lower()) & (df["PASSWORD"].astype(str) == pw)]

        while stu.empty and log_try < 3:
            print("\n  Input status : INVALID \u2718")
            print(f"  E-Mail Address or Password is incorrect. Attempts left : {3 - log_try}")

            email = str(input("\n  Enter your E-Mail Address: "))
            pw = str(input("\n  Enter your Password: "))

            log_try += 1
            stu = df[(df["EMAIL ID"].astype(str).str.lower() == email.lower()) & (df["PASSWORD"].astype(str) == pw)]

        if stu.empty:
            print("\n  Input status : LOGIN FAILED \u2718")
            print("  Maximum login attempts reached. Use [2 - FORGET PASSWORD] if you cannot remember your password.")
            continue

        else:
            s_row = stu.iloc[0]

            print("\n  Input status : LOGIN SUCCESSFUL \u2714")
            print("\n=================================================================================")
            print("                              STUDENT DASHBOARD")
            print("=================================================================================")

            print(f"\n  Name\n  {s_row['NAME']}")
            print(f"\n  Application Number\n  {s_row['APPLICATION NUMBER']}")
            print(f"\n  Date of birth\n  {str(s_row['DOB'])[:10]}")
            print(f"\n  Community\n  {s_row['CASTE']}")
            print(f"\n  Religion\n  {s_row['RELIGION']}")
            print(f"\n  E-Mail Address\n  {s_row['EMAIL ID']}")
            print(f"\n  Contact Number\n  {s_row['PHONE NUMBER']}")
            print(f"\n  Address\n  {s_row['ADDRESS/LOCATION']}, {s_row['CITY/VILLAGE']}, {s_row['DISTRICT']}, {s_row['STATE']}")
            print(f"\n  Board of Education\n  {s_row['BOARD OF EDUCATION']}")
            print(f"\n  Cutoff Marks\n  {s_row['CUTOFF']}")

            print("\n=================================================================================")
            print("                             PROVISIONAL ALLOTMENT")
            print("=================================================================================")

            if str(s_row["BRANCH"]).upper() == "NOT ALLOTTED":
                print("\n  You have not been allotted any seat in the provisional allotment.")

            else:
                print(f"\n  Alloted Branch\n  {s_row['BRANCH']}")
                print(f"\n  Alloted Campus\n  {s_row['CAMPUS']}")

            print("\n  We wish you great success in your upcoming studies!")
            print("                      THANK YOU !")


    elif log_input == "2":

        print("\n-----FORGET PASSWORD-----")

        df = pd.read_excel(r'C:\Users\jmjee\Downloads\ixgva_university_master_updated_v2.xlsx')

        fp_mail = str(input("\n  Enter your registered E-Mail Address: "))
        fp_stu = df[df["EMAIL ID"].astype(str).str.lower() == fp_mail.lower()]

        if fp_stu.empty:
            print("\n  Input status : INVALID \u2718")
            print("  This E-Mail Address is not registered. Please register first.")
            continue

        print("\n  Input status : VALID \u2714")
        print("\n  Verify your identity to reset the password")

        fp_dob = str(input("\n  Enter your DATE OF BIRTH (DD/MM/YYYY) : "))
        fp_ph = str(input("\n  Enter your registered CONTACT NUMBER : "))

        fp_iso = ""

        if fp_dob.count("/") == 2:
            (fd, fm, fy) = fp_dob.split("/")
            fp_iso = f"{fy}-{fm.zfill(2)}-{fd.zfill(2)}"

        fp_row = fp_stu.iloc[0]

        if fp_iso == str(fp_row["DOB"])[:10] and fp_ph == str(fp_row["PHONE NUMBER"]):
            print("\n  Verification status : SUCCESSFUL \u2714")
            print("\n--------------------------------------------------------------------------------")

            fp_valid = False

            while fp_valid == False:
                new_pw = str(input("\n  ENTER THE NEW PASSWORD : "))

                fp_special = ["!", "@", "#", "$", "%", "^", "&","*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?", "/", "~"]

                if len(new_pw) < 8:
                    print("\n  Input status : WEAK PASSWORD \u2718")
                    print("  Password should contain minimum 8 characters. Try again...")

                elif " " in new_pw:
                    print("\n  Input status : WEAK PASSWORD \u2718")
                    print("  Spaces are not allowed. Try again...")

                elif not (any(ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for ch in new_pw) and any(ch in "abcdefghijklmnopqrstuvwxyz" for ch in new_pw) and any(ch in "0123456789" for ch in new_pw) and any(ch in fp_special for ch in new_pw)):
                    print("\n  Input status : WEAK PASSWORD \u2718")
                    print("  Password should contain numbers, special characters, uppercases and lowercases.")

                elif new_pw == str(fp_row["PASSWORD"]):
                    print("\n  Input status : INVALID \u2718")
                    print("  New password cannot be the same as the old password. Try again...")

                else:
                    re_pw = str(input("\n  RE-ENTER THE NEW PASSWORD : "))

                    if re_pw == new_pw:
                        print("\n  Input status : STRONG PASSWORD \u2714")
                        fp_valid = True
                    else:
                        print("\n  Input status : INVALID \u2718")
                        print("  Passwords do not match. Try again...")

            df.loc[fp_stu.index[0], "PASSWORD"] = new_pw

            try:
                df.to_excel(r'C:\Users\jmjee\Downloads\ixgva_university_master_updated_v2.xlsx', index=False)

                print("\n=================================================================================")
                print("                     PASSWORD RESET SUCCESSFULLY \u2714")
                print("=================================================================================")
                print("\n  You can now login with your new password.")
                print("                      THANK YOU !")

            except PermissionError:
                print("\n  Input status : FAILED \u2718")
                print("  Unable to update the database. Close the Excel file if it is open and try again.")

        else:
            print("\n  Verification status : FAILED \u2718")
            print("  The Date of birth or Contact number does not match our records.")
            continue

    elif log_input == "3":

        print("\n\n                                                         Start your Tech Career with IXGVA University ! \n")
        print("                                               ===============================================================")
        print("                                               |                    REGISTRATION BROCHURE                    |")
        print("                                               ===============================================================")
        print("                                               |                                                             |")
        print("                                               |   I) SIGNING IN                                             |")
        print("                                               |                                                             |")
        print("                                               |      (1)  E-mail Address/ID                                 |")
        print("                                               |                                                             |")
        print("                                               |      (2)  Password                                          |")
        print("                                               |                                                             |")
        print("                                               |-------------------------------------------------------------|")
        print("                                               |                                                             |")
        print("                                               |   II) PERSONAL INFO                                         |")
        print("                                               |                                                             |")
        print("                                               |      (1)  Name of the Student                               |")
        print("                                               |                                                             |")
        print("                                               |      (2)  Date of birth                                     |")
        print("                                               |                                                             |")
        print("                                               |      (3)  Residential Address                               |")
        print("                                               |                                                             |")
        print("                                               |      (4)  City/Town/Village                                 |")
        print("                                               |                                                             |")
        print("                                               |      (5)  District                                          |")
        print("                                               |                                                             |")
        print("                                               |      (6)  State                                             |")
        print("                                               |                                                             |")
        print("                                               |      (7)  Country                                           |")
        print("                                               |                                                             |")
        print("                                               |      (8)  Phone number                                      |")
        print("                                               |                                                             |")
        print("                                               |-------------------------------------------------------------|")
        print("                                               |                                                             |")
        print("                                               |   III) DEMOGRAPHIC INFO                                     |")
        print("                                               |                                                             |")
        print("                                               |      (1)  Caste/Community                                   |")
        print("                                               |                                                             |")
        print("                                               |      (2)  Religion                                          |")
        print("                                               |                                                             |")
        print("                                               |      (3) Mother Tongue                                      |")
        print("                                               |                                                             |")
        print("                                               |-------------------------------------------------------------|")
        print("                                               |                                                             |")
        print("                                               |   IV) ACADEMIC INFO                                         |")
        print("                                               |                                                             |")
        print("                                               |      (1)  Board of Education                                |")
        print("                                               |                                                             |")
        print("                                               |      (2)  Medium of Education                               |")
        print("                                               |                                                             |")
        print("                                               |      (3)  School Name                                       |")
        print("                                               |                                                             |")
        print("                                               |      (4)  Marks obtained in 12th board exam                 |")
        print("                                               |                                                             |")
        print("                                               |           (i)   Mathematics (out of 100)                    |")
        print("                                               |                                                             |")
        print("                                               |           (ii)  Physics (out of 100)                        |")
        print("                                               |                                                             |")
        print("                                               |           (iii) Chemistry (out of 100)                      |")
        print("                                               |                                                             |")
        print("                                               ===============================================================")

        print("\n\n===================================SIGNING IN==================================\n")

        c_mail_ver = False

        while c_mail_ver == False:

            c_mail = str(input("\n  ENTER THE EMAIL ADDRESS/ID : "))
        
            if validEmail(c_mail) == True:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                c_mail_ver = True

            else:
                print("\n  Input status : INVALID \u2718")
                print("  PLease enter the valid e-mail address/ID again...")
                c_mail_ver = False



        s_count = 0
        n_count = 0
        cl_count = 0
        sl_count = 0
        Validity = False

        while Validity == False:
            pw = str(input("\n  ENTER THE PASSWORD : "))

            if len(pw) < 8:
                print("\n  Input status : WEAK PASSWORD \u2718")
                print("  Password should contain minimum 8 characters. Try again...")
                Validity = False

            else:
                for i in pw:
                    if (ord(i) >= 65 and ord(i) <= 90):
                        cl_count += 1
                        continue

                    elif (ord(i) >= 97 and ord(i) <= 122): 
                        sl_count += 1
                        continue

                    elif i in ["!", "@", "#", "$", "%", "^", "&","*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?", "/", "~"]:
                        s_count += 1

                    elif i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        n_count += 1

                    else:
                    
                        print("\n  Input status : WEAK PASSWORD \u2718")
                        print(f"  {i} is not allowed. Try again...")
                        break

                if n_count >= 1 and s_count >= 1 and cl_count >= 1 and sl_count >= 1:
                    print("\n  Input status : STRONG PASSWORD \u2714")
                    Validity = True

                elif " " in pw:
                    print("\n  Input status : WEAK PASSWORD \u2718")
                    print("  Spaces are not allowed. Try again...")
                    Validity = False

                else:
                    print("\n  Input status : WEAK PASSWORD \u2718")
                    print("  Password should contain numbers, special characters, uppercases and lowercases.")
                    Validity = False

        print("\n==================================PERSONAL INFO==================================")
    
        stu_name = str(input("\n  NAME OF THE STUDENT : ")).upper()
        print("\n--------------------------------------------------------------------------------")
        # Verification of Age 

        veri_dob = False

        while veri_dob == False:

            dob = str(input("\n  DATE OF BIRTH : ")).upper()

            if "/" in dob:
                pass
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Wrong format. Please enter in correct format...")
                veri_dob = False

            (dd, mm, yyyy) = dob.split("/")

            for d in dd:
                if d in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    continue
                else:
                    print("\n  Input status : INVALID \u2718")
                    print("  Wrong format. Please enter in correct format...")
                    veri_dob = False
                    break
            for m in mm:
                if m in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    continue
                else:
                    print("\n  Input status : INVALID \u2718")
                    print("  Wrong format. Please enter in correct format...")
                    veri_dob = False
                    break
            for y in yyyy:
                if y in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    continue
                else:
                    print("\n  Input status : INVALID \u2718")
                    print("  Wrong format. Please enter in correct format...")
                    veri_dob = False
                    break

            (bd, bm, by) = (int(dd), int(mm), int(yyyy))

            if (bd >= 1 and bd <= 31) and (bm <= 12 and bm >= 1) and (by >= 1947 and by <= 2026):
                pass

            else:
                print("\n  Input status : INVALID \u2718")
                print("  Wrong format. Please enter in correct format...")
                veri_dob = False

            f = str(date.today())

            (ty, tm, td)= f.split("-")
            (td, tm, ty) = (int(td), int(tm), int(ty))
            y = (ty - by) - 1

            if bm in [1, 3, 5, 7, 8, 11, 12]:
                sd = 31 - bd

            elif bm in [4, 6, 9, 10]:
                sd = 30 - bd

            elif bm == 2:
                if by % 4 == 0 and by % 400 == 0:
                    sd = 29 - bd
                else:
                    sd = 28 - bd
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Wrong format. Please enter in correct format...")
                veri_dob = False


            if bm == 12:
                sd += 0

            else:
                for a in range(bm+1 , 13):
                    if a in [1, 3, 5, 7, 8, 11, 12]:
                        sd += 31
                        continue

                    elif a in [4, 6, 9, 10]:
                        sd += 30
                        continue

                    else:
                        if by % 4 == 0 and by % 400 == 0:
                            sd += 29
                            continue
                        else:
                            sd += 28
                            continue


            for b in range(by+1 , ty):
                if b % 4 == 0 and b % 400 == 0:
                    sd += 366
                else:
                    sd += 365


            if tm == 1:
                sd += td

            for c in range(1, tm):
                if a in [1, 3, 5, 7, 8, 11, 12]:
                    sd += 31
                    continue

                elif a in [4, 6, 9, 10]:
                    sd += 30
                    continue

                else:
                    if by % 4 == 0 and by % 400 == 0:
                        sd += 29
                        continue
                    else:
                        sd += 28
                        continue
                        
            sd += (td + 1)
            a_d = (sd % 365.25)
            deci_age = round((sd / 365.25), 3)

            if deci_age < 16:
                print("\n  Input status : NOT ELIGIBILE \u2718")
                print("  Entered DOB doesn't meet the minimum age required.")
                print("  If wrong DOB is entered, Please enter the correct DOB again...")
                veri_dob = False

            elif deci_age > 30:
                print("\n  Input status : NOT ELIGIBILE \u2718")
                print("  Entered DOB exceeds the maximum age limit.")
                print("  If wrong DOB is entered, Please enter the correct DOB again...")
                veri_dob = False

            else:
                print("\n  Verification status : SUCCESSFUL \u2714")
                print("\n--------------------------------------------------------------------------------")

                veri_dob = True

        veri_resi = False

        while veri_resi == False:
    
            resi_add = str(input("\n  RESIDENTIAL ADDRESS : ")).upper()
    
            if len(resi_add) >= 10:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_resi = True
                pass

            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the valid address again...")
                veri_resi = False

        veri_city = False

        while veri_city == False:

            city = str(input("\n  YOUR CITY / TOWN / VILLAGE: ")).upper()

            if len(city) >= 3:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_city = True
                pass

            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_city = False

        veri_dist = False

        while veri_dist == False:

            dist = str(input("\n  DISTRICT: ")).upper()

            if len(dist) >= 3:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_dist = True
                pass

            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_dist = False

        veri_state = False

        while veri_state == False:

            state = str(input("\n  HOME STATE: ")).upper()

            if len(state) >= 1:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_state = True
                pass

            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_state = False

        veri_ctry = False

        while veri_ctry == False:

            country = str(input("\n  COUNTRY : "))

            if len(country) >= 3:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_ctry = True
                pass

            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_ctry = False

        veri_ph = False

        while veri_ph == False:

            ph = str(input("\n  CONTACT NUMBER : ")).upper()

            if len(ph) == 10:
                for p in ph:
                    if p in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        continue
                    else:
                        print("\n  Input status : INVALID \u2718")
                        print("  Please enter the correct info this time...")
                        veri_ph = False
            
                print("\n  Input status : VALID \u2714")
                veri_ph = True
    
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_ph = False


        print("\n================================DEMOGRAPHIC INFO================================")

        veri_com = False

        while veri_com == False:

            comu = str(input("\n  COMMUNITY / CASTE / CATEGORY : ")).upper()

            if comu in ["OC", "BC", "OBC", "SC", "ST"]:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_com = True
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_com = False

        veri_reli = False

        while veri_reli == False:

            reli = str(input("\n  RELIGION : ")).upper()

            if len(reli) >= 3:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_reli = True
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_reli = False

    
        veri_mt = False

        while veri_mt == False:

            mt = str(input("\n  MOTHER TONGUE : ")).upper()

            if len(mt) >= 3:
                print("\n  Input status : VALID \u2714")
                veri_mt = True
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_mt = False


        print("\n================================ACADEMIC INFO================================")
    

        veri_board = False

        while veri_board == False:

            board = str(input("\n  BOARD OF EDUCATION : ")).upper()

            if len(board) >= 3:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_board = True
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_board = False

        veri_med = False

        while veri_med == False:

            med = str(input("\n  MEDIUM OF EDUCATION : ")).upper()

            if len(med) >= 3:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_med = True
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_med = False

            veri_sch = False

        while veri_sch == False:

            sch = str(input("\n  SCHOOL NAME : ")).upper()

            if len(sch) >= 3:
                print("\n  Input status : VALID \u2714")
                print("\n--------------------------------------------------------------------------------")
                veri_sch = True
            else:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_sch = False

        print("\n  MARKS OBATAINED IN 12TH BOARD EXAM")

        # maths

        veri_math = False

        while veri_math == False:

            maths_str = str(input("\n  MATHEMATICS (out of 100) : "))

            try:
                maths = int(maths_str)

                if maths >= 1 and maths <= 100:
                    print("\n  Input status : VALID \u2714")
                    print("\n--------------------------------------------------------------------------------")
                    veri_math = True
                else:
                    print("\n  Input status : INVALID \u2718")
                    print("  Please enter the correct info this time...")
                    veri_math = False

            except ValueError:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_math = False


        # physics

        veri_phy = False

        while veri_phy == False:

            phy_str = str(input("\n  PHYSICS (out of 100) : "))

            try:
                phy = int(phy_str)

                if phy >= 1 and phy <= 100:
                    print("\n  Input status : VALID \u2714")
                    print("\n--------------------------------------------------------------------------------")
                    veri_phy = True
                else:
                    print("\n  Input status : INVALID \u2718")
                    print("  Please enter the correct info this time...")
                    veri_phy = False

            except ValueError:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_phy = False

        # chemistry

        veri_chem = False

        while veri_chem == False:

            chem_str = str(input("\n  CHEMISTRY (out of 100) : "))

            try:
                chem = int(chem_str)

                if chem >= 1 and chem <= 100:
                    print("\n  Input status : VALID \u2714")
                    print("\n=================================================================================")
                    veri_chem = True
                else:
                    print("\n  Input status : INVALID \u2718")
                    print("  Please enter the correct info this time...")
                    veri_chem = False

            except ValueError:
                print("\n  Input status : INVALID \u2718")
                print("  Please enter the correct info this time...")
                veri_chem = False

    
        agg_mark = maths + ((chem/100) * 50) + ((phy/100) * 50)
   


        print("                        REGISTRATION SUCCESSFUL \u2714")
        print("=================================================================================")
        cf_input = input("\nShall we proceed to the choice filling process? [Y] or [N] : ").upper()

        if cf_input == "N":
            print("You can login and go for the choice filling process anytime")
            print("THANK YOU !!!\n")

            continue
    
        elif cf_input == "Y":
            print("\n\n                                                              Make your choices wiser ! \n")
            print("                                               ===============================================================")
            print("                                               |                   CHOICE FILLING BROCHURE                   |")
            print("                                               ===============================================================")
            print("                                               |                                                             |")
            print("                                               |   BRANCH CODES:                                             |")
            print("                                               |                                                             |")
            print("                                               |   CS - Computer Science and Engineering                     |")
            print("                                               |   IT - Information Technology                               |")
            print("                                               |   AD - Artificial Intelligence and Data Science             |")
            print("                                               |   AM - Artificial Intelligence and Machine Learning         |")
            print("                                               |   CB - Cyber security                                       |")
            print("                                               |   BS - Computer Science and Business Systems                |")
            print("                                               |   EC - Electronics and Communication Enginneering           |")  
            print("                                               |   EV - ECE (VLSI Technology and Chip design)                |")
            print("                                               |   EE - Electricals and Electronics Engineering              |")
            print("                                               |   EI - Electronics and Instrumentation Enginneering         |")
            print("                                               |   MC - Mechanical Engineering                               |")
            print("                                               |   ME - Mechatronics Engineering                             |")
            print("                                               |   RA - Robotics and Automation Engineering                  |")
            print("                                               |   AE - Aerospace Engineering                                |")
            print("                                               |   MR - Marine Engineering                                   |")
            print("                                               |   MT - Metallurigical Engineering                           |")
            print("                                               |   PR - Printing Technology                                  |")
            print("                                               |   CV - Civil Engineering                                    |")
            print("                                               |   GI - Geoinformatics Engineering                           |")
            print("                                               |   CH - Chemical Engineering                                 |")
            print("                                               |   MS - Material Science and Engineering                     |")
            print("                                               |   TF - Textile & Fashion Technology                         |")
            print("                                               |   BM - Biomedical Engineering                               |")
            print("                                               |   BT - Biotechnology                                        |")
            print("                                               |   FD - Food Technology                                      |")
            print("                                               |                                                             |")
            print("                                               |-------------------------------------------------------------|")
            print("                                               |                                                             |")
            print("                                               |   CAMPUS CODES:                                             |")
            print("                                               |                                                             |")
            print("                                               |   01 - Chennai                                              |")
            print("                                               |   02 - Mumbai                                               |")
            print("                                               |   03 - Bengaluru                                            |")
            print("                                               |   04 - Noida                                                |")
            print("                                               |   05 - Hyderabad                                            |")
            print("                                               |   06 - Kolkata                                              |")
            print("                                               |                                                             |")
            print("                                               |-------------------------------------------------------------|")
            print("                                               |                                                             |")
            print("                                               |   SAMPLE INPUT FORMAT: CS_02                                |")
            print("                                               |                                                             |")
            print("                                               |   CS -> Computer Science and Engineering                    |")
            print("                                               |   02 -> Mumbai Campus                                       |")
            print("                                               |                                                             |")
            print("                                               |-------------------------------------------------------------|")
            print("                                               |                                                             |")
            print("                                               |   RESETTING, SUBMITTING AND CONFIRMATION:                   |")
            print("                                               |                                                             |")
            print("                                               |   * Enter 0 to reset the choice list and start filling      |")
            print("                                               |     your preferences afresh.                                |")
            print("                                               |                                                             |")
            print("                                               |   * Enter 1 to submit your choice list.                     |")
            print("                                               |                                                             |")
            print("                                               |   * Once the final confirmation of the choice list is       |")
            print("                                               |     made, you cannot make changes later. Confirmed          |")
            print("                                               |     choice list will get locked and will proceeded for the  |")
            print("                                               |     counselling process.                                    |")
            print("                                               |                                                             |")
            print("                                               ===============================================================")
    
        
            branch_codes = ["CS", "IT", "AD", "AM", "CB", "BS", "EC", "ES", "EV", "EE", "EI", "MC", "ME", "RA", "AE", "MR", "MT", "PR", "CV", "GI", "CH", "MS", "TE", "BM", "BT", "FD", "EV"]
        
            branch_names = ["COMPUTER SCIENCE AND ENGINEERING",
                            "INFORMATION TECHNOLOGY",
                            "ARTIFICIAL INTELLIGENCE AND DATA SCIENCE",
                            "ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING",
                            "CYBER SECURITY",
                            "COMPUTER SCIENCE AND BUSINESS SYSTEMS",
                            "ELECTRONICS AND COMMUNICATION ENGINNEERING",
                            "ECE (EMBEDDED SYSTEM)",
                            "ECE (VLSI TECHNOLOGY AND CHIP DESIGN)",
                            "ELECTRICALS AND ELECTRONICS ENGINEERING",
                            "ELECTRONICS AND INSTRUMENTATION ENGINNEERING",
                            "MECHANICAL ENGINEERING",
                            "MECHATRONICS ENGINEERING",
                            "ROBOTICS AND AUTOMATION ENGINEERING",
                            "AEROSPACE ENGINEERING",
                            "MARINE ENGINEERING",
                            "METALLURIGICAL ENGINEERING",
                            "PRINTING TECHNOLOGY",
                            "CIVIL ENGINEERING",
                            "GEO-INFORMATICS ENGINEERING",
                            "CHEMICAL ENGINEERING",
                            "MATERIAL SCIENCE AND ENGINEERING",
                            "TEXTILE ENGINEERING",
                            "BIOMEDICAL ENGINEERING",
                            "BIOTECHNOLOGY",
                            "AGRICULTURAL AND FOOD TECHNOLOGY",
                            "ENVIRONMENTAL ENGINEERING"]
        
            campus_codes = ["01", "02", "03", "04", "05", "06"]

            campus_names = ["CHENNAI","MUMBAI","BENGALURU","NOIDA","HYDERABAD","KOLKATA"]

            seats_100 = ["CS", "AD", "AM", "CB", "EC", "EE", "MC", "CV"]

            seats_70 = ["EV", "BS", "BT", "BM", "RA", "EI", "AE", "MS", "GI"]

            seats_50 = ["PR", "TF", "FD", "ME", "MR", "MT", "CH"]
        

            choice_no = 0
            choice_list = []
            ch_br = []
            ch_cp = []
            choice_lim = False

            while choice_lim == False:

                veri_choice = False
                choice_no += 1

                while veri_choice == False:

                    choice_f = str(input(f"\n  ENTER YOUR CHOICE NO.{choice_no} : ")).upper()

                    if choice_f == "1":
                        print("\n  Input status : SUBMITTED SUCCESSFULLY \u2714")
                        print("\n--------------------------------------------------------------------------------")
                        print("\n  YOUR IXGVA UNIVERSITY CHOICE LIST : ")
                        print("--------------------------------------------------------------------------------")

                        cnn = 0
        
                        for chs in choice_list:
                            (br, cp) = chs.split("_")
                            br_ind = branch_codes.index(br)
                            cp_ind = campus_codes.index(cp)

                            brn = branch_names[br_ind]
                            cpn = campus_names[cp_ind]

                            cnn += 1
                            print(f"  CHOICE NO.{cnn} -> {brn} at {cpn} Campus")
                            print("--------------------------------------------------------------------------------")
                        
                        veri_conf = False

                        while veri_conf == False:
                            conf = str(input("  \nDo you want to confirm this choice list? [Y] or [N] : ")).upper()

                            if conf == "Y":
                                print("\n=================================================================================")
                                print("                   CHOICE LIST HAS BEEN FREEZED SUCCESSFULLY \u2714")
                                print("=================================================================================")
                                choice_lim = True
                                veri_choice = True
                                veri_conf = True 

                            elif conf == "N":
                                choice_list.clear()
                                print("\n  Input status : RESET \u2714")
                                print("\n=================================================================================")
                                print("\n  Choice list has been RESET. Please fill your choices wisely again...")
                                choice_no = 1
                                cnn = 0
                                choice_lim = False
                                veri_choice = False
                                veri_conf = True

                            else:
                                print("\n  Input status : INVALID \u2718")
                                veri_conf = False


                    elif choice_f == "0":
                        choice_list.clear()
                        print("\n  Input status : RESET \u2714")
                        print("\n=================================================================================")
                        print("\n  Choice list has been RESET. Please fill your choices wisely again...")
                        choice_no = 1
                        cnn = 0
                        veri_choice = False
                        choice_lim = False

                    elif choice_f in choice_list:
                        print("\n  Input status : INVALID \u2718")
                        ind = choice_list.index(choice_f) + 1
                        print(f"  This choice has already been given at the CHOICE NO.{ind}")
                        veri_choice = False

                    elif validChoice(choice_f) == True:
                        choice_list.append(choice_f)
                        print("\n  Input status : VALID \u2714")
                        print("\n--------------------------------------------------------------------------------")
                        veri_choice = True

                    else:
                        print("\n  Input status : INVALID \u2718")
                        print("  Please enter the choices in correct format as mentioned in the Choice filling brochure")
                        veri_choice = False

        
            am = str(input("\n  Would you like to proceed to the provisional allotment? [Y] or [N] :  ")).upper()

            if am == "Y":

                df = pd.read_excel(r'C:\Users\jmjee\Downloads\ixgva_university_master_updated_v2.xlsx')

                allot = []

                for z in choice_list:
                    (brr , cpp) = z.split("_")

                    brs = branch_names[branch_codes.index(brr)]
                    cps = campus_names[campus_codes.index(cpp)]

                    gen_pool = df[(df["BRANCH"] == brs) & (df["CAMPUS"] == cps)]
                    res_pool = df[(df["BRANCH"] == brs) & (df["CAMPUS"] == cps) & (df["CASTE"] == comu)]

                    sorted_gen_pool = gen_pool.sort_values(by="CUTOFF", ascending=False)
                    sorted_res_pool = res_pool.sort_values(by="CUTOFF", ascending=False)

                    res_comu = ["OBC", "SC", "ST", "EWS"]
                    res = [0.27, 0.15, 0.8, 0.1]

                    if brr in seats_100:
                        if comu not in res_comu:
                            caste_seats = int(100 * 0.40)
                            if not sorted_gen_pool.empty:
                                seat_index = min(caste_seats - 1, len(sorted_gen_pool) - 1)
                                closing_cutoff = sorted_gen_pool.iloc[caste_seats - 1]["CUTOFF"]

                                if agg_mark > closing_cutoff:
                                    allot.append(z)
                                    break
                                else:
                                    continue
                        else:
                            caste_index = res_comu.index(comu)
                            caste_seats = int(100 * res[res_comu.index(brr)])
                            if not sorted_res_pool.empty:
                                seat_index = min(caste_seats - 1, len(sorted_res_pool) - 1)
                                closing_cutoff = sorted_res_pool.iloc[caste_seats - 1]["CUTOFF"]

                                if agg_mark > closing_cutoff:
                                    allot.append(z)
                                    break
                                else:
                                    continue

                if len(allot) > 0:
                    (abr , acp) = allot[0].split("_")
                    abrn = branch_names[branch_codes.index(abr)]
                    acpn = campus_names[campus_codes.index(acp)]

                    new_stu = {"NAME": stu_name, 
                                "DOB": dob,
                                "CASTE": comu, 
                                "RELIGION": reli,
                                "EMAIL ID": c_mail,
                                "PASSWORD": pw,
                                "CUTOFF": agg_mark,
                                "ADDRESS/LOCATION": resi_add,
                                "CITY/VILLAGE": city,
                                "DISTRICT": dist,
                                "STATE": state,
                                "PHONE NUMBER": ph,
                                "BOARD OF EDUCATION": board,
                                "BRANCH": abrn,
                                "CAMPUS": acpn}

                else:
                    new_stu = {"NAME": stu_name, 
                                "DOB": dob,
                                "CASTE": comu, 
                                "RELIGION": reli,
                                "EMAIL ID": c_mail,
                                "PASSWORD": pw,
                                "CUTOFF": agg_mark,
                                "ADDRESS/LOCATION": resi_add,
                                "CITY/VILLAGE": city,
                                "DISTRICT": dist,
                                "STATE": state,
                                "PHONE NUMBER": ph,
                                "BOARD OF EDUCATION": board,
                                "BRANCH": "NOT ALLOTTED",
                                "CAMPUS": "NOT ALLOTTED"}


                
                save_stu = dict(new_stu)

                (sv_d, sv_m, sv_y) = dob.split("/")

                save_stu["DOB"] = f"{sv_y}-{sv_m.zfill(2)}-{sv_d.zfill(2)}"
                save_stu["PHONE NUMBER"] = int(ph)
                save_stu["S.NO"] = int(df["S.NO"].max()) + 1
                save_stu["APPLICATION NUMBER"] = int(df["APPLICATION NUMBER"].max()) + 1

                df = pd.concat([df, pd.DataFrame([save_stu])[list(df.columns)]], ignore_index=True)

                try:
                    df.to_excel(r'C:\Users\jmjee\Downloads\ixgva_university_master_updated_v2.xlsx', index=False)
                    print(f"\n  Your APPLICATION NUMBER : {save_stu['APPLICATION NUMBER']}")

                except PermissionError:
                    print("\n  Input status : FAILED \u2718")
                    print("  Unable to save your data. Close the Excel file if it is open and try again.")

                print("\n=================================================================================")
                print("                             PROVISIONAL ALLOTMENT \u2714")
                print("=================================================================================")

                print(f"\n  Name\n  {stu_name}")
                print(f"\n  Date of birth\n  {dob}")
                print(f"\n  Age\n  {deci_age}")
                print(f"\n  Community\n  {comu}")
                print(f"\n  Cutoff Marks\n  {agg_mark}")
                print(f"\n  Alloted Branch\n {abrn}")
                print(f"\n  Alloted Campus\n {acpn}")

                print("\n  We wish you great success in your upcoming studies!")
                print("                      THANK YOU !")

    elif log_input == "4":

        print("\n=================================================================================")
        print("                      THANK YOU FOR VISITING IXGVA UNIVERSITY !")
        print("                              EXITING THE PORTAL ...")
        print("=================================================================================")
        break

    else:
        print("\n  Input status : INVALID \u2718")
        print("  Please enter 1, 2, 3 or 4 only.")