import unittest
from unit_test_lesson2 import*

class TestAdder(unittest.TestCase):
    def test_adder(self):
        self.assertEqual(adder(1,2,3),6)
    def test_adder_kwargs(self):
        self.assertEqual(adder(a=1,b=2,c=3), 6)
        self.assertEqual(adder(1,2,a=3,b=4), 10)

if __name__ == "__main__":
    unittest.main()
    
