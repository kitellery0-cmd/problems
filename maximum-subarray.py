# the key realisation here is that a negative sum is always bad as:
# negative + negative subtracts, and negative + positive will always be worse
# than 0 + positive.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sub = max(max_sub, cur_sum)
        return max_sub
