# You’re given an integer array nums and an integer target. You must find two different indices i and j such that: nums[i] + nums[j] == target
# You cannot reuse the same element twice (i != j)
# There is exactly one solution
# Return the two indices in any order
# Quick self-test cases
# two_sum([2,7,11,15], 9) -> [0,1]
# two_sum([3,2,4], 6) -> [1,2]
# two_sum([3,3], 6) -> [0,1]

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[num] = i

    return None

