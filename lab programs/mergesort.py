# Merge function to combine two sorted halves
def merge(left, right):
    result = []
    i = j = 0
   
    # Compare elements of left and right lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Merge Sort function
def merge_sort(arr):
    if len(arr) <= 1:  # Base case: a single element is already sorted
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

# Example usage
arr = [9, 7, 8, 3, 2, 1]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
