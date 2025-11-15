
def factorial(n):
    f=1
    if n!=0 and n!=1:
        return  n*factorial(n-1)
    else:
        return 1


print(factorial(5))