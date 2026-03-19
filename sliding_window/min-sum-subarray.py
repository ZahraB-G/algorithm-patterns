# Minimum Sum Subarray of Size K
# Problem: Given an array nums and integer k, return the minimum sum of any contiguous subarray of size k.
# Example
# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# Output = 6

def fun(nums, k):
    window_sum = sum(nums[:k])
    min_sum = window_sum
    for i in range(k,len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        min_sum = min(min_sum,window_sum)
    
    return min_sum

print(fun([2, 1, 5, 1, 3, 2], 3))
