class Solution:
    def fib(self, N: int) -> int:
        if N == 1 or N == 0:
            return N
        i1 = 0
        i2 = 1
        result = 0

        for x in range(2, N+1):
            result = i1 + i2
            i1 = i2
            i2 = result

        return result


print(Solution().fib(0))
print(Solution().fib(1))
print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))
print(Solution().fib(5))
print(Solution().fib(6))

