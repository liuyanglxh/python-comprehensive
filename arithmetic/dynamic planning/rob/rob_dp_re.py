# encoding:utf-8

class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return self.rob_sub(nums, len(nums) - 1)

	def rob_sub(self, nums, n):
		if n < 0:
			return 0
		if n == 0:
			return nums[0]
		if n == 1:
			return max(nums[0], nums[1])
		if n == 2:
			return max(nums[0] + nums[2], nums[1])

		# 偷n
		rob_n = nums[n] + self.rob_sub(nums, n - 2)
		# 不偷n
		no_rob_n1 = nums[n - 1] + self.rob_sub(nums, n - 3)
		no_rob_n2 = nums[n - 2] + self.rob_sub(nums, n - 4)
		return max(rob_n, no_rob_n1, no_rob_n2)


lst = [1, 2, 3, 1]
print Solution().rob(lst)
lst = [2, 7, 9, 3, 1]
print Solution().rob(lst)
