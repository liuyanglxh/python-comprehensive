from typing import List

'''
盛水最多容器
https://leetcode-cn.com/problems/container-with-most-water/
'''


class Solution:
	def maxArea(self, height: List[int]) -> int:
		max_area, left, right = 0, 0, len(height) - 1

		while left < right:
			max_area = max(max_area, (right - left) * min(height[left], height[right]))

			if height[left] == height[right]:
				left, right = left + 1, right - 1
			else:
				left, right = (left + 1, right) if height[left] < height[right] else (left, right - 1)

		return max_area


