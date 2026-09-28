class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        cur = 0
        while slow != cur:
            slow = nums[slow]
            cur = nums[cur]
        return slow
