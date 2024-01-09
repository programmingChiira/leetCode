def twoSum(nums, target):
    dictionary = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in dictionary:
            return [dictionary[complement], i]
        else:
            dictionary[num] = i
    return None

nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)