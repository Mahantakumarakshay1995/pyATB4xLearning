class A:
    static_a = 10
    @staticmethod
    def Run():
        print("Running")

A.Run()
print(A.static_a)
