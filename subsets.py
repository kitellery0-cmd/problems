class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):  # end of branch
                res.append(subset.copy())
                return
            subset.append(nums[i]) # include branch
            dfs(i + 1)
            subset.pop()        # exclude branch
            dfs(i + 1)

        dfs(0)
        return res
