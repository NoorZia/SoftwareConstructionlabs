import unittest
import restuarant
import numpy as np
class TestRestuarant(unittest.TestCase):

    def test_book(self):
        self.assertEqual(restuarant.booking_test("medium","noor",14),"true")
    def test_book2(self):
        self.assertEqual(restuarant.booking_test("large","noor",10),"false")

    def test_exlarge(self):
        self.assertEqual(restuarant.booking_test("exlarge","noor",12,6),"true")
    def test_exlarge2(self):
        self.assertEqual(restuarant.booking_test("exlarge","noor",12,15),"false")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRestuarant)
    unittest.TextTestRunner(verbosity=2).run(suite)
