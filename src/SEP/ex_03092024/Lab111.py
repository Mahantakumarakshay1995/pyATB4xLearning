class Calc:
    def sum(self,a,b):
        return a+b
    def sub(self, a, b):
        return a - b

or_r = Calc()
a=int(input("Enter num1"))
b=int(input("Enter num2"))
op_sum=or_r.sum(a,b)
op_sub = or_r.sub(a,b)

print(op_sum)
print(op_sub)

glo




