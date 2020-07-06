from typing import List

'''
盛水最多的容器
https://leetcode-cn.com/problems/container-with-most-water/
'''


class Solution:
	def maxArea(self, height: List[int]) -> int:

		max_area: int = 0

		# 建立字典：存下每个值对应的最小和最大位置
		d: dict[int:List[int]] = {}
		for index, value in enumerate(height):
			if value in d:
				d[value][1] = index
			else:
				d[value] = [index] * 2

		# 存下所有存活的index（每个值的最大、最小位置）
		s: set = set()
		for indices in d.values():
			for index in indices:
				s.add(index)

		# 把所有值取出来并排序
		values: List[int] = list(d.keys())
		values = sorted(values)

		# 从最小的值开始
		for value in values:
			# 这个值对应的最大位置和最小位置
			indices: List[int] = d[value]
			area = max(max(s) - indices[0], indices[1] - min(s)) * value
			max_area = max(area, max_area)
			s.remove(indices[0])
			if indices[1] in s:
				s.remove(indices[1])

		return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
