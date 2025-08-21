number=int(input("Enter a number up to which you want to find the average"))
i=0
sum=0
while i< number:
	i=i+1
	sum=sum+i
average=sum/i
print(f"The average of {number} natural number is {average}")