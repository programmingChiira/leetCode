def two_sum(nums, target):
        dictionary = {}
        for i, num in enumerate(nums, start=0):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], i]
            dictionary[num] = i
        return None

nums = [11, 2, 15, 7]
target = 9
result = two_sum(nums, target)
print(result)
