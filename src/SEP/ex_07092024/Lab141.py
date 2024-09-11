from abc import ABC, abstractmethod
class PyATB(ABC):
    @abstractmethod
    def pay_fee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Amit(PyATB):
    def pay_fee(self):
        print("Paid")
akm = Amit()
akm.enrolled()
akm.pay_fee()

