'''
Author: Ler2sq
Data: 2023-12-6
'''

from typing import Literal


# IMPORTANT: 为了维护 为Literal字面量枚举创建一个新类
GenderType = Literal["male", "female", "helicopter"]

class Person:
    def __init__(self, gender: GenderType) -> None:
        self.gender = gender

g: GenderType = "helicopter"
person = Person(gender=g)