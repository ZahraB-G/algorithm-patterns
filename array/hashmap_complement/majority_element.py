# Majority Element
# Given an array nums, return the element that appears more than ⌊n/2⌋ times.
# You may assume that the majority element always exists.
# Example: nums = [3,2,3] Output: 3
import math

def majority_element(nums):
    hash_map = {}
    majority = len(nums) // 2

    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

        if hash_map[num] > majority:
            return num
