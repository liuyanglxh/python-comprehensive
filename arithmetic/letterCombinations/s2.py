from typing import List


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		mapping = {
			"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
			"6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"],
		}
		lst = []
		for digit in digits:
			letters = mapping[digit]
			if len(lst) == 0:
				lst.extend(letters)
			else:
				circle = len(lst)
				lst = lst * len(letters)
				index = 0
				for letter in letters:
					for i in range(circle):
						lst[index] += letter
						index += 1
		lst.sort()
		return lst


if __name__ == '__main__':
	print(Solution().letterCombinations("235"))
