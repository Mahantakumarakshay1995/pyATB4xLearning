class Dog:

    name = None
    age = None

    def __init__(self,name):
        print("Called , Object is created")
        self.name = name
       # self.age = age


    def sleep(self):
        print("Sleeping")
        print("Who is sleeping -->", self.name)

dog1 = Dog("chow")

print(dog1.name)
print(dog1.sleep())

dog2 = Dog("Mow")
print(dog2.sleep())