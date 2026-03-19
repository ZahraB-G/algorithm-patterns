# Find Average of Subarrays of Size K
# Problem: Given an array nums and an integer k, return an array of the average of all contiguous subarrays of size k.
# Example
# nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
# k = 5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

def fun(nums, k):
    window_sum = sum(nums[:k])
    result = [window_sum / k]

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        result.append(window_sum / k)

    return result

print(fun([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
        