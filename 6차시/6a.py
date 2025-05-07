class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        else:
            return "F"


n = int(input())
students = []

for _ in range(n):
    name, score = input().split()
    s = Student(name, score)
    students.append(s)

for student in students:
    print(f"{student.name} : {student.get_grade()}")
