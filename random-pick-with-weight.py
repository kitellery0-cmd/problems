class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        l = 0
        r = len(self.prefix_sums) - 1
        while l < r:
            m = (l + r) // 2
            if self.prefix_sums[m] < target:
                l = m + 1
            else:
                r = m
        return l
