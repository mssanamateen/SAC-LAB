def is_armstrong(num):
    """Check if a 3-digit number is Armstrong"""
    original = num
    cube_sum = 0
    
    while num > 0:
        digit = num % 10        # get last digit
        cube_sum += digit ** 3  # add cube of digit
        num //= 10              # remove last digit
    
    return cube_sum == original

num = int(input("Enter a 3-digit number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
