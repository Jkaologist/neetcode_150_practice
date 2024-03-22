# brute force solution
def two_sum(nums, target):
    for i in range(0, len(nums)):
        diff = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == diff:
                return [i, j]
    return False


# use extra space
def two_sum(nums, target):
    num_dict = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in num_dict:
            return [num_dict[diff], i]
        num_dict[nums[i]] = i
    return False


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([3, 4], 6))
