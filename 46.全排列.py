# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(first:int = 0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return res
# @lc code=end

