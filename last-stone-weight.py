class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            biggest = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if biggest > second:
                heapq.heappush_max(stones, (biggest - second))

        if not stones:
            return 0
        return stones[0]
