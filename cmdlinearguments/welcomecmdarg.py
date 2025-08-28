import sys

if len(sys.argv) < 2:
    print("Please provide your name as an argument!")
else:
    fname = sys.argv[1]
    lname=sys.argv[2]
    print(f"Hello, {fname} {lname}! Welcome to the world of command-line arguments!")