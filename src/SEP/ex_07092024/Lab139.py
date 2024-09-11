from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name
        @abstractmethod
        def sound():
            pass

class Dog(Animal):

    def sound(self):
        print("Bark")

lab = Dog("som")
lab.sound()