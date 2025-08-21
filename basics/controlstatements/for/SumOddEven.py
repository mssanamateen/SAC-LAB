n=int(input("enter the limit:"))
even=odd=0
for i in range(n):
	if(i%2==0):
		even+=i
	else:
		odd+=i
print(f"sum of even numbers are {even}, odd numbers are {odd}")