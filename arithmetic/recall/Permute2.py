from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        first含义：表示要在这个位置上填入1个数字
        :param nums:
        :return:
        """

        def recall(first: int):
            if first == len(nums) - 1:
                result.append(nums[:])

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                recall(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        result = []
        recall(0)

        return result


print(Solution().permute([1, 2, 3]))
