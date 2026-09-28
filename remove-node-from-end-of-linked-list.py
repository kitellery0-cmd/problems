class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = dummy = ListNode(next=head)
        for _ in range(n + 1):
            r = r.next
        while r:
            l, r = l.next, r.next

        l.next = l.next.next
        return dummy.next
