from pydantic import BaseModel, EmailStr, field_validator
import unittest
# from typing 
class Library(BaseModel):
    email: EmailStr
    uid: int

    @field_validator("uid")
    def validate_uid(cls, value):
        if value == 0x0721:
            raise ValueError("you can't 0712 in library!")
        return value
    

class Test(unittest.TestCase):
    def test0721(self):
        with self.assertRaises(ValueError):
            lib = Library(email="Ayachi@nene.com", uid=0x0721)


if __name__ == "__main__":
    unittest.main()