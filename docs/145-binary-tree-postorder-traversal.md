## 题目：
给你一棵二叉树的根节点 root ，返回其节点值的后序遍历。

**示例**：

- 输入：root = [1,null,2,3]
- 输出：[3,2,1]

## 题解：

1. 初始化一个栈，两个节点指针：当前节点root指向根节点，前驱节点prev设为空。
2. 循环判断当前节点是否为空。如果不为空，入栈并连续左移。
3. 一直到节点为空，循环判断当前节点和栈是否为空。
4. 如果栈不为空，出栈并赋值给当前节点。再判断当前节点的右子树是否为空。
5. 如果当前节点的右子树为空，则将节点值加入结果，prev记录当前节点root地址，当前节点root置为空。
6. 如果当前节点的右子树不为空，再次入栈，节点右移。
7. 然后继续循环判断节点是否为空。
8. 出栈后如果当前节点的右子树等于prev，重复步骤5，将节点值加入结果，prev记录当前节点root地址，当前节点root置为空。
9. 最后如果当前节点和栈都为空则结束循环，返回结果。

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
vector<int> postorderTraversal(TreeNode* root) {
    vector<int> res;
    stack<TreeNode*> stk;
    TreeNode* prev = nullptr;
    while (root != nullptr || !stk.empty()) {
        while (root != nullptr) {
            stk.push(root);
            root = root->left;
        }
        root = stk.top();
        stk.pop();
        if (root->right == nullptr || root->right == prev) {
            res.push_back(root->val);
            prev = root;
            root = nullptr;    
        } else {
            stk.push(root);
            root = root->right;
        }
    }
    return res;
}
};
```
