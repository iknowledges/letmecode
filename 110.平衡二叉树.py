#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 计算任意节点高度
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            # 计算左右子树的高度
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            # 先判断左右子树是否平衡，再判断以当前节点为根的树是否平衡
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight-rightHeight) > 1:
                # 如果不平衡则返回-1
                return -1
            else:
                # 如果平衡则返回当前树的高度
                return max(leftHeight, rightHeight) + 1

        return height(root) != -1
# @lc code=end

