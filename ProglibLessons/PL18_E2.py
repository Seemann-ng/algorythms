from typing import List


class Student:
    def __init__(self, name: str, age: int, grade: str, scores: List[int]):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def avarageScore(self) -> float:
        return round(sum(self.scores) / len(self.scores), 2)


student = Student("John Doe", 15, "8A", [5, 3, 4, 5, 5, 4, 4, 4, 3, 5, 5])
print(f"Name: {student.name}\n"
      f"Age: {student.age}\n"
      f"Grade: {student.grade}\n"
      f"Scores: {student.scores}\n"
      f"Average score: {student.avarageScore()}")
