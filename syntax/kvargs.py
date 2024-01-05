import unittest

def f(a, b, c):
    return a + b + c

kvargs = {"a": 1, "b": 2, "c": 3}

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(**kvargs), 6)

if __name__ == "__main__":
    unittest.main()