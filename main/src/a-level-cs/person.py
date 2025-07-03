class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage
if __name__ == "__main__":
    person1 = Person("Alice", 18)
    person2 = Person("Bob", 20)
    person1.display_info()
    person2.display_info()



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

# Example usage
if __name__ == "__main__":
    student = Student("Charlie", 19, "S12345")
    student.display_info()