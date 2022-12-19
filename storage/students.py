from dataclasses import dataclass

from storage.base import BaseModel


@dataclass
class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    gender: str
    country: str

"""    @classmethod
    def get_student_by_id(self):
        res = self.exec()
        """
