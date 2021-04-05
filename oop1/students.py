class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


student1 = Student("Ana", 20, 12)
student2 = Student("Josh", 19, 4)
student3 = Student("Paul", 22, 10)

course = Course("AND1", 50)
course.add_student(student2)
course.add_student(student3)
# print(course.students[0].name)
print(course.get_average_grade())
print(course.add_student("Franciska"))
