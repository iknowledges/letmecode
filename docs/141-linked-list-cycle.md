## 题目：
给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。

**示例**：

- 输入：head = [3,2,0,-4], pos = 1
- 输出：true
- 解释：链表中有一个环，其尾部连接到第二个节点。

## 题解：

1. 初始时，定义两个指针，慢指针在位置head，而快指针在位置head.next。
2. 循环判断两个指针是否相同，如果不相同，慢指针每次移动一格，快指纹每次移动两格。（注意判断fast是否走到链表结尾）
3. 如果快慢指针相同，说明有环，返回true。

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) {
            return false;
        }
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (slow != fast && fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow == fast;
    }
};
```
