# Function definition
def square(num):   # 'num' here is a local variable
    print(f"Inside function, square of {num} is {num * num}")

# Main function
def main():
    num = 5   # 'num' here is from main (global/calling variable)
    square(num)   # Passing num as argument
    print(f"Back in main num is {num}")

# Entry point
if __name__ == "__main__":
    main()
