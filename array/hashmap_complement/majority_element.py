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
