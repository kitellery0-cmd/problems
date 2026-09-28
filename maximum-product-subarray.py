class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min = cur_max = 1

        for num in nums:
            prod_min, prod_max = cur_min * num, cur_max * num
            cur_min = min(num, prod_min, prod_max)
            cur_max = max(num, prod_min, prod_max)
            res = max(res, cur_max)
        return res

# this works as subsets will only be created with 0's. Negative numbers are
# handled by keeping track of cur_min
