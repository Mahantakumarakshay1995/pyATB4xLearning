#area
#Logic Building Formula
#Figure out the inputs and Outputs
#input ->r ,data type ,float
#pi->3.14
#power -> pow  or ** any
import math

#O/p ->Float area, print area

#rough logic= area= 3.141*pow(r,2)
#Step-3 write logic
radius=float(input("Enter the Radius of the circle\n"))
area=math.pi*math.pow(radius,2)
area2=3.141*(radius**2)
print("Area of circle is->",area)
print(f"Area of circle is {area:.2f}")
print("Area of circle is->",area2)

