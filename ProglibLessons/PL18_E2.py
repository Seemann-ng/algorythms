from typing import List

import numpy as np


class Student:
    def __init__(self, name: str, age: int, grade: str, scores: List[int]):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def avarageScore(self) -> float:
        return round(np.mean(self.scores), 2)


student = Student("John Doe", 15, "8A", [5, 3, 4, 5, 5, 4, 4, 4, 5, 5, 5])
print(f"""Name: {student.name}\n
      Age: {student.age}\n
      Grade: {student.grade}\n
      Scores: {student.scores}\n
      Average score: {student.avarageScore()}""")
