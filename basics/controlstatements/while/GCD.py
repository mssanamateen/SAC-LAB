m = int(input("Enter first positive number: "))
n = int(input("Enter second positive number: "))

if m == 0 and n == 0:
    print("Invalid Input")
    exit()
if m == 0:
    print(f"GCD is {n}")
    exit()
if n == 0:
    print(f"GCD is {m}")
    exit()

while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m

print(f"GCD of two numbers is {m}")
