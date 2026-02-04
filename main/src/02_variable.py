# src/variable.py
'''
This module demonstrates variable assignments and types in Python.
It includes functions to return different types of variables and print their types. 
It also shows how to print boolean values and formatted strings.

'''

# Variable assignment examples
number: int = 25
text: str = "twenty five"
full_name: str = "Ahmet Ahmetoglu"
details: str = f"{number} {72.5} {True}"    

print(type(number))          # <class 'int'>
print(type(text))            # <class 'str'>
print(type(details))         # <class 'str'>    
print(type(True))            # <class 'bool'>

#variable reassignment
number = 26
weight: float = 72.5
is_student: bool = False
print(f"{number} {weight} {is_student}")  # 26 72.5 False
print("2021-09-01 12:00:00")

# Final formatted string
first_name: str = "Ahmet"
last_name: str = "Ahmetoglu"
age: int = 25
weight: float = 74.5
is_student: bool = True
print(f"{first_name} - {last_name} - {age} - {weight} - {is_student}")  # Ahmet - Ahmetoglu - 25 - 74.5 - True


# multiple variable assignments
a, b, c = 1, 2.5, "Hello"
print(a)  # 1
print(b)  # 2.5
print(c)  # Hello



# Functions to return variables of different types

def get_integer():
    return 25


def get_string():
    return "twenty five"


def get_name():
    return "Ahmet Ahmetoglu"


def get_details():
    age = 25
    weight = 72.5
    is_student = True
    return f"{age} {weight} {is_student}"


def print_variable_types():
    print(type(get_integer()))
    print(type(get_string()))
    print(type(get_details()))
    print(type(True))


def print_boolean_values():
    print(True)
    print(True)
    print(True)
    print(True)


def print_combined_details():
    age = 26
    weight = 72.5
    is_student = False
    print(f"{age} {weight} {is_student}")


def print_datetime():
    print("2021-09-01 12:00:00")


def print_final_details():
    first_name = "Ahmet"
    last_name = "Ahmetoglu"
    age = 25
    weight = 74.5
    is_student = True
    print(f"{first_name} - {last_name} - {age} - {weight} - {is_student}")


def print_all():
    print(get_integer())
    print(type(get_integer()))
    print(get_string())
    print(get_name())
    print(get_details())
    print_variable_types()
    print_boolean_values()
    print_combined_details()
    print_datetime()
    print(type(get_string()))
    print(True)
    print_final_details()


if __name__ == "__main__":
    print_all()
