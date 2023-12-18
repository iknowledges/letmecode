## 题目：

给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

**示例**：

- 输入：root = [3,9,20,null,null,15,7]
- 输出：2

## 题解：

递归过程：

1. 当前节点 root 为空时，树的高度为0。
2. 当前节点 root 的左子树和右子树都为空时，树的高度为1。
3. 否则需要分别计算左右子树的最小深度，返回最小深度+1。

注意：辅助变量ans应初始化为整型的最大值，以防止一边为空、另一边有子树时取最小值，错误地返回辅助变量ans，因为我们需要的是左子树和右子树中的最小值。

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root == nullptr) {
            return 0;
        } else if(root->left == nullptr && root->right == nullptr) {
            return 1;
        }
        int ans = INT_MAX;
        if(root->left != nullptr){
            int l = minDepth(root->left);
            ans = min(ans, l);
        }
        if(root->right != nullptr) {
            int r = minDepth(root->right);
            ans = min(ans, r);
        }
        return ans + 1;
    }
};
```
