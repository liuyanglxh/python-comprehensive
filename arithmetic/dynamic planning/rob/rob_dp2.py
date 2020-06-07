# encoding:utf-8

class Solution(object):
	def rob(self, nums):
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
