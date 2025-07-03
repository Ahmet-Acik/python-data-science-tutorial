# main/src/a-level-cs/person.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Private attribute

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Student ID: {self.student_id}")


# Example usage
if __name__ == "__main__":
    person = Person("Alice", 18)
    person.display_info()
    person.set_age(21)
    print("Updated age:", person.get_age())
    person.set_age(-5)  # Will print a warning

    person1 = Person("Alice", 18)
    person2 = Person("Bob", 20)
    person1.display_info()
    person2.display_info()

    student = Student("Charlie", 19, "S12345")
    student.display_info()
