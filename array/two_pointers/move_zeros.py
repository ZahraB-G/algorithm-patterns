# Move Zeroes
# Given an array nums, move all 0's to the end while maintaining the relative order of the non-zero elements.
# Example: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
def fun(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow +=1
    for slow in range(slow,len(nums)):
        nums[slow] = 0
    return nums


