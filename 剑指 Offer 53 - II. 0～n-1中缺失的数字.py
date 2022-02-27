class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = list(range(len(nums) + 1))
        for i in range(len(nums)):
            res.remove(nums[i])
        return res[0]
