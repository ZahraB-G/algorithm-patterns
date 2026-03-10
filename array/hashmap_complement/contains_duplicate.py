# Contains Duplicate 
# Given an integer array nums, return true if any value appears at least twice.
# Return false if all elements are unique.
# Example
# nums = [1,2,3,1]
# Output
# true

def contains_duplicate(nums):
  hash_table = {}
  i = 0
  for num in nums:
    if num in hash_table:
      return True
    else:
      hash_table[num] = True
      i += 1
  return False

print(contains_duplicate([1,2,3,4,4,3]))