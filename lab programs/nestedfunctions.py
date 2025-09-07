test_variable = 5  # Global variable

def outer_function():
    test_variable = 60  # Local to outer_function

    def inner_function():
        test_variable = 100  # Local to inner_function
        print(f"Local variable value of {test_variable} having local scope to inner function is displayed")

    inner_function()
    print(f"Local variable value of {test_variable} having local scope to outer function is displayed ")

outer_function()
print(f"Global variable value of {test_variable} is displayed ")
