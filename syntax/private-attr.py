import unittest

class A:
    def __init__(self) -> None:
        self.__name = "a"

class Test(unittest.TestCase):

    def test(self) -> None:

        a = A()

        self.assertEqual(
            a.__dict__,
            {'_A__name': 'a'}
        )
        
        self.assertEqual(
            a._A__name, "a"
        )

if __name__ == "__main__":
    unittest.main()