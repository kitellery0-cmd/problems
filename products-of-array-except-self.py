class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = postfix = 1
        # prefix products
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        # postfix products
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

