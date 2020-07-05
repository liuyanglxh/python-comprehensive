# encoding:utf-8

"""
打家劫舍
"""
class Solution(object):
	def rob(self, nums):
		length = len(nums)
		if length == 0:
			return 0
		if length == 1 or length == 2 or length == 3:
			return max(nums)
		return max(nums[0] + self.rob_sub(nums[2:length - 1]), self.rob_sub(nums[1:]))

	def rob_sub(self, nums):
		length = len(nums)
		if length == 0:
			return 0
		if length == 1:
			return nums[0]
		if length == 2:
			return max(nums[0], nums[1])

		t0 = nums[0]
		t1 = max(nums[0], nums[1])
		for i in range(2, length):
			t2 = max(nums[i] + t0, t1)
			t0, t1 = t1, t2
		return t1
