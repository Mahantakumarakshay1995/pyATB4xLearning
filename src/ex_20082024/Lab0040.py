# grade Code
# input - int number
# o/p- Grade

grade = int(input("Enter Marks"))
if 90 <= grade <= 100:
    print("Your grade is", "A")
elif grade >= 80 and grade <= 89:
    print("Your grade is ", "B")
elif grade >= 70 and grade <= 79:
    print("Your grade is ", "C")
elif grade >= 60 and grade <= 69:
    print("Your grade is ", "D")
else:
    print("Your grade is", "F")
