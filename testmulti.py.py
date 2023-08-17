import unittest
from aufgabe import multipixel 

class Testmulti(unittest.TestCase):
    def test_multi_function(self):
        self.assertEqual(multipixel(2,3),6)

    def test_multi_float_function(self):
        self.assertAlmostEqual(multipixel(2.1, 2), 4.2)


if __name__ == "__main__":
    unittest.main()