# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        head = self
        while head:
            result.append(head.val)
            head = head.next
        return str(result)
