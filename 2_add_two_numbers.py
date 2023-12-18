from base import ListNode


def addTwoNumbers(l1, l2):
    carry = 0
    dump = ListNode()
    cur = dump
    while (l1 or l2):
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        val = v1 + v2 + carry
        carry = 1 if val > 9 else 0
        cur.next = ListNode(val = val % 10)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        cur.next = ListNode(val = carry)
    return dump.next


if __name__ == '__main__':
    # [2, 4, 3]
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    # [5, 6, 4]
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    # 342 + 465 = 807
    print([7, 0, 8])
    print(addTwoNumbers(l1, l2))