#
# @lc app=leetcode.cn id=1382 lang=python3
#
# [1382] 将二叉搜索树变平衡
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorderSeq = list()

        # 中序遍历将二叉搜索树转化为有序序列
        def getInorder(node):
            if node.left:
                getInorder(node.left)
            inorderSeq.append(node.val)
            if node.right:
                getInorder(node.right)

        # 递归建树
        def build(l, r):
            mid = (l + r) // 2
            node = TreeNode(inorderSeq[mid])
            if l <= mid - 1:
                node.left = build(l, mid - 1)
            if mid + 1 <= r:
                node.right = build(mid + 1, r)
            return node

        getInorder(root)
        return build(0, len(inorderSeq) - 1)
# @lc code=end

