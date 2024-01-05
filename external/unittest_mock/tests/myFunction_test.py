import unittest
# from .context import myFunction
from src import myFunction

class SumTest(unittest.TestCase):
    def test_Sum(self):
        self.assertEqual(myFunction.Sum(1, 1), 2)
        self.assertTrue(myFunction.Sum(1, 2) == 3)