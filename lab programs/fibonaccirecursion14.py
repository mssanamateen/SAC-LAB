def fibonacci(n):
    '''nth term in fibonacci series'''
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter n: "))
print(f"{n}th term in Fibonacci series is:", fibonacci(n))
