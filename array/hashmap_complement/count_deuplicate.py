# You are given an integer array nums and an integer k. 
# Return True if there exist two distinct indices i and j such that:
# nums[i] == nums[j]
# abs(i - j) <= k
# Otherwise, return False.

def count_duplicate(nums,k):
    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap and i - hashmap[num]<=k:
            return True
        hashmap[num] = i
    return False