def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[i - (k - 1)]
    
    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum subarray:", max_sum_subarray(arr, k))