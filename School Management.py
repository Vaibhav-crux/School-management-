
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((

                                                #THE CODE IS     (1021)     FOR ADMISSION

#)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

print("\t \t      !!!!!!J.P EDUCATION ACADEMY!!!!!! \n \t \t       !!!!! NATHMALPUR (Gorakhpur)!!! \n ************************************************************************************************************************************")
def options():
    print("\t\t\t\t\t__________________________________")
    print("\t\t\t\t\t! Office work CODE               !")
    print("\t\t\t\t\t! Teacher work CODE              !")
    print("\t\t\t\t\t! School head  CODE              !")
    print("\t\t\t\t\t! For exit write exitjpea        !")
    print("\t\t\t\t\t__________________________________")
#------------------------------------------------------------------------------------------------------------------------------------
    print("*******************************************Write the code which you want to access***************************************************")
    a=input("Enter the code = JPEA-")
    if(a.isalnum()==True):
        pass
        if(a=='1021'):
            print("\t \t \t------- You are in OFFICE WORK --------")
            print("####################################################################################################################################")
            home1()
        elif(a=='exitjpea'):
            exit(options)
        else:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@You entered the wrong code@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("=====================================================PLEASE TRY AGAIN===============================================================")
            options()
            return
    else:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@You entered any alphabets or sing which is invalid in code@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("=====================================================PLEASE TRY AGAIN===============================================================")
        options()
        return

#Work to dO (..........................................PENDING.................................................................................)
#
#
#
#
#            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def home1():
    print("\t \t \t\t ===============================")
    print("\t \t \t\t[ For Admission press 1         ]")
    print("\t \t \t\t[ For Fees list press 2         ]")
    print("\t \t \t\t[ For Conveyance list press 3   ]")
    print("\t \t \t\t[ For Submit Fee press 4        ]")
    print("\t \t \t\t[ For School calander press 5   ]")
    print("\t \t \t\t[ For exist press 6             ]")
    print("\t \t \t\t ===============================")
#-----------------------------------------------------------------------------------------------------------------------------------------------
    print("*************************************************************************************************************************************")
    m=input("\t \t \t Choose option from given menues  :  ")
    if(m.isdigit()==True):
        pass
        print("*******************************You have Choosen option  ",m,"  ************************************************************************")
        if(m=='1'):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Admission then press 1 \n\t\t\t\t\tIf you want to go any other option then press 2 \n\t\t\t\t\tIf you want to exit then press 3")
            print("\t\t\t\t\tIf want to change the work place(WANT TO GO ANY OTHER STREAM) then press 4") 
            ad=input("Enter the anyone option's given upward = ")
            while(ad.isdigit()==True):
                if(ad=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    admission()
                elif(ad=="2"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tRESETED")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    home1()
                elif(ad=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBYE... BYE...")
                    exit(home1)
                elif(ad=="4"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````\n\n\n")
                    options()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^You given any other option's except the choce's which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    home1()
            while(ad.isdigit()!=True):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^You given alphabet's or sing which is invalid ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                ad=input("Enter the anyone option's given upward = ")
        elif(m=='2'):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Fee list then press 1 \n\t\t\t\t\tIf you want to go any other option then press 2 \n\t\t\t\t\tIf you want to exit then press 3")
            print("\t\t\t\t\tIf want to change the work place(WANT TO GO ANY OTHER STREAM) then press 4") 
            ad=input("Enter the anyone option's given upward = ")
            while(ad.isdigit()==True):
                if(ad=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO FEE LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    Feelist()
                elif(ad=="2"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tRESETED")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    home1()
                elif(ad=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBYE... BYE...")
                    exit(home1)
                elif(ad=="4"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````\n\n\n")
                    options()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^You given any other option's except the choce's which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    home1()
            while(ad.isdigit()!=True):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the alphabet's or sing which is invalid ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                ad=input("Enter the anyone option's given upward = ")
        elif(m=='3'):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Conveyance list then press 1 \n\t\t\t\t\tIf you want to go any other option then press 2 \n\t\t\t\t\tIf you want to exit then press 3")
            print("\t\t\t\t\tIf want to change the work place(WANT TO GO ANY OTHER STREAM) then press 4") 
            ad=input("Enter the anyone option's given upward = ")
            while(ad.isdigit()==True):
                if(ad=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO conveyance LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    conveyance()
                elif(ad=="2"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tRESETED")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    home1()
                elif(ad=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBYE... BYE...")
                    exit(home1)
                elif(ad=="4"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````\n\n\n")
                    options()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^You given any other option's except the choce's which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    home1()
            while(ad.isdigit()!=True):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                ad=input("Enter the anyone option's given upward = ")
        elif(m=="4"):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Fee's subbmission then press 1 \n\t\t\t\t\tIf you want to go any other option then press 2 \n\t\t\t\t\tIf you want to exit then press 3")
            print("\t\t\t\t\tIf want to change the work place(WANT TO GO ANY OTHER STREAM) then press 4") 
            ad=input("Enter the anyone option's given upward = ")
            while(ad.isdigit()==True):
                if(ad=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO Fee's subbmission")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    submitfee()
                elif(ad=="2"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tRESETED")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    home1()
                elif(ad=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBYE... BYE...")
                    exit(home1)
                elif(ad=="4"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````\n\n\n")
                    options()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^You given any other option's except the choce's which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    home1()
            while(ad.isdigit()!=True):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                ad=input("Enter the anyone option's given upward = ")
        elif(m=="5"):
            School_calander()
        elif(m=="6"):
            exit(home1)
        else:
            home1()
            return
    else:
        print("*************************************************************************************************************************************")
        home1()
        return
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def admission():
#------------------------------------------------------------------------------------------------------------------------------------------------
    sn=input("Enter student first name  :  ")                             #STUDENT FIRST NAME
    while(sn.isalpha()==True):
        if(len(sn)>=3 or sn=="Om" or sn=="OM" or sn=="om"):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^The name is not of one / two letters^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            sn=input("Enter student first name  :  ")
    while(sn.isalpha()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the digit or sing which is invalid in student name^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        sn=input("Enter student first name  :  ")          
        
#------------------------------------------------------------------------------------------------------------------------------------------------
    ssn=input("Enter student last name  :  ")                             #STUDENT LAST NAME
    while(ssn.isalpha()==True):
        if(len(ssn)>=3):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^The name is not of one / two letters^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            ssn=input("Enter student last name  :  ")
    while(ssn.isalpha()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the digit or sing which is invalid in title of student^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        ssn=input("Enter student last name  :  ")
#----------------------------------------------------------------------------------------------------------------------------------------------       
    fn=input("Enter student Father first name  :  ")                      #STUDENT FATHER NAME
    while(fn.isalpha()==True):
        if(len(fn)>=2):
            print("\t \t \t\t \t \t##########################################")
            print("\t \t \t\t \t \t Student father full name is",fn,ssn)
            print("\t \t \t\t \t \t##########################################")
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^The name is not of one letters^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            fn=input("Enter student Father first name  :  ")
            pass
    while(fn.isalpha()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^You given the digit or sing which is invalid in Father's name^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        fn=input("Enter student father first name  :  ")
        pass
        print("\t \t \t\t \t \t##########################################")
        print("\t \t \t\t \t \t Student father name is",fn,ssn)
        print("\t \t \t\t \t \t##########################################")
#---------------------------------------------------------------------------------------------------------------------------------------------   
    mn=input("Enter student Mother first name  :  ")                      #STUDENT MOTHER NAME
    while(mn.isalpha()==True):
        if(len(mn)>=2):
            print("\t \t \t\t \t \t##########################################")
            print("\t \t \t\t \t \t Student mother full name is",mn,ssn)
            print("\t \t \t\t \t \t##########################################")
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^The name is not of one / two letters^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            mn=input("Enter student Mother first name  :  ")
            pass
    while(mn.isalpha()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the digit or sing which is invalid in Mother's name^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        mn=input("Enter student mother first name  :  ")
        pass
        print("\t \t \t\t \t \t##########################################")
        print("\t \t \t\t \t \t Student mother full name is",mn,ssn)
        print("\t \t \t\t \t \t##########################################")
#---------------------------------------------------------------------------------------------------------------------------------------------
    ad=input("Enter student Admission Number  :  ")                 #ADMISSION NUMBER        
    while(ad.isdigit()==True):                                   
        l=len(ad)
        if(l>=1 and l<=5):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^You given the value less then one or more then 10,000 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            ad=input("Enter student Admission Number  :  ")
    while(ad.isdigit()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^You given the alphabets or sign which is invalid in admission^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        ad=input("Enter student admission number :  ")
#----------------------------------------------------------------------------------------------------------------------------------------------
    cs=input("Enter the Student class : ")                              #STUDENT CLASS 
    while(cs.isalnum()==True):
        if(cs=="playway".upper() or cs=="lkg".upper() or cs=="nursery".upper or cs=="ukg".upper or cs=="1" or cs=="2" or cs=="3" or cs=="4" or cs=="5" or cs=="6" or cs=="7" or cs=="8" or cs=="9" or cs=="10" or cs=="11" or cs=="12"):
            if(cs=="11" or cs=="12"):
                print(".Maths\n.Bio\n.Commerse")
                st=input("Enter the stream which you want to study = ")
                if(st.isalpha()==True):
                    if(st=="Maths" or st=="Bio" or st=="Commerse"):
                        break
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("^^^^^^^^^^^^^^^^^You written something else except given options which is invalid in stream^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                        pass
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the digit's or sing which is invalid in Stream^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            else:
                break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid class expect Playway - 12^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            cs=input("Enter the Student class : ")
            continue
    while(cs.isalnum()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the sing which is invalid in class^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        cs=input("Enter the Student class : ")
#---------------------------------------------------------------------------------------------------------------------------------------------
    fo=input("Father occupassion  :  ")                             #STUDENT FATHER OCCUPISSION
    z=" "
    while(fo.isalpha()==True and z in fo):
        if(len(fo)>=5):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the smaller characters then 5 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            fo=input("Father occupassion  :  ")
    while(fo.isalpha()!=True and z not in fo):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the digit or sing which is invalid in Father occupassion^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        fo=input("Father occupassion :  ")
#----------------------------------------------------------------------------------------------------------------------------------------------
    mo=input("Mother occupission  :  ")                              #STUDENT MOTHER OCCUPISSION
    x=" "
    while(mo.isalpha()==True and x in mo):
        if(len(mo)>=5):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the smaller characters then 5 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            mo=input("Mother occupission  :  ")
            pass
    while(mo.isalpha()!=True and x not in mo):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the digit or sing which is invalid in Mother occupassion^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        mo=input("Mother occupission :  ")
#----------------------------------------------------------------------------------------------------------------------------------------------
    ps=input("Previous school name  :  ")                            #PREVIOUS SCHOOL NAME
    y="."
    y1=" "
    while(ps.isalpha()==True and y in ps and y1 in ps):
        if(len(ps)>=6):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the smaller characters then 6 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            ps=input("Previous school name  :  ")  
            pass
    while(ps.isalpha()!=True and y not in ps and y1 not in ps):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the digit or sing{except(.)(space)} which is invalid in School's name^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        ps=input("Previous school name  :  ")
#-----------------------------------------------------------------------------------------------------------------------------------------------
    sa=input("Student Address  :  ")                      #STUDENT ADDRESS
    a=" "
    b="-"
    while(sa.isalnum()==True and a in sa and b in sa):
        break
    while(sa.isalnum()!=True and a not in sa and b not in sa):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given the sing{except(-)(space)}  which is invalid in student adress^^^^^^^^^^^^^^^^^^^^^^^^^")
        sa=input("Student Address  :  ") 
#------------------------------------------------------------------------------------------------------------------------------------------------
    mn=input("Enter the phone number = ")                            #STUDENT PHONE NUMBER
    while(mn.isdigit()==True):
        l=len(mn)
        if(l==10):
            if(mn>="6" or mn<="10"):
                break
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^You have given the number which is starting from 1-5 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                mn=input("Enter the phone number =  ")
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the less or higher then 10 digits which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            mn=input("Enter the phone number =  ")
    while(mn.isdigit()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^You have given alphabets or sing which is invalid in phone number^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        mn=input("Enter the phone number =  ")
#--------------------------------------------------------------------------------------------------------------------------------------------------
    sg=input("Enter the student Gender (Male / M / m  or  Female / F/ f  or  Other / O/ o ) = ")  #STUDENT GENDER
    while(sg.isalpha()==True):
        pass
        if(sg=="MALE" or sg=="M" or sg=="male" or sg=="m"):
            break
        elif(sg=="FEMALE" or sg=="F" or sg=="female" or sg=="f"):
            break
        elif(sg=="OTHER" or sg=="o" or sg=="other" or sg=="O"):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given any else gender except M/ F/ O^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            sg=input("Enter the syudent Gender (Male / M / m  or  Female / F/ f) =  ")
    while(sg.isalpha()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given digit or sing which is invalid in gender^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        sg=input("Enter the syudent Gender (Male / M / m  or  Female / F/ f) =  ")
#-------------------------------------------------------------------------------------------------------------------------------------------------
    print("\t \t \t============================================================================")
    print("\t \t \t% If you want to give the ADDHAR NUMBER of student then press Y/y          %")    #ADDHAR NUMBER
    print("\t \t \t% If you did not want to give the ADDHAR NUMBER of student then press N/n  %")
    print("\t \t \t============================================================================")
    ao=input("Enter your choice = ")
    while(ao.isalpha()==True):
        if(ao=="Y" or ao=="y"):
            an=input("Enter your addhar number = ")
            if(an.isdigit()==True):
                if(len(an)==16):
                    break
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given less or higher digit then 16 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used alphabets or sing in Addhar Number which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                pass
        elif(ao=="N" or ao=="n"):
            break
        else:
            print("\t \t \t============================================================================")
            print("\t \t \t% If you want to give the ADDHAR NUMBER of student then press Y/y          %")
            print("\t \t \t% If you did not want to give the ADDHAR NUMBER of student then press N/n  %")
            print("\t \t \t============================================================================")
            ao=input("Enter your choice = ")
            if(ao.isalpha()==True):
                if(ao=="Y" or ao=="y"):
                    an=input("Enter your addhar number = ")
                    if(an.isdigit()==True):
                        if(len(an)==16):
                            break
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given less or higher digit then 16 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            pass
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used alphabets or sing in Addhar Number which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                        pass
                if(ao=="N" or ao=="n"):
                    break
    while(ao.isalpha()!=True):
        print("\t \t \t============================================================================")
        print("\t \t \t% If you want to give the ADDHAR NUMBER of student then press Y/y          %")
        print("\t \t \t% If you did not want to give the ADDHAR NUMBER of student then press N/n  %")
        print("\t \t \t============================================================================")
        ao=input("Enter your choice = ")
        pass
        if(ao=="Y" or ao=="y"):
            an=input("Enter your addhar number = ")
            if(an.isdigit()==True):
                if(len(an)==16):
                    break
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given less or higher digit then 16 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used alphabets or sing in Addhar Number which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                pass
        elif(ao=="N" or ao=="n"):
            break
        else:
            print("\t \t \t============================================================================")
            print("\t \t \t% If you want to give the ADDHAR NUMBER of student then press Y/y          %")
            print("\t \t \t% If you did not want to give the ADDHAR NUMBER of student then press N/n  %")
            print("\t \t \t============================================================================")
            ao=input("Enter your choice = ")
            if(ao.isalpha()==True):
                if(ao=="Y" or ao=="y"):
                    an=input("Enter your addhar number = ")
                    if(an.isdigit()==True):
                        if(len(an)==16):                            
                            break
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given less or higher digit then 16 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            pass
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used alphabets or sing in Addhar Number which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                        pass
                if(ao=="N" or ao=="n"):
                    break
#-------------------------------------------------------------------------------------------------------------------------------------------------
    print( "\t \t \t************************************************************************")     #STUDENT BROTHER DETALILS
    print(" \t \t \t*  If you have any brother in this school then press Y/y               *")
    print(" \t \t \t*                   Otherwise press n to Skip                          *")
    print( "\t \t \t************************************************************************")
    esb=input("Choose the options given upward = ")
    while(esb.isalpha()==True):
        if(esb=="y" or esb=="Y"):
            im=input("Enter the brother first name Ist = ")
            if(len(im)>=3 or im=="om" or im=="OM" or im=="Om"):
                if(im.isalpha()==True):
                    print("---------------------------------------------")
                    print("press 1 if you having one more brother \npress any key if you didn't having one more brother")
                    print("---------------------------------------------")
                    oo=input("choose any one option which given upward = ")
                    if(oo=="1"):
                        pass
                    else:
                        break
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used digit's or sing in brother name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^You given less then 3 alphabets in brother name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                pass
        elif(esb=="n" or esb=="N"):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^You given any other option (except y or n) in brother name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            esb=input("Choose the options given upward = ")
    while(esb.isalpha()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used digit's or sing in brother name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        esb=input("Choose the options given upward = ")
        pass
        if(esb=="y" or esb=="Y"):
            im=input("Enter the brother first name Ist = ")
            if(len(im)>=3 or im=="om" or im=="OM" or im=="Om"):
                if(im.isalpha()==True):
                    print("---------------------------------------------")
                    print("press 1 if you having one more brother \npress any key if you didn't having one more brother")
                    print("---------------------------------------------")
                    oo=input("choose any one option which given upward = ")
                    if(oo=="1"):
                        pass
                    else:
                        break
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used digit's or sing in brother name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^You given less then 3 alphabets in brother name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                pass
        elif(esb=="n" or esb=="N"):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^You given any other option (except y or n) in brother name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            esb=input("Choose the options given upward = ")

#-------------------------------------------------------------------------------------------------------------------------------------------------
    print( "\t \t \t************************************************************************")     #STUDENT SISTER DETALILS
    print(" \t \t \t*  If you have any sister in this school then press Y/y                *")
    print(" \t \t \t*                   Otherwise press n to Skip                          *")
    print( "\t \t \t************************************************************************")
    ess=input("Choose the options given upward = ")
    while(ess.isalpha()==True):
        if(ess=="y" or ess=="Y"):
            im=input("Enter the sister first name Ist = ")
            if(len(im)>=3 or im=="om" or im=="OM" or im=="Om"):
                if(im.isalpha()==True):
                    print("---------------------------------------------")
                    print("press 1 if you having one more sister \npress any key if you didn't having one more sister")
                    print("---------------------------------------------")
                    oo=input("choose any one option which given upward = ")
                    if(oo=="1"):
                        pass
                    else:
                        break
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used digit's or sing in sister name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^You given less then 3 alphabets in sister name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                pass
        elif(ess=="n" or ess=="N"):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^You given any other option (except y or n) in sister name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            ess=input("Choose the options given upward = ")
    while(ess.isalpha()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used digit's or sing in sister name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        ess=input("Choose the options given upward = ")
        pass
        if(ess=="y" or ess=="Y"):
            im=input("Enter the sister first name Ist = ")
            if(len(im)>=3 or im=="om" or im=="OM" or im=="Om"):
                if(im.isalpha()==True):
                    print("---------------------------------------------")
                    print("press 1 if you having one more sister \npress any key if you didn't having one more sister")
                    print("---------------------------------------------")
                    oo=input("choose any one option which given upward = ")
                    if(oo=="1"):
                        pass
                    else:
                        break
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used digit's or sing in sister name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^You given less then 3 alphabets in sister name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                pass
        elif(ess=="n" or ess=="N"):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^You given any other option (except y or n) in sister name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            ess=input("Choose the options given upward = ")
#-------------------------------------------------------------------------------------------------------------------------------------------------
    lg=input("Name the first name of (OTHER) local parent = ")                                #LOCAL PARENTS FIRST NAME
    while(lg.isalpha()==True):
        if(len(lg)>=2):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^You given less then 2 alphabets in parent's name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            lg=input("Name the first name of(OTHER) local parent = ") 
            pass
    while(lg.isalpha()==False):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^You have given digit or sing which is invalid in parent's name^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        lg=input("Name the first name of(OTHER) local parent = ") 
#-------------------------------------------------------------------------------------------------------------------------------------------------
    llg=input("Name the last name of (OTHER) local parent = ")                                #LOCAL PARENTS SECOND NAME
    while(llg.isalpha()==True):
        if(len(llg)>=3):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^You given less then 3 alphabets in parent's name which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            llg=input("Name the last name of(OTHER) local parent = ")   
            pass
    while(llg.isalpha()==False):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^You have given digit or sing which is invalid in parent's title^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        llg=input("Name the last name of(OTHER) local parent = ")   
#-------------------------------------------------------------------------------------------------------------------------------------------------
    en=input("Enter the Code number of your area (G.K.P) = 273-")                 #PINCODE OF THE AREA(G.K.P)
    while(en.isdigit()==True):
        if(len(en)==3):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^You given less or higher value then 3 digit's in G.K.P Code which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            en=input("Enter the Code number of your area  (G.K.P) = 273")
    while(en.isdigit()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("^^^^^^^^^^^^^^^^^^^^^^^You have given alphabets or sing which is invalid in G.K.P Code^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        en=input("Enter the Code number of your area  (G.K.P) = 273-")
#-------------------------------------------------------------------------------------------------------------------------------------------------
        

                                                            #WORK TO BE CONTINUED


#-------------------------------------------------------------------------------------------------------------------------------------------------

    print("*************************************************************************************************")
    print(" \t \t \tPress 1 for see the information  \n \t \t \tPress 2 to reset the Admission \n \t \t \tPress 3 for exit  \n \t \t \tPress 4 for Fee list") 
    ex=input(" Choose the given option = ")
    while(ex.isdigit()==True):
        if(ex=="4"):
            Fee()
        if(ex=="2"):
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n\n\n\t\t\t\tADMISSION WERE RESETED (PLEASE CONTINUE)")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            admission()
        elif(ex=="3"):
            exit(options)
        elif(ex=="1"):
            print("*********************************************************************************************************************************")
            print("\t \t \t \t \t \t\t   RESULTS ARE")
            print("\t \t \t \t \t \t\t ----------------")
            print("\t \t \t \t \t \t''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
            print(" \t \t \t \t \t \t' Student name                                 :  ",sn,ssn)
            print(" \t \t \t \t \t \t'",sn,ssn,"Father name                         :  ",fn)
            print(" \t \t \t \t \t \t'",sn,ssn,"Mother name                         :  ",mn)
            print(" \t \t \t \t \t \t'",sn,ssn,"Admission Number                    :  ",ad)
            print(" \t \t \t \t \t \t'",sn,ssn,"class                               :  ",cs)
            if(st=="Maths" or st=="Bio" or st=="Commerse"):
                print(" \t \t \t \t \t \t'",sn,ssn,"Stream                              :  ",st)
            else:
                pass
            print(" \t \t \t \t \t \t'",sn,ssn,"Father occupission                  :  ",fo)
            print(" \t \t \t \t \t \t'",sn,ssn,"Mother occupission                  :  ",mo)
            print(" \t \t \t \t \t \t'",sn,ssn,"Previous school name                :  ",ps)
            print(" \t \t \t \t \t \t'",sn,ssn,"Address                             :  ",sa)
            print(" \t \t \t \t \t \t' Enter the mobile number of",sn,ssn,"         :  ",mn)
            if(sg=="MALE" or sg=="M" or sg=="male" or sg=="m"):
                print(" \t \t \t \t \t \t'",sn,ssn," Gender                             :   Male")
            elif(sg=="FEMALE" or sg=="F" or sg=="female" or sg=="f"):
                print(" \t \t \t \t \t \t'",sn,ssn,"Gender                             :   Female")
            if(ao=="y" or ao=="Y"):
                print(" \t \t \t \t \t \t'",sn,ssn,"Addhar number                       :  ",an)
            else:
                pass
            if(esb=="Y" or esb=="y"):
                print( "\t \t \t \t \t \t'",sn,ssn,"brother name                        :  ",esb,ssn)
            else:
                pass
            if(ess=="Y" or ess=="y"):
                print( "\t \t \t \t \t \t'",sn,ssn,"sister name                         :  ",ess,ssn)
            else:
                pass
            print("\t \t \t \t \t \t' Name of (OTHER) local parent of",sn,ssn,"    :",   lg,llg)
            print("\t \t \t \t \t \t'",sn,ssn,"Code number of your area (G.K.P)    :   273 -",en)
            print("\t \t \t \t \t \t''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        else:
            print("\t \t \tWrong syntex")
            print(".................................................................................................")
            ex=int(input(" Choose the given option = "))
            print("=====================================================================================================")
        print("\t \t \t\t..............................")
        print("\t \t \t\tPress 1 for exit             .")
        print("\t \t \t\tPress 2 for reset admission  `")
        print("\t \t \t\tPress 1 for Fee list         .")
        print("\t \t \t\t``````````````````````````````")
        ax=input("Enter the options given upward = ")
        if(ax.isdigit()==True):
            if(ax=="1"):
                exit(home1)
            elif(ax=="2"):
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n\n\n\t\t\t\tADMISSION WERE RESETED (PLEASE CONTINUE)")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                admission()
            elif(ax=="3"):
                Fee()
            else:
                print("You given the wrong input")
                ax=input("Enter the options given upward = ")
        if(ax.isdigit()!=True):
            ax=input("Enter the options given upward = ")
#........................................................................................................................          
    while(ex.isdigit()!=True):
        print("**********************************  ERROR  ***************************************************************")
        print(" \t \t \tPress 1 for see the information  \n \t \t \tPress 2 to reset the Admission \n \t \t \tPress 3 for exit  \n \t \t \tPress 4 for Fee list") 
        ex=input(" Choose the given option = ")
        pass
        if(ex=="4"):
            Fee()
        if(ex=="2"):
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n\n\n\t\t\t\tADMISSION WERE RESETED (PLEASE CONTINUE)")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            admission()
        elif(ex=="3"):
            exit(options)
        elif(ex=="1"):
            print("*********************************************************************************************************************************")
            print("\t \t \t \t \t \t\t   RESULTS ARE")
            print("\t \t \t \t \t \t\t ----------------")
            print("\t \t \t \t \t \t''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
            print(" \t \t \t \t \t \t' Student name                                 :  ",sn,ssn)
            print(" \t \t \t \t \t \t'",sn,ssn,"Father name                         :  ",fn)
            print(" \t \t \t \t \t \t'",sn,ssn,"Mother name                         :  ",mn)
            print(" \t \t \t \t \t \t'",sn,ssn,"Admission Number                    :  ",ad)
            print(" \t \t \t \t \t \t'",sn,ssn,"class                               :  ",cs)
            if(st=="Maths" or st=="Bio" or st=="Commerse"):
                print(" \t \t \t \t \t \t'",sn,ssn,"Stream                              :  ",st)
            else:
                pass
            print(" \t \t \t \t \t \t'",sn,ssn,"St                               :  ",cs)
            print(" \t \t \t \t \t \t'",sn,ssn,"Father occupission                  :  ",fo)
            print(" \t \t \t \t \t \t'",sn,ssn,"Mother occupission                  :  ",mo)
            print(" \t \t \t \t \t \t'",sn,ssn,"Previous school name                :  ",ps)
            print(" \t \t \t \t \t \t'",sn,ssn,"Address                             :  ",sa)
            print(" \t \t \t \t \t \t' Enter the mobile number of",sn,ssn,"         :  ",mn)
            if(sg=="MALE" or sg=="M" or sg=="male" or sg=="m"):
                print(" \t \t \t \t \t \t'",sn,ssn," Gender                             :   Male")
            elif(sg=="FEMALE" or sg=="F" or sg=="female" or sg=="f"):
                print(" \t \t \t \t \t \t'",sn,ssn,"Gender                             :   Female")
            if(ao=="y" or ao=="Y"):
                print(" \t \t \t \t \t \t'",sn,ssn,"Addhar number                       :  ",an)
            else:
                pass
            if(esb=="Y" or esb=="y"):
                print( "\t \t \t \t \t \t'",sn,ssn,"brother name                        :  ",cn,ssn)
                print( "\t \t \t \t \t \t'",sn,ssn,"brother Class name                  :  ",bc)
            else:
                pass
            if(ess=="Y" or ess=="y"):
                print( "\t \t \t \t \t \t'",sn,ssn,"sister name                         :  ",sn,ssn)
                print( "\t \t \t \t \t \t'",sn,ssn,"brother Class name                  :  ",sc)
            else:
                pass
            print("\t \t \t \t \t \t' Name of (OTHER) local parent of",sn,ssn,"    :",   lg,llg)
            print("\t \t \t \t \t \t'",sn,ssn,"Code number of your area (G.K.P)    :   273 -",en)
            print("\t \t \t \t \t \t''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        else:
            print("\t \t \tWrong syntex")
            print(".................................................................................................")
            ex=int(input(" Choose the given option = "))
            print("=====================================================================================================")
        print("\t \t \t\t..............................")
        print("\t \t \t\tPress 1 for exit             .")
        print("\t \t \t\tPress 2 for reset admission  `")
        print("\t \t \t\tPress 3 for Fee list         .")
        print("\t \t \t\t``````````````````````````````")
        ax=input("Enter the options given upward = ")
        if(ax.isdigit()==True):
            if(ax=="1"):
                exit(home1)
            elif(ax=="2"):
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n\n\n\t\t\t\tADMISSION WERE RESETED (PLEASE CONTINUE)")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                admission()
            elif(ax=="3"):
                Fee()
            else:
                print("You given the wrong input")
                ax=input("Enter the options given upward = ")
        if(ax.isdigit()!=True):
            ax=input("Enter the options given upward = ")


#.......................................................................................................................



    
#........................................................................................................................
def Feelist():
    print("Press 1 for Pre Nursery \nPress 2 for L.K.G & U.K.G \nPress 3 for class 1-5 \nPress 4 for 6-8 \nPress 5 for 9-10 \nPress 6 for 11-12 \nPress 7 for go to options \nPress 8 for change the work place \nPress 9 for exit")
    ch=input("Enter the number of given options = ")
    while(ch.isdigit()==True):
        print("**********************************************************************")
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#For class p=Nursery)))
        if(ch=="1"):
            print("\t \t \tPress N for new student \t \t \tPress O for old student")
            so=input("Choose the option given upward = ")
            while(so.isalpha()==True):
                if(so=="N" or so=="n"):         # NEW STUDENTS
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 3,150")
                    print("Terminal Fee \t \t \t        :\t 1,500")
                    print("Quarterly Fees \t \t \t  \t:\t 4,850")
                    print("Ist installment \t \t  \t:\t 9,400")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 3,700")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 1,500")
                    print("Quarterly Fees \t \t \t  \t:\t 3,700")
                    print("IIIrd installment \t \t  \t:\t 5,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t \t  \t:\t 3,700")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Options..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        return
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                if(so=="O" or so=="o"):               # OLD STUDENTS
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 4,850")
                    print("Terminal Fee \t \t \t  : \t 1,500")
                    print("Ist installment \t\t  :\t 6,350")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 3,700")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 3,700")
                    print("Terminal Fee \t \t \t  : \t 1,500")
                    print("IIIrd installment \t\t  :\t 5,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 3,700")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        return
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    Feelist()
            while(so.isalpha()!=True):
                                             #New student's
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the digit's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                so=input("Choose the option given upward = ")
                pass
                if(so=="N" or so=="n"):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 3,150")
                    print("Terminal Fee \t \t \t        :\t 1,500")
                    print("Quarterly Fees \t \t \t  \t:\t 4,850")
                    print("Ist installment \t \t  \t:\t 9,400")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 3,700")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 1,500")
                    print("Quarterly Fees \t \t \t  \t:\t 3,700")
                    print("IIIrd installment \t \t  \t:\t 5,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t \t  \t:\t 3,700")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose the Options..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                if(so=="O" or so=="o"):
                                          #Old student's
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 4,850")
                    print("Terminal Fee \t \t \t  : \t 1,500")
                    print("Ist installment \t\t  :\t 6,350")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 3,700")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 3,700")
                    print("Terminal Fee \t \t \t  : \t 1,500")
                    print("IIIrd installment \t\t  :\t 5,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 3,700")
                    print("######################################################################################################")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Convence..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        so=input("Choose the option given upward = ")
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    break
                            
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#Class LKG-Ukg))))                               
        if(ch=="2"):
            print("\t \t \tPress N for new student \t \t \tPress O for old student")
            so=input("Choose the option given upward = ")
            while(so.isalpha()==True):
                if(so=="N" or so=="n"):                      #NEW STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 4,150")
                    print("Terminal Fee \t \t \t        :\t 1,600")
                    print("Quarterly Fees \t \t \t  \t:\t 5,250")
                    print("Ist installment \t \t  \t:\t 11,000")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 4,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 1,600")
                    print("Quarterly Fees \t \t \t  \t:\t 4,200")
                    print("IIIrd installment \t \t  \t:\t 5,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t \t  \t:\t 2,200")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                if(so=="O" or so=="o"):                     #OLD STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 2,250")
                    print("Terminal Fee \t \t \t  : \t 1,600")
                    print("Ist installment \t\t  :\t 6,850")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 4,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 4,200")
                    print("Terminal Fee \t \t \t  : \t 1,600")
                    print("IIIrd installment \t\t  :\t 5,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 4,200")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        Feelist()
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    break
            while(so.isalpha()!=True):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the digit's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                so=input("Choose the option given upward = ")
                pass
                if(so=="N" or so=="n"):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 4,150")
                    print("Terminal Fee \t \t \t        :\t 1,600")
                    print("Quarterly Fees \t \t \t  \t:\t 5,250")
                    print("Ist installment \t \t  \t:\t 11,000")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 4,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 1,600")
                    print("Quarterly Fees \t \t \t  \t:\t 4,200")
                    print("IIIrd installment \t \t  \t:\t 5,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t \t  \t:\t 2,200")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                if(so=="O" or so=="o"):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 2,250")
                    print("Terminal Fee \t \t \t  : \t 1,600")
                    print("Ist installment \t\t  :\t 6,850")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 4,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 4,200")
                    print("Terminal Fee \t \t \t  : \t 1,600")
                    print("IIIrd installment \t\t  :\t 5,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 4,200")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    Feelist()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#CLASS 1-5                                          
        if(ch=="3"):
            print("\t \t \tPress N for new student \t \t \tPress O for old student")
            so=input("Choose the option given upward = ")
            while(so.isalpha()==True):
                if(so=="N" or so=="n"):                     #NEW STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 4,200")
                    print("Terminal Fee \t \t \t        :\t 1,900")
                    print("Quarterly Fees \t \t \t  \t:\t 5,900")
                    print("Ist installment \t \t  \t:\t 12,000")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 4,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 1,900")
                    print("Quarterly Fees \t \t \t  \t:\t 4,900")
                    print("IIIrd installment \t \t  \t:\t 6,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t \t  \t:\t 4,900")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                if(so=="O" or so=="o"):        #OLD STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 4,850")
                    print("Terminal Fee \t \t \t  : \t 1,900")
                    print("Ist installment \t\t  :\t 7,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 4,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 4,900")
                    print("Terminal Fee \t \t \t  : \t 1,900")
                    print("IIIrd installment \t\t  :\t 6,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 4,900")
                    print("====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        Feelist()
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    break
            while(so.isalpha()!=True):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the digit's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                so=input("Choose the option given upward = ")
                pass
                if(so=="N" or so=="n"):                     #New Student's
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 4,200")
                    print("Terminal Fee \t \t \t        :\t 1,900")
                    print("Quarterly Fees \t \t \t  \t:\t 5,900")
                    print("Ist installment \t \t  \t:\t 12,000")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 4,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 1,900")
                    print("Quarterly Fees \t \t \t  \t:\t 4,900")
                    print("IIIrd installment \t \t  \t:\t 6,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t \t  \t:\t 4,900")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                if(so=="O" or so=="o"):        #Old Student's
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 4,850")
                    print("Terminal Fee \t \t \t  : \t 1,900")
                    print("Ist installment \t\t  :\t 7,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 4,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 4,900")
                    print("Terminal Fee \t \t \t  : \t 1,900")
                    print("IIIrd installment \t\t  :\t 6,800")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 4,900")
                    print("====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        Feelist()
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    break
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#CLASS 6-8
        if(ch=="4"):             
            print("\t \t \tPress N for new student \t \t \tPress O for old student")
            so=input("Choose the option given upward = ")
            while(so.isalpha()==True):
                if(so=="N" or so=="n"):         #NEW STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 4,700")
                    print("Terminal Fee \t \t \t        :\t 2,000")
                    print("Quarterly Fees \t \t \t  \t:\t 6,300")
                    print("Ist installment \t \t  \t:\t 13,000")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 5,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 2,000")
                    print("Quarterly Fees \t \t \t  \t:\t 5,300")
                    print("IIIrd installment \t \t  \t:\t 7,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 4,900")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                if(so=="O" or so=="o"):             #OLD STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 6,300")
                    print("Terminal Fee \t \t \t  : \t 2,000")
                    print("Ist installment \t\t  :\t 8,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 5,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 5,300")
                    print("Terminal Fee \t \t \t  : \t 2,000")
                    print("IIIrd installment \t\t  :\t 7,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 5,300")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        Feelist()
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    break
            while(so.isalpha()!=True):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the digit's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                so=input("Choose the option given upward = ")
                pass
                if(so=="N" or so=="n"):           #New Student's
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 4,700")
                    print("Terminal Fee \t \t \t        :\t 2,000")
                    print("Quarterly Fees \t \t \t  \t:\t 6,300")
                    print("Ist installment \t \t  \t:\t 13,000")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 5,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 2,000")
                    print("Quarterly Fees \t \t \t  \t:\t 5,300")
                    print("IIIrd installment \t \t  \t:\t 7,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 4,900")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                if(so=="O" or so=="o"):                 #Old student's
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 6,300")
                    print("Terminal Fee \t \t \t  : \t 2,000")
                    print("Ist installment \t\t  :\t 8,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 5,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 5,300")
                    print("Terminal Fee \t \t \t  : \t 2,000")
                    print("IIIrd installment \t\t  :\t 7,300")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 5,300")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        Feelist()
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    break
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#CLASS 9-10
        if(ch=="5"):
            print("\t \t \tPress N for new student \t \t \tPress O for old student")
            so=input("Choose the option given upward = ")
            while(so.isalpha()==True):
                if(so=="N" or so=="n"):            #NEW STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 5,100")
                    print("Terminal Fee \t \t \t        :\t 2,700")
                    print("Quarterly Fees \t \t \t  \t:\t 7,200")
                    print("Ist installment \t \t  \t:\t 15,000")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 6,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 2,700")
                    print("Quarterly Fees \t \t \t  \t:\t 6,200")
                    print("IIIrd installment \t \t  \t:\t 8,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t \t  \t:\t 6,200")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                    
                if(so=="O" or so=="o"):            #OLD STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 7,200")
                    print("Terminal Fee \t \t \t  : \t 2,700")
                    print("Ist installment \t\t  :\t 9,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 6,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 6,200")
                    print("Terminal Fee \t \t \t  : \t 2,700")
                    print("IIIrd installment \t\t  :\t 8,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 6,200")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        Feelist()
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    break
            while(so.isalpha()!=True):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the digit's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                so=input("Choose the option given upward = ")
                pass
                if(so=="N" or so=="n"):            #NEW STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Admission Fee of new student is \t: \t 5,100")
                    print("Terminal Fee \t \t \t        :\t 2,700")
                    print("Quarterly Fees \t \t \t  \t:\t 7,200")
                    print("Ist installment \t \t  \t:\t 15,000")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t \t  \t:\t 6,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Terminal Fee \t \t \t        :\t 2,700")
                    print("Quarterly Fees \t \t \t  \t:\t 6,200")
                    print("IIIrd installment \t \t  \t:\t 8,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t \t  \t:\t 6,200")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                            
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        break
                    
                if(so=="O" or so=="o"):            #OLD STUDENT'S
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 7,200")
                    print("Terminal Fee \t \t \t  : \t 2,700")
                    print("Ist installment \t\t  :\t 9,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IInd installment \t\t  :\t 6,200")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Quarterly Fees \t\t \t  :\t 6,200")
                    print("Terminal Fee \t \t \t  : \t 2,700")
                    print("IIIrd installment \t\t  :\t 8,900")
                    print("=====================================================================================================")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("IVth installment \t\t  :\t 6,200")
                    print("=====================================================================================================")
                    print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                    print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                    ex=input(" Choose the given option = ")
                    if(ex.isdigit()==True):
                        if(ex=="1"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Fee List..............................................")
                            print("\n\n\n")
                            Feelist()
                        elif(ex=="2"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Choose The Option..............................................")
                            print("\n\n\n")
                            home1()
                        elif(ex=="3"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Conveyance..............................................")
                            print("\n\n\n")
                            conveyance()
                        elif(ex=="4"):
                            print("_____________________________________________________________________________________________________________________________________")
                            print("\n\n")
                            print(".........................................Welcome To Admission..............................................")
                            print("\n\n\n")
                            admission()
                        elif(ex=="5"):
                            print("\t\t\t\t\t\tBye.. Bye...")
                            exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            Feelist()
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        Feelist()
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    break
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#CALSS 11
        if(ch=="6"):
            print("Choose your stream \nPress 1 for Science \nPress 2 for Commerce")
            eo=input("Enter the number by given option upward = ")
            if(eo.isdigit()==True):
                if(eo=="1"):
                    print("\t \t \tPress N for new student \t \t \tPress O for old student")
                    so=input("Choose the option given upward = ")
                    while(so.isalpha()==True):
                        if(so=="N" or so=="n"):          #NEW STUDENT'S
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Admission Fee of new student is \t: \t 6,300")
                            print("Terminal Fee \t \t \t        :\t 3,200")
                            print("Quarterly Fees \t \t \t  \t:\t 11,500")
                            print("Ist installment \t \t  \t:\t 21,000")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IInd installment \t \t  \t:\t 10,500")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Terminal Fee \t \t \t        :\t 3,200")
                            print("Quarterly Fees \t \t \t  \t:\t 10,500")
                            print("IIIrd installment \t \t  \t:\t 13,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IVth installment \t \t  \t:\t 10,500")
                            print("=====================================================================================================")
                            print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                            print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                            ex=input(" Choose the given option = ")
                            if(ex.isdigit()==True):
                                if(ex=="1"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Fee List..............................................")
                                    print("\n\n\n")
                                    Feelist()
                                elif(ex=="2"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Choose The Option..............................................")
                                    print("\n\n\n")
                                    home1()
                                elif(ex=="3"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Conveyance..............................................")
                                    print("\n\n\n")
                                    conveyance()
                                elif(ex=="4"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Admission..............................................")
                                    print("\n\n\n")
                                    admission()
                                elif(ex=="5"):
                                    print("\t\t\t\t\t\tBye.. Bye...")
                                    exit(home1)
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    Feelist()
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                                Feelist()
                                
                        if(so=="O" or so=="o"):       #OLD STUDENT'S
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Quarterly Fees \t\t \t  :\t 11,500")
                            print("Terminal Fee \t \t \t  : \t 3,200")
                            print("Ist installment \t\t  :\t 14,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IInd installment \t\t  :\t 10,500")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Quarterly Fees \t\t \t  :\t 10,500")
                            print("Terminal Fee \t \t \t  : \t 3,200")
                            print("IIIrd installment \t\t  :\t 13,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IVth installment \t\t  :\t 10,500")
                            print("=====================================================================================================")
                            print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                            print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                            ex=input(" Choose the given option = ")
                            if(ex.isdigit()==True):
                                if(ex=="1"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Fee List..............................................")
                                    print("\n\n\n")
                                    Feelist()
                                elif(ex=="2"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Choose The Option..............................................")
                                    print("\n\n\n")
                                    home1()
                                elif(ex=="3"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Conveyance..............................................")
                                    print("\n\n\n")
                                    conveyance()
                                elif(ex=="4"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Admission..............................................")
                                    print("\n\n\n")
                                    admission()
                                elif(ex=="5"):
                                    print("\t\t\t\t\t\tBye.. Bye...")
                                    exit(home1)
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    Feelist()
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                                Feelist()
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                            break
                    while(so.isalpha()!=True):
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the digit's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        so=input("Choose the option given upward = ")
                        pass
                        if(so=="N" or so=="n"):          #New Student's
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Admission Fee of new student is \t: \t 6,300")
                            print("Terminal Fee \t \t \t        :\t 3,200")
                            print("Quarterly Fees \t \t \t  \t:\t 11,500")
                            print("Ist installment \t \t  \t:\t 21,000")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IInd installment \t \t  \t:\t 10,500")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Terminal Fee \t \t \t        :\t 3,200")
                            print("Quarterly Fees \t \t \t  \t:\t 10,500")
                            print("IIIrd installment \t \t  \t:\t 13,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IVth installment \t \t  \t:\t 10,500")
                            print("=====================================================================================================")
                            print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                            print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                            ex=input(" Choose the given option = ")
                            if(ex.isdigit()==True):
                                if(ex=="1"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Fee List..............................................")
                                    print("\n\n\n")
                                    Feelist()
                                elif(ex=="2"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Choose The Option..............................................")
                                    print("\n\n\n")
                                    home1()
                                elif(ex=="3"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Conveyance..............................................")
                                    print("\n\n\n")
                                    conveyance()
                                elif(ex=="4"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Admission..............................................")
                                    print("\n\n\n")
                                    admission()
                                elif(ex=="5"):
                                    print("\t\t\t\t\t\tBye.. Bye...")
                                    exit(home1)
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    Feelist()
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                                Feelist()
                        
                        if(so=="O" or so=="o"):       #Old Student's
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Quarterly Fees \t\t \t  :\t 11,500")
                            print("Terminal Fee \t \t \t  : \t 3,200")
                            print("Ist installment \t\t  :\t 14,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IInd installment \t\t  :\t 10,500")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Quarterly Fees \t\t \t  :\t 10,500")
                            print("Terminal Fee \t \t \t  : \t 3,200")
                            print("IIIrd installment \t\t  :\t 13,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IVth installment \t\t  :\t 10,500")
                            print("=====================================================================================================")
                            print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                            print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                            ex=input(" Choose the given option = ")
                            if(ex.isdigit()==True):
                                if(ex=="1"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Fee List..............................................")
                                    print("\n\n\n")
                                    Feelist()
                                elif(ex=="2"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Choose The Option..............................................")
                                    print("\n\n\n")
                                    home1()
                                elif(ex=="3"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Conveyance..............................................")
                                    print("\n\n\n")
                                    conveyance()
                                elif(ex=="4"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Admission..............................................")
                                    print("\n\n\n")
                                    admission()
                                elif(ex=="5"):
                                    print("\t\t\t\t\t\tBye.. Bye...")
                                    exit(home1)
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    Feelist()
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                                Feelist()
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                            break
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                if(eo=="2"):
                    print("\t \t \tPress N for new student \t \t \tPress O for old student")
                    so=input("Choose the option given upward = ")
                    if(so.isalpha()==True):
                        if(so=="N" or so=="n"):         #NEW STUENT'S
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Admission Fee of new student is \t: \t 6,300")
                            print("Terminal Fee \t \t \t        :\t 3,200")
                            print("Quarterly Fees \t \t \t  \t:\t 10,800")
                            print("Ist installment \t \t  \t:\t 20,200")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IInd installment \t \t  \t:\t 9,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Terminal Fee \t \t \t        :\t 3,200")
                            print("Quarterly Fees \t \t \t  \t:\t 9,700")
                            print("IIIrd installment \t \t  \t:\t 12,900")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IVth installment \t \t  \t:\t 9,700")
                            print("=====================================================================================================")
                            print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                            print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                            ex=input(" Choose the given option = ")
                            if(ex.isdigit()==True):
                                if(ex=="1"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Fee List..............................................")
                                    print("\n\n\n")
                                    Feelist()
                                elif(ex=="2"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Choose The Option..............................................")
                                    print("\n\n\n")
                                    home1()
                                elif(ex=="3"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Conveyance..............................................")
                                    print("\n\n\n")
                                    conveyance()
                                elif(ex=="4"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Admission..............................................")
                                    print("\n\n\n")
                                    admission()
                                elif(ex=="5"):
                                    print("\t\t\t\t\t\tBye.. Bye...")
                                    exit(home1)
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    Feelist()
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                                break
                        if(so=="O" or so=="o"):        #OLD STUDENT'S
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Quarterly Fees \t\t \t  :\t 11,500")
                            print("Terminal Fee \t \t \t  : \t 3,200")
                            print("Ist installment \t\t  :\t 14,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IInd installment \t\t  :\t 10,500")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Quarterly Fees \t\t \t  :\t 10,500")
                            print("Terminal Fee \t \t \t  : \t 3,200")
                            print("IIIrd installment \t\t  :\t 13,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IVth installment \t\t  :\t 10,500")
                            print("=====================================================================================================")
                            print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                            print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                            ex=input(" Choose the given option = ")
                            if(ex.isdigit()==True):
                                if(ex=="1"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Fee List..............................................")
                                    print("\n\n\n")
                                    Feelist()
                                elif(ex=="2"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Choose The Option..............................................")
                                    print("\n\n\n")
                                    home1()
                                elif(ex=="3"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Conveyance..............................................")
                                    print("\n\n\n")
                                    conveyance()
                                elif(ex=="4"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Admission..............................................")
                                    print("\n\n\n")
                                    admission()
                                elif(ex=="5"):
                                    print("\t\t\t\t\t\tBye.. Bye...")
                                    exit(home1)
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    Feelist()
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                                Feelist()
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                            break
                    while(so.isalpha()!=True):
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the digit's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                        so=input("Choose the option given upward = ")
                        pass
                        if(so=="N" or so=="n"):         #NEW STUENT'S
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Admission Fee of new student is \t: \t 6,300")
                            print("Terminal Fee \t \t \t        :\t 3,200")
                            print("Quarterly Fees \t \t \t  \t:\t 10,800")
                            print("Ist installment \t \t  \t:\t 20,200")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IInd installment \t \t  \t:\t 9,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Terminal Fee \t \t \t        :\t 3,200")
                            print("Quarterly Fees \t \t \t  \t:\t 9,700")
                            print("IIIrd installment \t \t  \t:\t 12,900")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IVth installment \t \t  \t:\t 9,700")
                            print("=====================================================================================================")
                            print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                            print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                            ex=input(" Choose the given option = ")
                            if(ex.isdigit()==True):
                                if(ex=="1"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Fee List..............................................")
                                    print("\n\n\n")
                                    Feelist()
                                elif(ex=="2"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Choose The Option..............................................")
                                    print("\n\n\n")
                                    home1()
                                elif(ex=="3"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Conveyance..............................................")
                                    print("\n\n\n")
                                    conveyance()
                                elif(ex=="4"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Admission..............................................")
                                    print("\n\n\n")
                                    admission()
                                elif(ex=="5"):
                                    print("\t\t\t\t\t\tBye.. Bye...")
                                    exit(home1)
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    Feelist()
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                                break
                        if(so=="O" or so=="o"):        #OLD STUDENT'S
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ist installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Quarterly Fees \t\t \t  :\t 11,500")
                            print("Terminal Fee \t \t \t  : \t 3,200")
                            print("Ist installment \t\t  :\t 14,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IInd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IInd installment \t\t  :\t 10,500")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IIIrd installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Quarterly Fees \t\t \t  :\t 10,500")
                            print("Terminal Fee \t \t \t  : \t 3,200")
                            print("IIIrd installment \t\t  :\t 13,700")
                            print("=====================================================================================================")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IVth installment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("IVth installment \t\t  :\t 10,500")
                            print("=====================================================================================================")
                            print(" \t \t \tPress 1 for continue in fee list  \n \t \t \tPress 2 to go mainmenu \n \t \t \tPress 3 for conveyance")
                            print(" \t \t \tPress 4 to go in admission \n \t \t \tPress 5 for exit ")  
                            ex=input(" Choose the given option = ")
                            if(ex.isdigit()==True):
                                if(ex=="1"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Fee List..............................................")
                                    print("\n\n\n")
                                    Feelist()
                                elif(ex=="2"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Choose The Option..............................................")
                                    print("\n\n\n")
                                    home1()
                                elif(ex=="3"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Conveyance..............................................")
                                    print("\n\n\n")
                                    conveyance()
                                elif(ex=="4"):
                                    print("_____________________________________________________________________________________________________________________________________")
                                    print("\n\n")
                                    print(".........................................Welcome To Admission..............................................")
                                    print("\n\n\n")
                                    admission()
                                elif(ex=="5"):
                                    print("\t\t\t\t\t\tBye.. Bye...")
                                    exit(home1)
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!   You given any other option (except 1,2,3) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    Feelist()
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                                Feelist()
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!You given the invalid alphabet's except N/O which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                            break
        if(ch=="7"):
            print("Welcome")
            home1()
        if(ch=="8"):
            options()
        if(ch=="9"):
            print("\t\t\t\t\t\tBye... Bye...")
            exit(home1)
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
            Feelist()
    while(ch.isdigit()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
        Feelist()
        
            


#.......................................................................................................................



    
#........................................................................................................................
def conveyance():
    print("\t AMOUNT\t\t\t-\t\tCHECKPOINTS")
    print("\t 800 Rupee\t\t-\t1.Rajendar Nagar")
    print("\t 800 Rupee\t\t-\t2.Gorakhnath Temple Main Gate")
    print("\t 800 Rupee\t\t-\t3.Rasoolpur")
    print("\t 800 Rupee\t\t-\t4.Green City Colony")
    print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("\t 900 Rupee\t\t-\t1.Shastri Nagar")
    print("\t 900 Rupee\t\t-\t2.Humayunpur Jageshar Pasi Chauraha")
    print("\t 900 Rupee\t\t-\t3.Jhulelal Mandir")
    print("\t 900 Rupee\t\t-\t4.Ramlila Maidan")
    print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("\t1000 Rupee\t\t-\t1.Bargadwan Junction")
    print("\t1000 Rupee\t\t-\t2.J P  Hospital & Tarnag Crossing")
    print("\t1000 Rupee\t\t-\t3.Subhash Chandra Bose Nagar")
    print("\t1000 Rupee\t\t-\t4.Harawaha Phatak")
    print("\t1000 Rupee\t\t-\t5.Naya Gaon & Bankatwan")
    print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("\t1100 Rupee\t\t-\t1.Mohripur")
    print("\t1100 Rupee\t\t-\t2.Dharamshala")
    print("\t1100 Rupee\t\t-\t3.Bauliya Colony")
    print("\t1100 Rupee\t\t-\t4.Jafar Bazar")
    print("\t1100 Rupee\t\t-\t5.Buxshipur/Vikas Nagar-Vistar")
    print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("\t1200 Rupee\t\t-\t1.Mahuatar Junction/ Balapar")
    print("\t1200 Rupee\t\t-\t2.Mahuatar Ghasikatra/ Nizampur")
    print("\t1200 Rupee\t\t-\t3.Geeta Garden/ Shivpur Shahbazganj")
    print("\t1200 Rupee\t\t-\t4.Padri Bazar")
    print("\t1200 Rupee\t\t-\t5.Bichiya Colony")
    print("\t1200 Rupee\t\t-\t6.Kaali Mandir/Golghar")
    print("\t1200 Rupee\t\t-\t7.Ghosh Company")
    print("\t1200 Rupee\t\t-\t8.Raptinagar")
    print("\t1200 Rupee\t\t-\t9.Mohaddipur")
    print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("\t1300 Rupee\t\t-\t1.Ghantaghar")
    print("\t1300 Rupee\t\t-\t2.Peepeganj")
    print("\t1300 Rupee\t\t-\t3.Padleganj")
    print("\t1300 Rupee\t\t-\t4.Medical College")
    print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("\t1400 Rupee\t\t-\t1.Taramandal")
    print("\t1400 Rupee\t\t-\t2.Sahara State")
    print("\t1400 Rupee\t\t-\t3.Jankhandi")
    print("\t1400 Rupee\t\t-\t1.Nandanagar")
    print("\t1400 Rupee\t\t-\t1.Sainik Bihar")
    print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("\n\n\n")
    print("\t \t \t\t.................................")
    print("\t \t \t\t. Press 1 for Admission         .")
    print("\t \t \t\t. Press 2 for Fee list          .")
    print("\t \t \t\t. Press 3 for Options           .")
    print("\t \t \t\t. Press 4 for change work place .")
    print("\t \t \t\t. Press 5 for exit              .")
    print("\t \t \t\t.................................")
    s=input("Choose the Option's Given Upward = ")
    while(s.isdigit()==True):
        if(s=="1"):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Admission then press 1 ")
            print("\t\t\t\t\tIf you want to change then press 2")
            print("\t\t\t\t\tIf you want to exit then press 3")
            sd=input("Enter any one option's which given upward = ")
            if(sd.isdigit()==True):
                if(sd=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    admission()
                elif(sd=="2"):
                    print("\t\t\t\t\tchoose Where You Want To Go")
                    break
                elif(sd=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBye... Bye...")
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other digit which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                pass
        elif(s=="2"):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Feelist then press 1 ")
            print("\t\t\t\t\tIf you want to change then press 2")
            print("\t\t\t\t\tIf you want to exit then press 3")
            sd=input("Enter any one option's which given upward = ")
            if(sd.isdigit()==True):
                if(sd=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    Feelist()
                elif(sd=="2"):
                    print("\t\t\t\t\tchoose Where You Want To Go")
                    break
                elif(sd=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBye... Bye...")
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other digit which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                pass
        elif(s=="3"):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Option's then press 1 ")
            print("\t\t\t\t\tIf you want to change then press 2")
            print("\t\t\t\t\tIf you want to exit then press 3")
            sd=input("Enter any one option's which given upward = ")
            if(sd.isdigit()==True):
                if(sd=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    home1()
                elif(sd=="2"):
                    print("\t\t\t\t\tchoose Where You Want To Go")
                    break
                elif(sd=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBye... Bye...")
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other digit which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                pass
        elif(s=="4"):
            print("\n\n\t\t\t\t\tIf you are conferm to change Work place then press 1 ")
            print("\t\t\t\t\tIf you want to change then press 2")
            print("\t\t\t\t\tIf you want to exit then press 3")
            sd=input("Enter any one option's which given upward = ")
            if(sd.isdigit()==True):
                if(sd=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    options()
                elif(sd=="2"):
                    print("\t\t\t\t\tchoose Where You Want To Go")
                    break
                elif(sd=="3"):
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other digit which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                pass
        elif(s=="5"):
            print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
            print("\n\n\n\t\t\t\t\t\t\tBye... Bye...")
            exit(home1)
    while(s.isdigit()!=True):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
        s=input("Choose the Option's Given Upward = ")
        pass
        if(s=="1"):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Admission then press 1 ")
            print("\t\t\t\t\tIf you want to change then press 2")
            print("\t\t\t\t\tIf you want to exit then press 3")
            sd=input("Enter any one option's which given upward = ")
            if(sd.isdigit()==True):
                if(sd=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    admission()
                elif(sd=="2"):
                    print("\t\t\t\t\tchoose Where You Want To Go")
                    break
                elif(sd=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBye... Bye...")
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other digit which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                pass
        elif(s=="2"):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Feelist then press 1 ")
            print("\t\t\t\t\tIf you want to change then press 2")
            print("\t\t\t\t\tIf you want to exit then press 3")
            sd=input("Enter any one option's which given upward = ")
            if(sd.isdigit()==True):
                if(sd=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    Feelist()
                elif(sd=="2"):
                    print("\t\t\t\t\tchoose Where You Want To Go")
                    break
                elif(sd=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBye... Bye...")
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other digit which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                pass
        elif(s=="3"):
            print("\n\n\t\t\t\t\tIf you are conferm to go in Option's then press 1 ")
            print("\t\t\t\t\tIf you want to change then press 2")
            print("\t\t\t\t\tIf you want to exit then press 3")
            sd=input("Enter any one option's which given upward = ")
            if(sd.isdigit()==True):
                if(sd=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    home1()
                elif(sd=="2"):
                    print("\t\t\t\t\tchoose Where You Want To Go")
                    break
                elif(sd=="3"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tBye... Bye...")
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other digit which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                pass
        elif(s=="4"):
            print("\n\n\t\t\t\t\tIf you are conferm to change Work place then press 1 ")
            print("\t\t\t\t\tIf you want to change then press 2")
            print("\t\t\t\t\tIf you want to exit then press 3")
            sd=input("Enter any one option's which given upward = ")
            if(sd.isdigit()==True):
                if(sd=="1"):
                    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                    print("\n\n\n\t\t\t\t\t\t\tWELCOME TO ADMISSION LIST")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    options()
                elif(sd=="2"):
                    print("\t\t\t\t\tchoose Where You Want To Go")
                    break
                elif(sd=="3"):
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other digit which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                    pass
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given the alphabet's or sing which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("---------------------------------------------PLEASE TRY AGAIN-----------------------------------------------------------------------")
                pass
        elif(s=="5"):
            print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
            print("\n\n\n\t\t\t\t\t\t\tBye... Bye...")
            exit(home1)

#=======================================================================================================================================================================

def submitfee(): 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    na=input("Enter the full name of student = ")
    sa=" "
    while(na.isalpha()==True and sa in na):
        break
    while(na.isalpha()!=True and sa not in na):
        na=input("Enter the full name of student = ")
    cs=input("Enter the Student class = ")
    while(cs.isalnum()==True):
        if(cs=="playway".upper() or cs=="lkg".upper() or cs=="nursery".upper() or cs=="ukg".upper() or cs=="1" or cs=="2" or cs=="3" or cs=="4" or cs=="5" or cs=="6" or cs=="7" or cs=="8" or cs=="9" or cs=="10" or cs=="11" or cs=="12"):
            break
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid class expect Playway - 12^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            cs=input("Enter the Student class : ")
            continue
    while(cs.isalnum()!=True):
        print("Wrong")
        cs=input("Enter the Student class = ")
    print("=============================================================================================================")
    print("Give input by Y or N")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    I=input("I st installment = ")
    while(I.isalpha()==True):
        if(I=="y" or I=="Y"):
            II=input("II nd installment = ")
            if(II.isalpha()==True):
                if(II=="Y" or II=="y"):
                    III=input("III rd installment = ")
                    if(III.isalpha()==True):
                        if(III=="Y" or III=="y"):
                            IV=input("IV th inatallment = ")
                            if(IV.isalpha()==True):
                                if(IV=="Y" or IV=="y"):
                                    if(cs=="NURSERY" or cs=="PLAYWAY"):
                                        print("I II III IV installment")
                                elif(IV=="N" or IV=="n"):
                                    print("I II III installment")
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid alphabets except Y/N^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the digit or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                        elif(III=="N" or III=="n"):
                            print("I II installment")
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid alphabets except Y/N^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the digit or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                elif(II=="N" or II=="n"):
                    if(cs=="NURSERY" or cs=="PLAYWAY"):
                        print("\n\t\t\tFEE FOR CLASS =",cs,"\n\n")
                        print("=============== I st installment ====================")
                        print("Admission fee = 3150")
                        print("Terminal fee = 1500")
                        print("Quarterly fee = 4850")
                        print("......................................................................................................")
                        ton=3150+1500+4850
                        print("Total fee = ",ton)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the digit or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    print("**************************************************************************************************************************")
                    pass
#     88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                    print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                    print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                    pp=input("Enter the any one digit option which given upward = ")
                    if(pp.isdigit()==True):
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
                    else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                            print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                            pp=input("Enter the any one digit option which given upward = ")
                            pass
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
#     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # L.K.G AND U.K.G 
            elif(cs=="LKG" or cs=="UKG"):
                        print("\n\t\t\tFEE FOR CLASS =",cs,"\n\n")
                        print("=============== I st installment ====================")
                        print("Admission fee = 4150")
                        print("Terminal fee = 1600")
                        print("Quarterly fee = 4850")
                        print("......................................................................................................")
                        tok=4150+1600+4850
                        print("Total fee = ",tok)
                        print("**************************************************************************************************************************")
#     88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                        print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                        pp=input("Enter the any one digit option which given upward = ")
                        if(pp.isdigit()==True):
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                            print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                            pp=input("Enter the any one digit option which given upward = ")
                            pass
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
#     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # 1,2,3,4 & 5
                    elif(cs=="1" or cs=="2" or cs=="3" or cs=="4" or cs=="5"):
                        print("\n\t\t\tFEE FOR CLASS =",cs,"\n\n")
                        print("=============== I st installment ====================")
                        print("Admission fee = 4200")
                        print("Terminal fee = 1900")
                        print("Quarterly fee = 5900")
                        print("......................................................................................................")
                        to1=4200+1900+5900
                        print("Total fee = ",to1)
#     88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                        print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                        pp=input("Enter the any one digit option which given upward = ")
                        if(pp.isdigit()==True):
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                            print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                            pp=input("Enter the any one digit option which given upward = ")
                            pass
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
#     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # 6,7 & 8
                    elif(cs=="6" or cs=="7" or cs=="8"):
                        print("\n\t\t\tFEE FOR CLASS =",cs,"\n\n")
                        print("=============== I st installment ====================")
                        print("Admission fee = 4700")
                        print("Terminal fee = 2000")
                        print("Quarterly fee = 6300")
                        print("......................................................................................................")
                        to6=4700+2000+6300
                        print("Total fee = ",to6)
#     88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                        print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                        pp=input("Enter the any one digit option which given upward = ")
                        if(pp.isdigit()==True):
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                            print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                            pp=input("Enter the any one digit option which given upward = ")
                            pass
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
#     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # 9 & 10
                    elif(cs=="9" or cs=="10"):
                        print("\n\t\t\tFEE FOR CLASS =",cs,"\n\n")
                        print("=============== I st installment ====================")
                        print("Admission fee = 5100")
                        print("Terminal fee = 3200")
                        print("Quarterly fee = 7200")
                        print("......................................................................................................")
                        to9=5100+3200+7200
                        print("Total fee = ",to9)
#     88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                        print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                        pp=input("Enter the any one digit option which given upward = ")
                        if(pp.isdigit()==True):
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
                        else:
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                            print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                            print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                            pp=input("Enter the any one digit option which given upward = ")
                            pass
                            if(pp=="1"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                submitfee()
                            elif(pp=="2"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                home1()
                            elif(pp=="3"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                admission()
                            elif(pp=="4"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                Feelist()
                            elif(pp=="5"):
                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                options()
                            elif(pp=="6"):
                                print("\n\n\t\t\t\t\tBye... Bye...")
                                exit(home1)
                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                pass
                                if(pp=="1"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                    submitfee()
                                if(pp=="2"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                    home1()
                                if(pp=="3"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                    admission()
                                if(pp=="4"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                    Feelist()
                                if(pp=="5"):
                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                    options()
                                if(pp=="6"):
                                    print("\n\n\t\t\t\t\tBye... Bye...")
                                    exit(home1)
#     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    elif(cs=="11" or cs=="12"):
      # 11 & 12
                        print("\t \t \t Press 1 for commerse stream \n \t \t \t Press 2 for science stream")
                        sc=input("Enter the number by given options = ")
                        if(sc.isdigit()==True):
                            if(sc=="1"):
                                print("\n\t\t\tFEE FOR CLASS =",cs,"Commerse\n\n")
                                print("=============== I st installment ====================")
                                print("Admission fee = 6300")
                                print("Terminal fee = 3200")
                                print("Quarterly fee = 10700")
                                print("......................................................................................................")
                                toc=5100+3200+7200
                                print("Total fee = ",toc)
#     88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                if(pp.isdigit()==True):
                                    if(pp=="1"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                        submitfee()
                                    elif(pp=="2"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                        home1()
                                    elif(pp=="3"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                        admission()
                                    elif(pp=="4"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                        Feelist()
                                    elif(pp=="5"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                        options()
                                    elif(pp=="6"):
                                        print("\n\n\t\t\t\t\tBye... Bye...")
                                        exit(home1)
                                    else:
                                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                        print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                        print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                        pp=input("Enter the any one digit option which given upward = ")
                                        pass
                                        if(pp=="1"):
                                           print("\n\n\t\t\t\tYou chossen option ",pp)
                                           print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                           submitfee()
                                        if(pp=="2"):
                                            print("\n\n\t\t\t\tYou chossen option ",pp)
                                            print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                            home1()
                                        if(pp=="3"):
                                            print("\n\n\t\t\t\tYou chossen option ",pp)
                                            print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                            admission()
                                        if(pp=="4"):
                                            print("\n\n\t\t\t\tYou chossen option ",pp)
                                            print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                            Feelist()
                                        if(pp=="5"):
                                            print("\n\n\t\t\t\tYou chossen option ",pp)
                                            print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                            options()
                                        if(pp=="6"):
                                            print("\n\n\t\t\t\t\tBye... Bye...")
                                            exit(home1)
                                        else:
                                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                            print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                            print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                            pp=input("Enter the any one digit option which given upward = ")
                                            pass
                                            if(pp=="1"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                                ubmitfee()
                                            elif(pp=="2"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                                home1()
                                            elif(pp=="3"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                                admission()
                                            elif(pp=="4"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                                Feelist()
                                            elif(pp=="5"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                                options()
                                            elif(pp=="6"):
                                                print("\n\n\t\t\t\t\tBye... Bye...")
                                                exit(home1)
                                            else:
                                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                                pp=input("Enter the any one digit option which given upward = ")
                                                pass
                                                if(pp=="1"):
                                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                                    submitfee()
                                                if(pp=="2"):
                                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                                    home1()
                                                    if(pp=="3"):
                                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                                        print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                                        admission()
                                                    if(pp=="4"):
                                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                                        print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                                        Feelist()
                                                    if(pp=="5"):
                                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                                        options()
                                                    if(pp=="6"):
                                                        print("\n\n\t\t\t\t\tBye... Bye...")
                                                        exit(home1)
#     \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                                         

                            elif(sc=="2"):
                                print("\n\t\t\tFEE FOR CLASS =",cs,"Science\n\n")
                                print("=============== I st installment ====================")
                                print("Admission fee = 6300")
                                print("Terminal fee = 3200")
                                print("Quarterly fee = 11500")
                                print("......................................................................................................")
                                tos=5100+3200+11500
                                print("Total fee = ",tos)
#     88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                pp=input("Enter the any one digit option which given upward = ")
                                if(pp.isdigit()==True):
                                    if(pp=="1"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                        submitfee()
                                    elif(pp=="2"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                        home1()
                                    elif(pp=="3"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                        admission()
                                    elif(pp=="4"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                        Feelist()
                                    elif(pp=="5"):
                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                        options()
                                    elif(pp=="6"):
                                        print("\n\n\t\t\t\t\tBye... Bye...")
                                        exit(home1)
                                    else:
                                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                        print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                        print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                        pp=input("Enter the any one digit option which given upward = ")
                                        pass
                                        if(pp=="1"):
                                           print("\n\n\t\t\t\tYou chossen option ",pp)
                                           print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                           submitfee()
                                        if(pp=="2"):
                                            print("\n\n\t\t\t\tYou chossen option ",pp)
                                            print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                            home1()
                                        if(pp=="3"):
                                            print("\n\n\t\t\t\tYou chossen option ",pp)
                                            print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                            admission()
                                        if(pp=="4"):
                                            print("\n\n\t\t\t\tYou chossen option ",pp)
                                            print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                            Feelist()
                                        if(pp=="5"):
                                            print("\n\n\t\t\t\tYou chossen option ",pp)
                                            print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                            options()
                                        if(pp=="6"):
                                            print("\n\n\t\t\t\t\tBye... Bye...")
                                            exit(home1)
                                        else:
                                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                            print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                            print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                            pp=input("Enter the any one digit option which given upward = ")
                                            pass
                                            if(pp=="1"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                                ubmitfee()
                                            elif(pp=="2"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                                home1()
                                            elif(pp=="3"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                                admission()
                                            elif(pp=="4"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                                Feelist()
                                            elif(pp=="5"):
                                                print("\n\n\t\t\t\tYou chossen option ",pp)
                                                print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                                options()
                                            elif(pp=="6"):
                                                print("\n\n\t\t\t\t\tBye... Bye...")
                                                exit(home1)
                                            else:
                                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                                                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                                                pp=input("Enter the any one digit option which given upward = ")
                                                pass
                                                if(pp=="1"):
                                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                                                    submitfee()
                                                if(pp=="2"):
                                                    print("\n\n\t\t\t\tYou chossen option ",pp)
                                                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                                                    home1()
                                                    if(pp=="3"):
                                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                                        print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                                                        admission()
                                                    if(pp=="4"):
                                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                                        print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                                                        Feelist()
                                                    if(pp=="5"):
                                                        print("\n\n\t\t\t\tYou chossen option ",pp)
                                                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                                                        options()
                                                    if(pp=="6"):
                                                        print("\n\n\t\t\t\t\tBye... Bye...")
                                                        exit(home1)
#     ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                            else:
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!You given any other option (except 1 & 2) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\t \t \t Press 1 for commerse stream \n \t \t \t Press 2 for science stream")
                                sc=input("Enter the number by given options = ")
                                pass
                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!AGAIN...you given any other option (except 1 & 2) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                print("\n\t \t \t Press 1 for reset fee submission\n\t \t \t Press 2 for fill the II nd installment\n\t \t \t Press 3 for go to option's")
                                print("\t \t \t Press 4 for change work place\n\t \t \t Press 5 for exit")
                                pd=input("Select any one option of a given following = ")
                                if(pd.isdigit()==True):
                                    if(pd=="1"):
                                        print("\n\n########################################################################################")
                                        print("THE FEE SUBMISSION IS RESETED")
                                        print("########################################################################################\n")
                                        break
                                    elif(pd=="2"):
                                        print("\n\n########################################################################################")
                                        print("THE II nd INSTALLMENT IS RESETED")
                                        print("########################################################################################\n")
                                        pass
                                    elif(pd=="3"):
                                        print("\n\n########################################################################################")
                                        print("THE OPTION'S MENU IS RESETED")
                                        print("########################################################################################\n")
                                        home1()
                                    elif(pd=="4"):
                                        print("\n\n########################################################################################")
                                        print("THE WORK PLACE IS RESETED")
                                        print("########################################################################################\n")
                                        options()
                                    elif(pd=="5"):
                                        print("\n\n\n\nBye... Bye...")
                                        exit(home1)
                                    else:
                                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!AGAIN...you given any other option (except 1 & 2) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                        print("\n\t \t \t Press 1 for reset fee submission\n\t \t \t Press 2 for fill the II nd installment\n\t \t \t Press 3 for go to option's")
                                        print("\t \t \t Press 4 for change work place\n\t \t \t Press 5 for exit")
                                        pd=input("Select any one option of a given following = ")
                                        pass
                                        if(pd=="1"):
                                            print("\n\n########################################################################################")
                                            print("THE FEE SUBMISSION IS RESETED")
                                            print("########################################################################################\n")
                                            break
                                        elif(pd=="2"):
                                            print("\n\n########################################################################################")
                                            print("THE II nd INSTALLMENT IS RESETED")
                                            print("########################################################################################\n")
                                            pass
                                        elif(pd=="3"):
                                            print("\n\n########################################################################################")
                                            print("THE OPTION'S MENU IS RESETED")
                                            print("########################################################################################\n")
                                            home1()
                                        elif(pd=="4"):
                                            print("\n\n########################################################################################")
                                            print("THE WORK PLACE IS RESETED")
                                            print("########################################################################################\n")
                                            options()
                                        elif(pd=="5"):
                                            print("\n\n\n\nBye... Bye...")
                                            exit(home1)
                                        
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                else:
                                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!AGAIN...you given any other option (except 1 & 2) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                    print("\n\t \t \t Press 1 for reset fee submission\n\t \t \t Press 2 for fill the II nd installment\n\t \t \t Press 3 for go to option's")
                                    print("\t \t \t Press 4 for change work place\n\t \t \t Press 5 for exit")
                                    pd=input("Select any one option of a given following = ")
                                    pass
                                    if(pd=="1"):
                                        print("\n\n########################################################################################")
                                        print("THE FEE SUBMISSION IS RESETED")
                                        print("########################################################################################\n")
                                        break
                                    elif(pd=="2"):
                                        print("\n\n########################################################################################")
                                        print("THE II nd INSTALLMENT IS RESETED")
                                        print("########################################################################################\n")
                                        pass
                                    elif(pd=="3"):
                                        print("\n\n########################################################################################")
                                        print("THE OPTION'S MENU IS RESETED")
                                        print("########################################################################################\n")
                                        home1()
                                    elif(pd=="4"):
                                        print("\n\n########################################################################################")
                                        print("THE WORK PLACE IS RESETED")
                                        print("########################################################################################\n")
                                        options()
                                    elif(pd=="5"):
                                        print("\n\n\n\nBye... Bye...")
                                        exit(home1)
                                    else:
                                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!AGAIN...you given any other option (except 1 & 2) which is invalid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                                        print("\n\t \t \t Press 1 for reset fee submission\n\t \t \t Press 2 for fill the II nd installment\n\t \t \t Press 3 for go to option's")
                                        print("\t \t \t Press 4 for change work place\n\t \t \t Press 5 for exit")
                                        pd=input("Select any one option of a given following = ")
#+=====================================================================================================

                                # TO be continued



#+=====================================================================================================
                                    
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid alphabets except Y/N^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the digit or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
        elif(I=="N" or I=="n"):
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You must have to pay the first fee then you should proceed^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------There are some options please select any one---------------------------------------")
            print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
            print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
            pp=input("Enter the any one digit option which given upward = ")
            if(pp.isdigit()==True):
                if(pp=="1"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                    submitfee()
                elif(pp=="2"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                    home1()
                elif(pp=="3"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                    admission()
                elif(pp=="4"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                    Feelist()
                elif(pp=="5"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                    options()
                elif(pp=="6"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\t\t\t\t\tBye... Bye...")
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                    print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                    pp=input("Enter the any one digit option which given upward = ")
                    pass
                    if(pp=="1"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                        submitfee()
                    if(pp=="2"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                        home1()
                    if(pp=="3"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                        admission()
                    if(pp=="4"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                        Feelist()
                    if(pp=="5"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                        options()
                    if(pp=="6"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\t\t\t\t\tBye... Bye...")
                        exit(home1)
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the alphabet's or sing which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                pp=input("Enter the any one digit option which given upward = ")
                pass
                if(pp=="1"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                    submitfee()
                elif(pp=="2"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                    home1()
                elif(pp=="3"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                    admission()
                elif(pp=="4"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                    Feelist()
                elif(pp=="5"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                    options()
                elif(pp=="6"):
                    print("\n\n\t\t\t\tYou chossen option ",pp)
                    print("\n\n\t\t\t\t\tBye... Bye...")
                    exit(home1)
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You have given the invalid digit's except given upwards^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    print("\n\n\n\t\t\t\tPress 1 if you want to submmit fee of another student\n\t\t\t\tPress 2 if you want to go in option's")
                    print("\t\t\t\tPress 3 for go to admission\n\t\t\t\tPress 4 to see the fee list\n\t\t\t\tPress 5 to change the work place\n\t\t\t\tPress 6 for exit")
                    pp=input("Enter the any one digit option which given upward = ")
                    pass
                    if(pp=="1"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________FEE SUBMISSION IS RESETED_________________________________________\n\n")
                        submitfee()
                    if(pp=="2"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S OPTON _________________________________________\n\n")
                        home1()
                    if(pp=="3"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________WELCOME TO ADMISSION_________________________________________\n\n")
                        admission()
                    if(pp=="4"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________WELCOME TO FEE LIST _________________________________________\n\n")
                        Feelist()
                    if(pp=="5"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\n\n___________________________________________________CHOOSE YOUR'S WORK PLACE _________________________________________\n\n")
                        options()
                    if(pp=="6"):
                        print("\n\n\t\t\t\tYou chossen option ",pp)
                        print("\n\n\t\t\t\t\tBye... Bye...")
                        exit(home1)
                    









#------------------------------------------------------------------------------------------------------------------------------------
options()
home1()
