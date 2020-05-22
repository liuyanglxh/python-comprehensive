from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # p1、p2分别表示爬到第n、n+1个台阶的总消耗
        p1, p2 = 0, 0
        # x代表p2爬到的楼层数
        for x in range(1, len(cost)):
            p3 = min(p1 + cost[x - 1], p2 + cost[x])
            p1, p2 = p2, p3
        # 当p2达到len(cost)-1位置时，p1还差一梯到达，因此p1还需要再爬一次才可以，故最后返回结果是 min(p1 + cost[len(cost) - 1], p2)
        return min(p1 + cost[len(cost) - 1], p2)


cost: List[int] = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(Solution().minCostClimbingStairs(cost))
