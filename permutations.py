class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:        # each number
            new_perms = []
            for p in perms:     # each permutation
                for i in range(len(p) + 1): # each idx pos
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
