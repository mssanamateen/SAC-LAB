try:
    n = int(input("Enter a number: "))
    print("Square:", n*n)
except ValueError:
    print(" Please enter a valid number!")
else:
    print("No error occurred!")
finally:
    print("This block always runs.")
