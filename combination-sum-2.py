class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i]) # include branch
            dfs(i + 1, total + candidates[i])
            cur.pop()           # exclude branch
            # skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res


# s = Solution()
# print(s.combinationSum2( [9,2,2,4,6,1,5], 8))
"""
res:
Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
] 
"""
