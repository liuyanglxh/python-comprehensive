from typing import List


class MaxGoldLinear:
    # g -- 金矿总数 w -- 工人总数 gold -- 每座金矿的产量  worker -- 每座金矿消耗的工人数
    def __init__(self, w: int, gold: List[int], worker: List[int]):
        self.w = w
        self.gold = gold
        self.worker = worker

    def solution(self) -> int:
        pre: List[int] = [0] * (self.w + 1)  # 位置0不使用
        curr: List[int] = [0] * (self.w + 1)  # 位置0不使用
        # 准备第一行数据：max_worker表示可用的最大工人数
        for available_worker in range(1, self.w + 1):
            if available_worker < self.worker[0]:
                pre[available_worker] = 0
            else:
                pre[available_worker] = self.gold[0]

        # 外层循环，从第2个金矿开始
        for gold_index in range(1, len(self.gold)):
            # 当前矿需要的工人数
            worker_needed = self.worker[gold_index]
            # 当前矿的产量
            gold_volume = self.gold[gold_index]
            # 内层循环：可用工人数从1个开始
            for available_worker in range(1, self.w + 1):
                """
                如果给的工人不够挖当前矿，那这个位置的值就是上一个数组相同位置的值
                """
                if available_worker < worker_needed:
                    curr[available_worker] = pre[available_worker]
                else:
                    dig = pre[available_worker - worker_needed] + gold_volume
                    no_dig = pre[available_worker]
                    curr[available_worker] = max(dig, no_dig)
            pre = curr
            curr = [0] * (self.w + 1)

        return pre[len(pre) - 1]


class MaxGoldRecursion:
    # g -- 金矿总数 w -- 工人总数 gold -- 每座金矿的产量  worker -- 每座金矿消耗的工人数
    def __init__(self, total_worker: int, gold_volumes: List[int], worker_needs: List[int]):
        self.total_worker = total_worker
        self.gold_volumes = gold_volumes
        self.worker_needs = worker_needs

    def solution(self) -> int:
        return self.getMaxGold(self.total_worker, len(self.gold_volumes) - 1)

    def getMaxGold(self, available_worker: int, gold_index: int) -> int:
        # 边界
        # 挖到最后一个矿了
        if gold_index == 0:
            if available_worker >= self.worker_needs[0]:
                return self.gold_volumes[0]
            else:
                return 0

        # 递推关系
        dig: int
        if available_worker >= self.worker_needs[gold_index]:
            dig = self.gold_volumes[gold_index] + self.getMaxGold(available_worker - self.worker_needs[gold_index],
                                                                  gold_index - 1)
        else:
            dig = self.getMaxGold(available_worker, gold_index - 1)

        no_dig: int = self.getMaxGold(available_worker, gold_index - 1)
        return max(dig, no_dig)


w = 10
gold = [500, 400, 350, 300, 200]
worker = [5, 5, 3, 4, 3]
print(MaxGoldRecursion(total_worker=w, gold_volumes=gold, worker_needs=worker).solution())
print(MaxGoldLinear(w=w, gold=gold, worker=worker).solution())

# m: MaxGoldRecursion = MaxGoldRecursion(w=w, gold=gold, worker=worker)

# for left_worker in range(1, 11):
#     print(m.getMaxGold(left_worker, 3))
