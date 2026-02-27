# Given an integer array nums and an integer target,
# return the number of unique pairs whose sum equals target.
def count_pairs(nums, target):
    hashmap = {}
    count = 0
    for i, num in enumerate(nums):
        complement = target - num 
        if complement in hashmap:
            count += hashmap.get(num,0)+1
        hashmap[complement] = num
    return count

print(count_pairs([1, 5, 7, -1, 5],6))