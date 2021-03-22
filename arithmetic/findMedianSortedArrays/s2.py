from typing import List


class Solution:
	'''
	把2个数组合并后取中位数，但是并不真去合并，而是仅找出中位的2个数字即可
	'''

	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

		middle, odd = int((len(nums1) + len(nums2)) / 2), (len(nums1) + len(nums2)) % 2 == 1
		left, right = middle if odd else middle - 1, middle
		act_left, act_right, left_val, right_val = -1, -1, 0, 0
		# 模拟合并
		i1, i2 = 0, 0
		while act_left != left or act_right != right:
			i1, i2, val = self.__findOne(nums1, nums2, i1, i2)
			if act_left < left:
				act_left, left_val = act_left + 1, val
			if act_right < right:
				act_right, right_val = act_right + 1, val

		return (left_val + right_val) / 2

	def __findOne(self, nums1: List[int], nums2: List[int], i1: int, i2: int):
		if i1 >= len(nums1):
			e, i2 = nums2[i2], i2 + 1
		elif i2 >= len(nums2):
			e, i1 = nums1[i1], i1 + 1
		elif nums1[i1] <= nums2[i2]:
			e, i1 = nums1[i1], i1 + 1
		else:
			e, i2 = nums2[i2], i2 + 1
		return i1, i2, e


if __name__ == '__main__':
	nums1 = [1, 2, 3, 4]
	nums2 = [2, 3, 2, 4, 6, 3, 1, 3, 6, 3, 2, 8]
	print(Solution().findMedianSortedArrays(nums1, nums2))
	from arithmetic.findMedianSortedArrays import s1

	print(s1.Solution().findMedianSortedArrays(nums1, nums2))
