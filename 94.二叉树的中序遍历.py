# @before-stub-for-debug-begin
from python3problem94 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        cur = root
        while len(stack) > 0 or cur:
            while cur:
                # 入栈左移
                stack.append(cur)
                cur = cur.left
            # 出栈
            cur = stack.pop()
            # 右移前存入结果
            result.append(cur.val)
            # 右移
            cur = cur.right
        return result
# @lc code=end

