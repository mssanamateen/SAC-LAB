def is_digit_sum_even(n):
    """Check if sum of digits of n is even."""
    digit_sum = sum(int(d) for d in str(n))
    return digit_sum % 2 == 0

def display_even_digit_sum_numbers(start, end):
    """Display numbers with even digit sum between start and end."""
    for num in range(start, end + 1):
        if is_digit_sum_even(num):
            print(num, end=" ")

display_even_digit_sum_numbers(100, 200)
