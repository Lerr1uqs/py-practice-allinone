'''
Author: Ler2sq
Data: 2023-12-6
'''

from typing import NewType
Uid = NewType("Uid", int)
Atk = NewType("Atk", int)

# 使用newtype创建一个新的type 避免本质相同实质不同的变量之间的赋值
class Test:
    def __init__(self) -> None:
        self.uid: Uid = 1
        self.atk: Atk = 1

    def do(self) -> None:
        self.uid = self.atk # 能被mypy检测出来

t = Test()