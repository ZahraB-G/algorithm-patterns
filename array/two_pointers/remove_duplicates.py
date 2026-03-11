# Remove Duplicates from Sorted Array
# Given a sorted array nums, remove duplicates in-place so that each element appears only once.
# Return the number of unique elements.
# Example: nums = [1,1,2]
# Output: 2
def remove_duplicates(nums):

    slow = 0

    for fast in range(1, len(nums)):

        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1