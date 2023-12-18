def twoSum(nums, target):
    d = dict()
    for i, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], i]
        else:
            d[num] = i
    return []


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print([0, 1]) 
    print(twoSum(nums, target))
