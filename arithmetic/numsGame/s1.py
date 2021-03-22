from typing import List


class Solution:
	'''
	结果对1,000,000,007取余
	'''

	def numsGame(self, nums: List[int]) -> List[int]:
		s = set([x for x in range(len(nums))])
		min_total, min_result = 1000000007, [1000000007] * len(nums)
		for i in range(len(nums)):
			if i not in s: continue
			total, result = 0, [0] * len(nums)
			for j in range(len(nums)):
				if j == i: continue
				expect = nums[i] + (j - 1) + 1
				diff = expect - nums[j]
				if diff == 0:
					if j in s: s.remove(j)
					continue
				total += abs(diff)
				result[j] = abs(diff)
			if total < min_total:
				min_total = total
				min_result = result

		real_result = [0] * len(min_result)
		for i in range(len(real_result)):
			add = 0
			for j in range(i + 1): add += min_result[j]
			real_result[i] = add
		return real_result


if __name__ == '__main__':
	print(Solution().numsGame([3, 4, 5, 1, 6, 7]))
