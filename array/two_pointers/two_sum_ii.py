# Two Sum II (Sorted Array) 
# Given a sorted array of integers numbers and a target value target, 
# find two numbers such that they add up to the target.
# Return their indices.
# Example
# numbers = [2,7,11,15]
# target = 9
# Output [0,1]
def fun(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        result = nums[left] + nums[right] 
        if result== target:
            return [left,right]
        elif result < target:
            left +=1
        else:
            right-=1

