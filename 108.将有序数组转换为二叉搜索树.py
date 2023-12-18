# @before-stub-for-debug-begin
from python3problem108 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 给定索引构建树节点
        def helper(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            # 计算索引的中间位置
            mid = (left + right) // 2
            node = TreeNode(val=nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node
        return helper(0, len(nums) - 1)
# @lc code=end

