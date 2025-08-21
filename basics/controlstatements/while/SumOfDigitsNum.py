num=int(input("enter the number:"))
Original_num=num
sum=0
while num>0:
	digit=num%10
	sum+=digit
	num//=10
print(f"Sum of digits of {Original_num} is {sum}")