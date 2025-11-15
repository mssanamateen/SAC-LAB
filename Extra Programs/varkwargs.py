def factorial(**kwargs):
  
    for key,value in kwargs.items():
        f=1
        for i in range(1,int(value)+1):
            f=f*i
        print(f"factorial of {value}is {f}")

factorial(n1=2,n2=6,n3=8)
factorial(n1=2,n2=6,n3=8,n4=5)