"""1. 两数之和"""

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
"""
import copy

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            nums_copy = copy.deepcopy(nums)
            nums_copy.remove(nums[i])
            # 如果有
            if target - nums[i] in nums_copy:
                if target == 2*nums[i]:
                    return(nums.index(nums[i]), nums_copy.index(nums[i]) + 1)
                else:
                    return(nums.index(nums[i]), nums.index(target - nums[i]))
