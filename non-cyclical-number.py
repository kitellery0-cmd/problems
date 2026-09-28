class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            sum = 0
            while n:
                x = n % 10
                x **= 2
                sum += x
                n //= 10
            return sum

        slow = sos(n)
        fast = sos(slow)

        while slow != fast:
            slow = sos(slow)
            fast = sos(sos(fast))
        return True if fast == 1 else False
