#Adio Roheen
#Lucky John Mbikeshimana



from pluto import *
hospital=[]
Yes=[]

''' Here we add two hospitals' credentials on our hospitals lists. '''

Hospital2=Hospital("ICH","Tokyo","A0056","Public",["Goldberg","UK INSURANCE","Ifeoma"],25,29,["Dr Adedeji,Padaetrician","Dr Yemi,Optician","Dr Awopegba,Surgeon"],5,["Dentistry","Optical Services"])
hospital.append(Hospital2)
Hospital3=Hospital("Redmond","Oyo","A1234","private",["Midhealth","Made in Lagos","Gyrate"],255,145,["Dr Bayo,Optometrist","Dr Busrat,Nephrologist"],4,["Optical services","Dentistry","ENT","SURGERY"])
hospital.append(Hospital3)
Yes.append(Hospital2.Doctors)


print("Welcome to PlutoHealth Hospital!! ")
print("We look forward to working with you!! ")

'''Here we ask the user to choose the right action he would like to take: '''


PlutoHealth = True

while PlutoHealth:
    
    ''' Here we ask what kind of the user is using Pluto Health; '''

    PlutoUserType = int(input(str("Do you want to use Pluto Health as a Hospital or Patient? Type 1 for Hospital and Type 2 for Patient.  ")))

    if PlutoUserType ==1:
        
        Input = int(input("Choose the activity you would like to perform: \n"
    
            " Press 1 for Joining our team\n"
            "Press 2 for Viewing the list of hospitals\n"
            "Press 3 for adding patients \n"
            "Press 4 for Viewing Your Doctor's List\n"
            "Press 5 for Viewing your Insurance List\n"
            "Press 6 for adding a doctor to your list\n"
            "Press 7 to Add an Insurance company"))



        ''' When the Pluto Health user is a Hospital that would like to join the platform. '''

        if Input == 1:
            print("Thanks for Choosing to join us")
            Name = input("Enter the name of your Hospital: ")
            Location = input("Enter the location of the hospital: ")
            Registration = input("Enter the registration ID: ")
            Ownership = input("Is it a Private or Public Company? Type '1' for Private and '2' for Public: ")
            Insurance = input("Does your hospital have insurance registered Under it,If yes List them")
            
            if Insurance == "No":
                print("You have to be registered under an Insurance Scheme for you to be on  Pluto")
                exit("Thank You")
    


'''
     Here we ask the doctor more information on the number of doctors & nurses it has, etc. 

'''
    Doc = int(input('Kindly Input the number of Doctors in your Hospital: '))
    Nurses = int(input("Kindly input the number of Nurses in your Hospital: "))
    Dokita=input("Name of Doctors: ")
    Bentley=[]
    Dokita1=input()
    Bentley.append(Dokita)
    Bentley.append(Dokita1)

        ''' Here we ask the user to show us the rating as well as we make a list of the services offered on Pluto Health. '''

    Ratings = int(input("Kindly input your ratings as given on google.Ratings would be verified: "))
    Service = input("Kindly give us a list of your first service offered: ")
    Service1 = input("Second service offered: ")
    service2 = input("Third Service offered: ")

    ''' We then make a list of the services offered here!!!  '''

    List = []
    List.append(Service)
    List.append(Service1)
    List.append(service2)
    print("Your services are",List)

    Your=[]
    Hospital1=Hospital(Name,Location,Registration,Ownership,Insurance,Doc,Nurses,Bentley,Ratings,Service)
    Your.append(Hospital1)
    print(Your)
    print(Hospital1.Doctors)


''' Viewing the list of hospitals available on Plutto Health'''

        elif Input  == 2:
            for x in hospital:
                print(x)

''' Adding a patient to Pluto Health.'''

        elif Input==3:
            Name = input("What is the Name of your Hospital: ")
            Location = input("Where is the location of the hospital: ")
            Registration = input("What is the registration ID: ")
            Ownership = input("Is it a private or public Company: ")
            Insurance = input("Does your hospital have insurance registered Under it: ")
            Doc = int(input('Kindly Input the number of Doctors in your Hospital: '))
            Nurses = int(input("Kindly input the number of Nurses in your Hospital: "))
            infinity=input()
            Ratings = int(input("Kindly input your ratings as given on google.Ratings would be verified: "))
            Service = input("Kindly give us a list of your services: ")
            patient = input("Kindly input the patients name: ")
            Ailment = input("Kindly enter the Ailment of the patient: ")
            Detection = input("Kindly enter the date the ailment was detected: ")
            Terminal = input("Is it a terminal disease? ")
            New_Patient = Patient(Name,Location,Registration,Ownership,Insurance,Doc,Nurses,infinity,Ratings,Service,patient,Ailment,Detection,Terminal)


''' Viewing the Pluto Health Insurance List. '''

            elif Input == 5:
                Hospital_Name = input("Kindly enter the name of your Hospital: ")
                
                if Hospital_Name == "Redmond":
                    for x in Hospital2.Insurance:
                        print (x)

                elif Hospital_Name == "ICH":
                    for x in Hospital3.Insurance:
                        print(x)

''' Viewing Doctor's List! '''

            elif Input==4:
                HospitalDoctor=input("Kindly enter your hospital: ")
                
                if HospitalDoctor=="Redmond":
                    print(Hospital2.Doctors)
                
                elif HospitalDoctor=="ICH":
                    for x in Hospital3.Doctors:
                        print (Hospital3.Doctors)

''' Adding a doctor to your list. '''

            elif Input==6:
                Hospital_Append=input("Kindly enter your Hospital name: ")
                New_Doctor=input("Kindly enter the new Doctor you would like to enter: ")
                
                if Hospital_Append =="ICH":
                    Yes.append(New_Doctor)
                    print(Yes)

                elif Hospital_Append=="Redmond":
                    Ayo=[]
                    Ayo.append(Hospital3.Doctors)
                    Ayo.append(New_Doctor)
                    print(Ayo)


''' Adding an Insurance Company to Pluto Health'''

            elif Input==7:
                H=input("Kindly enter the name of yor hospital")
                L=input("Kindly input the name of your new insurance company")
                if H=="ICH":
                    K=[]
                    K.append(Hospital2.Insurance)
                    K.append(L)
                    print(K)
                elif H=="Redmond":
                    Finally=[]
                    Finally.append(Hospital3.Insurance)
                    Finally.append(L)
                    print(Finally)
    

    ''' For patients using PlutoHealth'''
    
    elif PlutoUserType ==2:
        print("Welcome to Pluto Patient!!! ")
        Input5 = int(str(" Choose the action to take; '1' to SignUp to Pluto Patient, '2' to Terminate using Pluto Health: "))


        if Input5==1:
            Name = input("What is the Name of your Hospital: ")
            Location = input("Where is the location of the hospital: ")
            Registration = input("What is the registration ID: ")
            Ownership = input("Is it a private or public Company: ")
            Insurance = input("Does your hospital have insurance registered Under it: ")
            Doc = int(input('Kindly Input the number of Doctors in your Hospital: '))
            Nurses = int(input("Kindly input the number of Nurses in your Hospital: "))
            infinity=input()
            Ratings = int(input("Kindly input your ratings as given on google.Ratings would be verified: "))
            Service = input("Kindly give us a list of your services: ")
            patient = input("Kindly input the patients name: ")
            Ailment = input("Kindly enter the Ailment of the patient: ")
            Detection = input("Kindly enter the date the ailment was detected: ")
            Terminal = input("Is it a terminal disease? ")
            New_Patient = Patient(Name,Location,Registration,Ownership,Insurance,Doc,Nurses,infinity,Ratings,Service,patient,Ailment,Detection,Terminal)

        elif Input5==2:
            '''Here the patient can terminate his insurance!! '''

            validateTermination = input(str("Are you sure you want to terminate using Pluto Health? Type YES: "))

            if validateTermination.lower()=="yes":
                print("Thanks for believing in us and we look forward to you relying on us again")
                print("==============================================================")
                print("Our services are always available.")
        
            else:
                print("YOUR SESSION HAS ENDED !!!!")