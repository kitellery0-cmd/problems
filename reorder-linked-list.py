class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        prev = slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        second = prev
        while second:
            tmp1, tmp2 = head.next, second.next
            head.next = second
            second.next = tmp1
            head, second = tmp1, tmp2
