n = int(input("Enter the limit: "))
even = odd = 0
for i in range(1,n):
    if i % 2 == 0:
        even += i
    else:
        odd += i
else:  # this runs only if loop finishes normally
    print(f"Sum of even numbers are {even}, odd numbers are {odd}")
