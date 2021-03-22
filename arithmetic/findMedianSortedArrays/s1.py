from typing import List


class Solution:
	'''
	把2个数组合并后取中位数
	'''

	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		merge = []
		total_len = len(nums1) + len(nums2)
		left = int(total_len / 2) if total_len % 2 == 1 else int(total_len / 2) - 1
		right = int(total_len / 2)
		# 特殊情况
		if len(nums1) == 0: return (nums2[left] + nums2[right]) / 2
		if len(nums2) == 0: return (nums1[left] + nums1[right]) / 2
		i1, i2 = 0, 0
		while len(merge) <= right:
			if i1 < len(nums1) and i2 < len(nums2):
				e1, e2 = nums1[i1], nums2[i2]
				if e1 == e2:
					merge.append(e1)
					merge.append(e2)
					i1 += 1
					i2 += 1
				elif e1 < e2:
					merge.append(e1)
					i1 += 1
				else:
					merge.append(e2)
					i2 += 1
			elif i1 < len(nums1):
				merge.append(nums1[i1])
				i1 += 1
			else:
				merge.append(nums2[i2])
				i2 += 1

		return (merge[left] + merge[right]) / 2


if __name__ == '__main__':
	nums1 = [1, 2, 3, 4]
	nums2 = [1, 2]
	print(Solution().findMedianSortedArrays(nums1, nums2))
