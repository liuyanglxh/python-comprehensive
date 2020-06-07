# encoding:utf-8

class Solution(object):
	def rob(self, nums):
		# 边界
		length = len(nums)
		if length == 0:
			return 0
		if length == 1:
			return nums[0]
		if length == 2:
			return max(nums[0], nums[1])
		if length == 3:
			return max(nums[0] + nums[2], nums[1])
		if length == 4:
			return max(nums[0] + nums[2], nums[1] + nums[3], nums[0] + nums[3])

		tmp1 = nums[0]
		tmp2 = max(nums[0], nums[1])
		tmp3 = max(nums[0] + nums[2], nums[1])
		tmp4 = max(nums[0] + nums[2], nums[1] + nums[3], nums[0] + nums[3])
		for i in range(4, length):
			tmp = max(nums[i] + tmp3, nums[i - 1] + tmp2, nums[i - 2] + tmp1)
			tmp1, tmp2, tmp3, tmp4 = tmp2, tmp3, tmp4, tmp
		return tmp4


lst = [1, 2, 3, 1]
print Solution().rob(lst)
lst = [2, 7, 9, 3, 1]
print Solution().rob(lst)
