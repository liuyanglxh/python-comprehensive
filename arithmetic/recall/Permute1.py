from typing import List

"""
https://leetcode-cn.com/problems/permutations/
"""


class Solution:

    def __init__(self):
        self.cache: dict[str: List[int]] = {}

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 or len(nums) == 0:
            return [nums[:]]

        result: List[List[int]]

        # 避免重复计算的缓存
        sorted(nums)
        key: str = nums.__str__()
        if key in self.cache:
            result = self.cache[key]
        else:
            result = []
            for index in range(0, len(nums)):
                num = nums[index]
                sub_nums = nums[:]
                sub_nums.remove(num)

                sub_list: List[List[int]] = self.permute(sub_nums)
                for sub_index, sub_result in enumerate(sub_list):
                    head: List[int] = [num] * (1 + len(sub_result))
                    for i, e in enumerate(sub_result):
                        head[i + 1] = e
                    result.append(head)

            self.cache[key] = result

        return result


print(Solution().permute([1, 2, 3, 4]))
