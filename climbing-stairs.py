class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1] * (n + 1)

        for i in range(n - 2, -1, -1):
            stairs[i] = stairs[i + 1] + stairs[i + 2]

        return stairs[0]
