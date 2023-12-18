#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        cur = root
        prev = None
        while len(stack) > 0 or cur:
            while cur:
                # 入栈左移
                stack.append(cur)
                cur = cur.left
            # 出栈带条件右移
            cur = stack.pop()
            # 节点存入结果的条件：(1)没有右子树 (2)前一次访问的是右子树
            if not cur.right or cur.right == prev:
                result.append(cur.val)
                prev = cur
                # 置为空再次出栈
                cur = None
            else:
                # 有右子树重新入栈
                stack.append(cur)
                # 右移
                cur = cur.right
        return result
# @lc code=end

