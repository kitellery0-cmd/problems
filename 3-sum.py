class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            val = nums[i]
            if val > 0:
                break

            if (i > 0 and val == nums[i - 1]):
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r: # 2 sum 2 (2 ptrs)
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # skip dupes
                        l += 1

        return res

