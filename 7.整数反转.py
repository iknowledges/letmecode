# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31-1
        ans = 0
        while x != 0:
            # python负数整除向下取整，因此需要+1
            if ans < INT_MIN // 10 + 1 or ans > INT_MAX // 10:
                return 0
            remain = x % 10
            # python中取模运算-123%10=7，所以要减去10
            # 而x是10的负整数倍时不要特殊处理
            if x < 0 and remain != 0:
                remain -= 10
                x -= remain
            ans = ans * 10 + remain
            x //= 10
        return ans
# @lc code=end

