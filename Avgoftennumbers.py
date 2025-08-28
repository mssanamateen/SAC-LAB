count=0
total=0
while count <10:
    num=int(input(f"Enter number{count+1}:"))
    total+=num
    count+=1
avg=total/10
print("average of 10 numbers is:",avg)