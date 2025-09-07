a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))

if a==b==c:
	print("All the three numbers are equal")
elif a>=b and a>=c:
	print(f"{a} is the greatest number")
elif b>=a and b>=c:
	print(f"{b} is the greatest number")
else:
	print(f"{c} is the greatest number")