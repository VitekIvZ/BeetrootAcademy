#task1lesson16.py

"""
    School

Make a class structure in python representing people at school. 
Make a base class called Person, a class called Student, and another one called Teacher. 
Try to find as many methods and attributes as you can which belong to different classes, 
and keep in mind which are common and which are not. 
For example, the name should be a Person attribute, while salary should only be available 
to the teacher. 
    """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, grades=None):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Average Grade: {self.get_average_grade():.2f}")


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}, Salary: {self.salary}")


if __name__ == "__main__":
    student = Student("Alice", 20, "S12345", [90, 85, 88])
    teacher = Teacher("Mr. Smith", 40, "Mathematics", 50000)

    student.display_info()
    
    teacher.display_info()
    
    
    
