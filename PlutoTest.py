import unittest
from pluto import PlutoInsurance

if __name__ == "__main__":
    unittest.main()


class Testinsurancepluto(unittest.TestCase):
    def test_New(self):
        Insurance1=PlutoInsurance(1,"Detty December","Yearly")
        Insurance2=PlutoInsurance(2,"Detty","Monthly")
        self.assertNotEqual(Insurance1.InsurancePlan,1)
        self.assertNotEqual(Insurance2.InsurancePlan,2)


    def test_InsuranceID(self):
        Insurance1 = PlutoInsurance(1, "Delight", "Yearly")
        Insurance2 = PlutoInsurance(2, "Gold", "Monthly")

        self.assertEqual(Insurance1.InsuranceID, 1)
        self.assertEqual(Insurance2.InsuranceID, 2)

        Insurance1.InsuranceID = 12
        Insurance2.InsuranceID = 10

        self.assertEqual(Insurance1.InsuranceID, 12)
        self.assertEqual(Insurance2.InsuranceID, 10)

    def test_InsuranceName(self):
        Insurance1 = PlutoInsurance(1, "UK DELIGHT", "Yearly")
        Insurance2 = PlutoInsurance(2, "Gold", "Monthly")
        self.assertEqual(Insurance1.InsuranceName, "UK DELIGHT")
        self.assertEqual(Insurance2.InsuranceName, "Gold")
        Insurance1.InsuranceName="Express"
        Insurance2.InsuranceName="Zenith"
        self.assertEqual(Insurance1.InsuranceName, "Express")
        self.assertEqual(Insurance2.InsuranceName, "Zenith")




    def test_WrongInsuranceName(self):
        Insurance1 = PlutoInsurance(1, "UK DELIGHT", "Yearly")
        Insurance2 = PlutoInsurance(2, "Gold", "Monthly")
        self.assertEqual(Insurance1.InsuranceName, "UK DELIGHT")
        self.assertEqual(Insurance2.InsuranceName, "Gold")

        self.assertNotEqual(Insurance1.InsuranceName, 123)
        self.assertNotEqual(Insurance2.InsuranceName, 4657)

    def test_WrongInsuranceID(self):
        Insurance1 = PlutoInsurance(1, "UK DELIGHT", "Yearly")
        Insurance2 = PlutoInsurance(2, "Gold", "Monthly")
        self.assertNotEqual(Insurance1.InsuranceID, "Mafo")
        self.assertNotEqual(Insurance2.InsuranceName, "GUI")













