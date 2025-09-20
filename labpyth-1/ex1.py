class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group 
        self.grades = grades

    def average_grade(self):
        return sum(self.grades)/len(self.grades)

    def is_excellent(self):
        return self.average_grade() >= 4.5


students = []

with open('student.txt', "r", encoding="utf-8") as file:
    for line in file:
        name, group, grades_str = line.split(";")
        grades = list(map(int, grades_str.split(',')))
        students.append(Student(name, group, grades))

with open("excellent_students.txt", "w", encoding="utf-8") as f:
    for student in students:
        if student.is_excellent():
            f.write(f"{student.name};{student.group};{','.join(map(str, student.grades)), student.average_grade()}\n")