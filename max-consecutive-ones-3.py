class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = zeroes = max_ones = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1

            while (zeroes > k):
                if nums[l] == 0:
                    zeroes -= 1
                l += 1

            max_ones = max(max_ones, (r - l + 1))
        
        return max_ones
