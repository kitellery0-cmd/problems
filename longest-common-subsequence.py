# this is just like house robber except we need to connect the last and first
# house. this means that we can run two slices and run it on them. one with the
# loop and one without, returning the largest.

# to find the max we will run a search that checks the maximum of the current
# and house 2 back vs the last max total
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # call the other one
        return max(self.rob_segment(nums), self.rob_segment(nums[1 : ] + nums[0]))

    def rob_segment(nums) -> int:
        if len(nums) == 1:
            return nums[0]
        max_loot = [0] * len(nums)
        max_loot[0] = nums[0]
        max_loot[1] = max(nums[0], nums[1])
        max_sum = 0

        for i in range(2, len(nums)):
            max_loot[i] = max(max_loot[i - 1], nums[i] + max_loot[i - 2])

        return max(max_loot)
