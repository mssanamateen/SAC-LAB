import sys 
#need it to access command-line arguments
import math 
# to use math.sqrt() (square root function)
#float() converts the arguments from string to  number (because command-line inputs come as text).
s1=float(sys.argv[1])
s2=float(sys.argv[2])
s3=float(sys.argv[3])
#heron's formula is used to calculate the area of triangle when 3 sides are given
#1. calculate  the semi-perimeter of the triangle.
s=(s1+s2+s3)/2
#2. area
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(f" area of traingle is : {area}")

