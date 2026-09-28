class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0

        while l1 or l2 or carry:
            summ = carry
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next

            carry, val = divmod(summ, 10)
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next
