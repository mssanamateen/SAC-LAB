n=int(input("enter the limit:"))
x,y=0,1
count=0
while count<n:
	print(x, end=" ")
	z=x+y
	x=y
	y=z
	count+=1
