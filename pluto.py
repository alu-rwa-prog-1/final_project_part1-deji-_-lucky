class Hospital:
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctor,NumberofNurses,Doctors,Ratings,Services):
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
        print("A new Hospital has been added,Welcome officially to our team")
    def password(self):
        return '{}.{}@pluto'.format(self.Name,self.Registration)
    def __repr__(self):
        return 'Hospital Name: {} '.format(self.Name)

    class PlutoInsurance:
        def __init__(self, InsuranceID, InsuranceName, InsurancePlan):
            self.InsuranceID = InsuranceID
            self.InsuranceName = InsuranceName
            self.InsurancePlan = InsurancePlan
            print("Welcome to Pluto Insurance!!! ")


class Doctors(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services,DoctorName,Specialization,Gender):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services)
        self.DoctorName=DoctorName
        self.Specialization=Specialization
        self.Gender=Gender
    def __repr__(self):
        return 'Hospital Name: {} '.format(self.Name)

class Insurance(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services,InsuranceName,ID):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services)
        self.InsurannceName=InsuranceName
        self.ID=ID

class Patient(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services,NOP,Ailment,Detection,Terminal):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Doctors,Ratings,Services)
        self.Nop=NOP
        self.Ailment=Ailment
        self.Detection=Detection
        self.Terminal=Terminal
        print("A new patient has been added")

class PlutoInsurance:
    def __init__(self, InsuranceID, InsuranceName, InsurancePlan):
        self.InsuranceID = InsuranceID
        self.InsuranceName = InsuranceName
        self.InsurancePlan = InsurancePlan
        print("Welcome to Pluto Insurance!!! ")



