class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        l = 0
        r = len(nums) - 1

        while l <= r:
            swap = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[swap], nums[i] = nums[i], nums[swap]
                    swap += 1
            nums[swap], nums[r] = nums[r], nums[swap]
            if swap == target:
                return nums[swap]
            if swap > target:
                r = swap - 1
            else:
                l = swap + 1

        return -1
                



