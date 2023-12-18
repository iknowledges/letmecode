## 题目：
给定一个二叉树的根节点 root ，返回它的中序遍历 。

**示例**：

- 输入：root = [1,null,2,3]
- 输出：[1,3,2]

## 题解：

1. 初始化一个栈，将当前节点指向根节点。
2. 循环判断当前节点是否为空。如果不为空，入栈并左移。
3. 一直到节点为空，循环判断当前节点和栈是否为空。
4. 如果栈不为空，出栈并赋值给当前节点，节点值加入结果并将节点右移。
5. 然后继续循环判断当前节点是否为空。为空就出栈，不为空就重复步骤2入栈。
6. 最后当前节点和栈都为空循环结束，返回结果。

```cpp
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
vector<int> inorderTraversal(TreeNode* root) {
    vector<int> res;
    stack<TreeNode*> stk;
    while (root != nullptr || !stk.empty()) {
        while (root != nullptr) {
            stk.push(root);
            root = root->left;
        }
        root = stk.top();
        stk.pop();
        res.push_back(root->val);
        root = root->right;
    }
    return res;
}
};
```
