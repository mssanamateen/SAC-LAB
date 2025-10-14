# Binary Search in Python

def binary_search(arr, target):
    low = 0                      # starting index
    high = len(arr) - 1          # ending index

    while low <= high:
        mid = (low + high) // 2  # find middle index

        if arr[mid] == target:
            return mid            # target found
        elif arr[mid] < target:
            low = mid + 1         # search in right half
        else:
            high = mid - 1        # search in left half

    return -1                     # target not found


arr = [0, 1, 2, 4, 9]   # list must be sorted
target = int(input("Enter the element to search: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
