#triangle classifier

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a == b == c:
    print("Equilateral")
elif a ==b or b==c or c==a:
    print("Iscoscales")
else:
    print("Scalane")

