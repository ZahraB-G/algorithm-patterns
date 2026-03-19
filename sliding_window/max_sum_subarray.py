# Maximum Sum Subarray of Size K
# Problem: Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.
# Example
# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# Output: 9
def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2],3))
