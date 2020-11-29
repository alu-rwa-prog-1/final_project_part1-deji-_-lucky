#Lucky John Mbikeshimana
#Adio Roheen

import unittest

from PlutoApp import *



if __name__ == "__main__":
    unittest.main()


''' Testing Patients class'''

#Testing the Verification for Login ID

def test_PatientValidID(Hospital2):

    self.assertEqual(Hospital2( "", "", "A0056"), "A0056") #This results into being successful.


def test_PatientValidID(Hospital2):

    self.assertEqual(Hospital2( "", "", "A0056"), "A0036") #This fails.


#Testing the Patient's Location

def test_PatientLocation(Hospital2):

    self.assertIs(Hospital2("", "Tokyo"), "Tokyo") #This is successful.

def test_PatientLocation(Hospital2):

    self.assertIs(Hospital2("", "Tokyo"), "Tokyo") #This is successful.


#Testing the name


def test_Name(Hospital2):

    self.assertEqual(Hospital2("","","","","","","","","","Dr Adedeji")) #This is successful.




class TestHospital(unittest.TestCase):
    def test_HospitalName(self):
        Hospital2=Hospital("ICH","Tokyo","AOQ12","Public",["Goldberg","UK INSURANCE","Ifeoma"],25,29,["Dr Adedeji,Padaetrician","Dr Yemi,Optician","Dr Awopegba,Surgeon"],5,["Dentistry","Optical Services"])
        Hospital3=Hospital("Redmond","Oyo","A1234","private",["Midhealth","Made in Lagos","Gyrate"],255,145,["Dr Bayo,Optometrist","Dr Busrat,Nephrologist"],4,["Optical services","Dentistry","ENT","SURGERY"])
        self.assertEqual(Hospital2.Name,"ICH")
        self.assertEqual(Hospital3.Name,"Redmond")

        Hospital2.Name="Highland"
        Hospital3.Name="Alaafia"
        self.assertEqual(Hospital2.Name,"Highland")
        self.assertEqual(Hospital3.Name,"Alaafia")
    def test_HospitalRegistration(self):
        Hospital2 = Hospital("ICH", "Tokyo", "AOQ12", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29,
                             ["Dr Adedeji,Padaetrician", "Dr Yemi,Optician", "Dr Awopegba,Surgeon"], 5,
                             ["Dentistry", "Optical Services"])
        Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145,
                             ["Dr Bayo,Optometrist", "Dr Busrat,Nephrologist"], 4,
                             ["Optical services", "Dentistry", "ENT", "SURGERY"])
        self.assertEqual(Hospital2.Registration, "AOQ12")
        self.assertEqual(Hospital3.Registration, "A1234")
        Hospital2.Registration="B134E"
        Hospital3.Registration="VE567"
        self.assertEqual(Hospital2.Registration,"B134E")
        self.assertEqual(Hospital3.Registration,"VE567")
    def test_WrongName(self):
        Hospital2 = Hospital("ICH", "Tokyo", "AOQ12", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29,
                             ["Dr Adedeji,Padaetrician", "Dr Yemi,Optician", "Dr Awopegba,Surgeon"], 5,
                             ["Dentistry", "Optical Services"])
        Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145,
                             ["Dr Bayo,Optometrist", "Dr Busrat,Nephrologist"], 4,
                             ["Optical services", "Dentistry", "ENT", "SURGERY"])
        self.assertEqual(Hospital2.Name,"ICH")
        self.assertEqual(Hospital3.Name,"Redmond")

        self.assertNotEqual(Hospital2.Name,8908)
        self.assertNotEqual(Hospital3.Name,6789)
    def test_WrongRegistion(self):
        Hospital2 = Hospital("ICH", "Tokyo", "AOQ12", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29,
                             ["Dr Adedeji,Padaetrician", "Dr Yemi,Optician", "Dr Awopegba,Surgeon"], 5,
                             ["Dentistry", "Optical Services"])
        Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145,
                             ["Dr Bayo,Optometrist", "Dr Busrat,Nephrologist"], 4,
                             ["Optical services", "Dentistry", "ENT", "SURGERY"])
        self.assertEqual(Hospital2.Registration,"AOQ12")
        self.assertEqual(Hospital3.Registration,"A1234")

        self.assertNotEqual(Hospital2.Registration,11234)
        self.assertNotEqual(Hospital3.Registration,2367)
    def test_Rating(self):
        Hospital2 = Hospital("ICH", "Tokyo", "AOQ12", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29,
                             ["Dr Adedeji,Padaetrician", "Dr Yemi,Optician", "Dr Awopegba,Surgeon"], 5,
                             ["Dentistry", "Optical Services"])
        Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145,
                             ["Dr Bayo,Optometrist", "Dr Busrat,Nephrologist"], 4,
                             ["Optical services", "Dentistry", "ENT", "SURGERY"])
        self.assertEqual(Hospital2.Ratings,5)
        self.assertEqual(Hospital3.Ratings,4)

        self.assertNotEqual(Hospital2.Ratings,"Ife")
        self.assertNotEqual(Hospital3.Ratings,"Dan8i")

    def Test_InsuranceID(self):
        Insurance1=PlutoInsurance(1,"UK DELIGHT","Yearly")
        Insurance2=PlutoInsurance(2,"Gold","Monthly")
        self.assertEqual(Insurance1.InsuranceID,1)
        self.assertEqual(Insurance2.InsuranceID,2)

        Insurance1.InsuranceID=12
        Insurance2.InsuranceID=10
        self.assertEqual(Insurance1.InsuranceID,12)
        self.assertEqual(Insurance2.InsuranceID,10)



class TestPlutoInsurance(unittest.TestCase):

    def Test_InsuranceID(self):
        Insurance1 = PlutoInsurance(1, "Delight", "Yearly")
        Insurance2 = PlutoInsurance(2, "Gold", "Monthly")

        self.assertEqual(Insurance1.InsuranceID,1)
        self.assertEqual(Insurance2.InsuranceID,2)

        Insurance1.InsuranceID=12
        Insurance2.InsuranceID=10

        self.assertEqual(Insurance1.InsuranceID,"12")
        self.assertEqual(Insurance2.InsuranceID,"10")

    def TestInsurance_Name(self):
        Insurance1 = PlutoInsurance(1, "UK DELIGHT", "Yearly")
        Insurance2 = PlutoInsurance(2, "Gold", "Monthly")
        self.assertEqual(Insurance1.InsuranceName, "UK DELIGHT")
        self.assertEqual(Insurance2.InsuranceID, "GOLD")

        Insurance1.InsuranceName="Healthline"
        Insurance2.InsuranceName="Health plus"
        self.assertEqual(Insurance1.InsuranceName,"Healthline")
        self.assertEqual(Insurance1.InsuranceName,"Health plus")

    def Test_WrongInsuranceName(self):
        Insurance1 = PlutoInsurance(1, "UK DELIGHT", "Yearly")
        Insurance2 = PlutoInsurance(2, "Gold", "Monthly")
        self.assertEqual(Insurance1.InsuranceName,"UK DELIGHT")
        self.assertEqual(Insurance2.InsuranceName,"Gold")

        self.assertNotEqual(Insurance1.InsuranceName,123)
        self.assertNotEqual(Insurance2.InsuranceName,4657)

    def Test_WrongInsuranceID(self):
        Insurance1 = PlutoInsurance(1, "UK DELIGHT", "Yearly")
        Insurance2 = PlutoInsurance(2, "Gold", "Monthly")
        self.assertEqual(Insurance1.InsuranceID, 1)
        self.assertEqual(Insurance2.InsuranceName, 2)

        self.assertNotEqual(Insurance1.InsuranceID, "AA")
        self.assertNotEqual(Insurance2.InsuranceID, "mAFO")