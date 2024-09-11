class Person:
    def __init__(self):
        self.name = input ("Enter Name\n")
        self.age= input("Enter age-->\n")

    def display_information(self):
        print(f"Name is{self.name}")
        print(f"Name is{self.age}")
p1 = Person()

p1.display_information()