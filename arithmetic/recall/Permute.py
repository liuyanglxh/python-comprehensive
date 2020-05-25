from typing import List

"""
https://leetcode-cn.com/problems/permutations/
"""


class Solution:

    def __init__(self):
        self.cache: dict[str: List[int]] = {}

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permute_sub(sorted(nums))

    def permute_sub(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 or len(nums) == 0:
            return [nums[:]]

        # 避免重复计算的缓存
        key: str = nums.__str__()
        if key in self.cache:
            return self.cache[key]

        total = 1
        for t in range(1, len(nums) + 1):
            total *= t

        result: List[List[int]] = [[]] * total
        result_index = 0
        for index in range(0, len(nums)):
            num = nums[index]
            sub_nums = nums[:]
            sub_nums.remove(num)

            sub_list: List[List[int]] = self.permute_sub(sub_nums)
            for sub_index, sub_result in enumerate(sub_list):
                head: List[int] = [num] * (1 + len(sub_result))
                for i, e in enumerate(sub_result):
                    head[i + 1] = e
                result[result_index] = head
                result_index += 1

        self.cache[key] = result

        return result


print(Solution().permute([4, 3, 2, 1]))
