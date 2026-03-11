# Intersection of Two Arrays 
# Given two arrays nums1 and nums2, return their intersection.
# Each element in the result must be unique.
# Example
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# Output
# [2]
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()
    for num in nums2:
        if num in set1:
            result.add(num)
    return result
print(intersection([1,2,2,1],[2,2]))