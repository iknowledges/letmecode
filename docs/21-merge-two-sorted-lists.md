## 题目：

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例**：

- 输入：l1 = [1,2,4], l2 = [1,3,4]
- 输出：[1,1,2,3,4,4]

## 题解：

1. 初始化一个哨兵节点prevhead，值设为-1，用于返回合并后的链表，创建一个prev指针指向prevhead。然后开始循环遍历两个链表。
2. 比较L1和L2当前节点的值。
3. 如果L1<=L2，就把L1接到prev后面，同时将L1和prev后移一位。
4. 继续比较L1和L2当前节点的值。
5. 如果L1>L2，就把L2接到prev后面，同时将L2和prev后移一位。
6. 如果一个链表遍历完了，就把另一个非空链表接到prev后面，并返回prehead的next节点。

```cpp
/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     ListNode *next;
*     ListNode() : val(0), next(nullptr) {}
*     ListNode(int x) : val(x), next(nullptr) {}
*     ListNode(int x, ListNode *next) : val(x), next(next) {}
* };
*/
class Solution {
public:
ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode* prevhead = new ListNode(-1);
    ListNode* prev = prevhead;
    while(list1!=nullptr && list2!=nullptr){
        if(list1->val<list2->val){
            prev->next = list1;
            list1 = list1->next;
            prev = prev->next;
        }else{
            prev->next = list2;
            list2 = list2->next;
            prev = prev->next;
        }
    }
    if(list1!=nullptr){
        prev->next = list1;
    }
    if(list2!=nullptr){
        prev->next = list2;
    }
    return prevhead->next;
}
};
```
