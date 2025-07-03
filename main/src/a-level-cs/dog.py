
from animal import Animal

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} says: Woof! (Breed: {self.breed})")