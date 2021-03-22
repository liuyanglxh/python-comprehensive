from typing import List


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		mapping = {
			"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
			"6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"],
		}
		total_len = 0
		for digit in digits: total_len *= len(mapping[digit])
		lst = [[] * len(digits)] * total_len
		for digit in digits:
			letters, index = mapping[digit], 0
			for letter in letters:
				for x in range(int(total_len / len(letters))):
					lst[index].append(letter)
					index += 1
		return ["".join(a) for a in lst]


if __name__ == '__main__':
	print(Solution().letterCombinations("23"))
