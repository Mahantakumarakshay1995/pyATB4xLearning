class Employee:
    name = None
    age = None
    phone = None
    adress = None
    eid = None
    def __init__(self,id,name,age,phone,adress):
        self.eid=id
        self.name=name
        self.age=age
        self.phone=phone
        self.adress=adress
    def walk(self):
        print("Walking")

    def talk(self):
        print("talking")
    def printadress(self):
        pass

e1 = Employee(101,"Akshay",30,1234,"KA")
e2 = Employee(102,"veram",30,4321,"OD")


