# Method OverLoading
# Python does not support method overloading
# in the Traditional Sense

class A:
    def m(self):

        print("Printing m**")


class B(A):
    def m(self):

        print("Printing child m**")


class c:
    b1 = A()
    b1.m()
