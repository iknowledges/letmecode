## 题目

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。

**示例**：

- 输入：nums = [2,7,11,15], target = 9
- 输出：[0,1]

## 题解

1. 遍历数组 nums，判断映射表中是否存在 (target-当前值) 的 key。如果没有，就把{当前值：下标}以存入映射表；
2. 如果有，就返回两个下标。

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = dict()
    for i, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], i]
        else:
            d[num] = i
    return []
```
