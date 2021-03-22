class Solution:
	'''
	最长回文子串
	'''

	def longestPalindrome(self, s: str) -> str:
		if len(s) in (0, 1): return s
		maxLen, maxLeft, maxRight = 1, 0, 0
		for i in range(len(s)):
			double = s[i] == s[i - 1]
			single = i < len(s) - 1 and s[i - 1] == s[i + 1]

			def method_name(left, right, maxLeft, maxLen, maxRight, s):
				while left > 0 and right < len(s) - 1:
					if not s[left - 1] == s[right + 1]: break
					left, right = left - 1, right + 1
				if right - left + 1 > maxLen: maxLen, maxLeft, maxRight = right - left + 1, left, right
				return maxLeft, maxLen, maxRight

			if single: maxLeft, maxLen, maxRight = method_name(i, i, maxLeft, maxLen, maxRight, s)
			if double: maxLeft, maxLen, maxRight = method_name(i - 1, i, maxLeft, maxLen, maxRight, s)

		return s[maxLeft:maxRight + 1]


s = "ab"
print(Solution().longestPalindrome(s))
