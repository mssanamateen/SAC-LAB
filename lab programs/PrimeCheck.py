num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
elif num == 2 or num == 3:
    print(f"{num} is a prime number.")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
