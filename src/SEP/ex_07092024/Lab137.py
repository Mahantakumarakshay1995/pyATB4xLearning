class Father:

    def home1(self):
        print("1BHK")


class Son(Father):
    def home(self):
        pass


# super().home()
# print("No House")

akm = Son()
akm.home1()
