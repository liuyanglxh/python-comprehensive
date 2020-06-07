# encoding:utf-8

class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return self.rob_sub(nums, 0)

	def rob_sub(self, nums, index):
		# 边界
		if index >= len(nums):
			return 0
		if index == len(nums) - 1:
			return nums[index]
		if index == len(nums) - 2:
			return max(nums[index], nums[index + 1])
		# 递归
		# 第一种情况，偷index
		rob_index = nums[index] + self.rob_sub(nums, index + 2)
		rob_after_index = nums[index + 1] + self.rob_sub(nums, index + 3)
		return max(rob_index, rob_after_index)


lst = [1, 2, 3, 1]
print Solution().rob(lst)
lst = [2, 7, 9, 3, 1]
print Solution().rob(lst)
