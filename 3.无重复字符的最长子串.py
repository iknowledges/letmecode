# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        start, result = 0, 0
        for cur, char in enumerate(s):
            # 判断当前字符是否已经出现过
            if char in charDict:
                idx = charDict[char]
                # 当前字符已经出现过，而且索引大于等于start，就把start指针后移一位，如abca
                if idx == start:
                    start = idx + 1
            # 保存字符和索引映射
            charDict[char] = cur
            result = max(cur - start + 1, result)
        return result
# @lc code=end

