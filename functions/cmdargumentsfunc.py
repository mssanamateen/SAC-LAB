import sys
def greet(name):
    print(f"Hello {name}!")

if len(sys.argv)>1:
    greet(sys.argv[1])
else:
    print("please enter the command line arguments")
