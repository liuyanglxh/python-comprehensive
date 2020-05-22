from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 特殊情况，数组长度小于3，首元素非负，尾元素非正，都无法满足条件
        if len(nums) < 3 or nums[0] > 0 or nums[len(nums) - 1] < 0:
            return result
        # 1.排序
        nums.sort()
        # 2.选一个索引i，从0开始往后循环，直到遇到正数就退出循环
        i = 0
        while nums[i] < 0:
            # i位置数字和之前数据重复了，直接跳过
            if i > 0 and nums[i - 1] == nums[i]:
                i = i + 1
                continue

            left = i + 1
            right = len(nums) - 1

            i = i + 1

        return result
