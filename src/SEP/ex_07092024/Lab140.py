#ABC is a class from where we have to inherit abstratct method
from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self,name):
        self.name=name
    def loan(self):
        pass
class Son(Father):
    def loan(self):
        print("Paid the loan amount is-->"+ self.name)

akm = Son("1L")
akm.loan()