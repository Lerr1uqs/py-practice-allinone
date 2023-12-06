import unittest
class Example1:
    # static attribute
    a = 1
    
    def modify(self, a):
        self.a = a

    @staticmethod
    def sm():
        ...
    
    @classmethod
    def cm(cls) -> int:
        return cls.a

    @classmethod
    def cm_modify(cls, a) -> None:
        cls.a = a

class Example2:
    a: int
    
    @classmethod
    def cm(cls) -> int:
        return cls.a


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Example1.cm(), 1)
        e = Example1()
        e.modify(2)
        self.assertEqual(Example1.cm(), 1)

    def test2(self):
        with self.assertRaises(AttributeError):
            # AttributeError: type object 'Example2' has no attribute 'a'
            Example2.cm()

    def test3(self):
        e1 = Example1()
        e2 = Example1()

        Example1.cm_modify(5)
        self.assertEqual(e1.a, 5)# 通过cls修改类全部实例的静态属性

        e2.modify(2)
        self.assertEqual(e2.a, 2)

if __name__ == "__main__":
    unittest.main()

'''
结论 classmethod能访问类静态定义的一些变量的值 但是staticmethod就不行 就这个细微的差别
'''