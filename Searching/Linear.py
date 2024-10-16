def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10
print("Element found at index (Linear Search):", linear_search(arr, target))
