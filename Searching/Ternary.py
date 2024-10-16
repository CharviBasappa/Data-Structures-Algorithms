def ternary_search(arr, left, right, target):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10
print("Element found at index (Ternary Search):", ternary_search(arr, 0, len(arr) - 1, target))
