# @before-stub-for-debug-begin
from python3problem66 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            # 逆向遍历找到第一个不是9的数
            if digits[i] != 9:
                digits[i] += 1
                # 后续所有元素都置为0
                j = i + 1
                while j < len(digits):
                    digits[j] = 0
                    j += 1
                return digits
            i -= 1
        # 所有元素都是9
        return [1] + [0] * len(digits)
# @lc code=end

