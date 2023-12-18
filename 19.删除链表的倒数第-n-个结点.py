# @before-stub-for-debug-begin
from python3problem19 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        # fast最后指向None，所以slow开始指向一个哑节点
        dummy = ListNode(0, head)
        slow = dummy
        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
# @lc code=end

