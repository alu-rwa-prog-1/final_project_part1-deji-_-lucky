#Adio Roheen
#Lucky John Mbikeshimana


''' Here are all classes for PlutoHealth and their corresponding functions:  '''


''' We start with the Hospital's function! '''
class Hospital:
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctor,NumberofNurses,Doctors,Ratings,Services):

        ''' We start with creating a hospital.'''

        self.Name=Name
        self.Location=Location
        self.Registration=Registration
        self.Ownership=Ownership
        self.Insurance=Insurance
        self.NumberofDoctor=NumberofDoctor
        self.NumberofNurses=NumberofNurses
        self.Doctors=Doctors,
        self.Ratings=Ratings
        self.Services=Services

        print("A new Hospital has been added. Welcome to Pluto Health! ")


    def __repr__(self):

        return 'Hospital Name: {} '.format(self.Name)
Hospital9=Hospital("ad","IB","ASDFD","P","HGH","2","8","Dov",6,"ASD")


''' We create doctors class by inheriting the characters of the hospital; parent.'''

class Doctors(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services,DoctorName,Specialization,Gender):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services)
        self.DoctorName=DoctorName
        self.Specialization=Specialization
        self.Gender=Gender
    def __repr__(self):
        return 'Hospital Name: {} '.format(self.Name)

''' We create Insurance class by inheriting the characters of the hospital; parent.'''
class Insurance(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services,InsuranceName,ID):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services)
        self.InsurannceName=InsuranceName
        self.ID=ID

''' We create patient class by inheriting the characters of the hospital; parent.'''
class Patient(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services,NOP,Ailment,Detection,Terminal):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services)
        self.Nop=NOP
        self.Ailment=Ailment
        self.Detection=Detection
        self.Terminal=Terminal
        print("A new patient has been added")


