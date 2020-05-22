class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0 or n == 2:
            return n
        i1 = 0
        i2 = 1
        result = 0

        for x in range(1, n + 1):
            result = i1 + i2
            i1 = i2
            i2 = result

        return result
