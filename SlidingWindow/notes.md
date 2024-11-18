## Sliding Window

- Brute force approach to solve the problem is to use nested loops. This approach has a time complexity of O(n^2).
- Sliding window technique is used to solve the problem in O(n) time complexity.

- **Sliding Window** is a technique for finding subarrays or sublists in a list or array. It is used to solve problems that require finding the longest or shortest subarray or sublists that satisfy a certain condition.

- Keywords : **Fixed size, Dynamic size, Window, Subarray, Substring Longest, Shortest, Contiguous, Non-contiguous,maximum,minimum,k(window size)**

- **Fixed size** : The size of the window is fixed and does not change.
- **Dynamic size** : The size of the window is dynamic and changes according to the problem.

## Code implementation

- Window : [i, j] -> i is the start of the window and j is the end of the window
- Window size : j - i + 1

- Brute force
```python

def max_sum_subarray(arr, k):
    max_sum = 0
    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

- Sliding window
```python
def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum
```