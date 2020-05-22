# 整数反转
# https://leetcode-cn.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:

        positive = True
        if x < 0:
            positive = False
            x = -x

        strValue = str(x)
        x = int(strValue[::-1])
        if not positive:
            x = -x
        if x > (2 << 30) - 1 or x < - (2 << 30):
            x = 0

        return x
