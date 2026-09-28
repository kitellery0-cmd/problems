class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)] # group nums by frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        res = [] # pop k nums
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                k -= 1
                if k == 0:
                    return res
