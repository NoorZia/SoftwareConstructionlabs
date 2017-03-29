import unittest
import restuarant_db as restuarant
import numpy as np
class TestRestuarant(unittest.TestCase):

    def test_book(self):
        self.assertEqual(restuarant.booking_test("medium","noor",13),True)
    def test_book2(self):
        self.assertEqual(restuarant.booking_test("large","noor",10),False)
    def test_book3(self):
        self.assertEqual(restuarant.booking_test("small","noor",17),True)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRestuarant)
    unittest.TextTestRunner(verbosity=2).run(suite)
