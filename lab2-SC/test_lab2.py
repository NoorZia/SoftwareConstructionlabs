import unittest
import lab2
import numpy as np
class TestMultiplication(unittest.TestCase):

    def test_iteration(self):

        a,b = lab2.start_random_population(2,2,2,2)

        self.assertEqual(lab2.iterative(a,b), np.matmul(np.array(a),np.array(b)).tolist())

    def test_stressen(self):

        a,b = lab2.start_random_population(3,3,3,3)

        self.assertEqual(np.matmul(np.array(lab2.padding(a)),np.array(lab2.padding(b))).tolist(), lab2.strassen(a,b,len(a)/2))

    def test_stressen_iteration(self):

        a,b = lab2.start_random_population(4,4,4,4)

        self.assertEqual(lab2.iterative(a,b), lab2.strassen(a,b,len(a)/2))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiplication)
    unittest.TextTestRunner(verbosity=2).run(suite)
