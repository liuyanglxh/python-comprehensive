from typing import List

from arithmetic.listnode import ListNode


class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		queue = PriorityQueue(lists)
		head, tail = None, None
		while True:
			ele = queue.poll()
			if not ele: break
			if not head:
				head, tail = ele, ele
			else:
				tail.next, tail = ele, ele
		return head


# 优先队列
class PriorityQueue:
	def __init__(self, lists: List[ListNode]):
		self.nodes = [] * len(lists)
		self.__init_queue(lists)

	def __init_queue(self, lists: List[ListNode]):
		'''
		把队列初始化成一个优先队列
		'''
		for node in lists:
			if node is None: continue
			self.nodes.append(node)
			cur_index = len(self.nodes) - 1
			# 把新元素上滤到一个合适的位置
			while cur_index > 0:
				up_index = int(cur_index - 1 / 2)
				up, cur = self.nodes[up_index], self.nodes[cur_index]
				if up.val <= cur.val: break
				self.__swap(up_index, cur_index)
				cur_index = up_index

	def poll(self) -> ListNode:
		'''
		弹出顶部元素
		'''
		if len(self.nodes) == 0: return None
		ele = self.nodes[0]
		self.nodes[0] = ele.next
		# 顶部元素需要找到一个合适的位置，或者被删除
		if not self.nodes[0]:
			self.__del_top()
		else:
			self.__down(0)

		return ele

	def __down(self, index: int):
		'''
		元素下滤
		'''
		nodes = self.nodes
		# 处理脚标越界的问题
		left_index, right_index = index * 2 + 1, index * 2 + 2
		if index >= len(nodes) or left_index >= len(nodes): return
		# 从左右节点中找出需要下滤的位置
		to_compare = left_index if right_index >= len(nodes) or nodes[left_index].val < nodes[
			right_index].val else right_index
		# 顶部元素更小，则停止
		if nodes[index].val <= nodes[to_compare].val: return
		# 顶部元素更大，交换，然后继续下滤
		self.__swap(index, to_compare)
		self.__down(to_compare)

	def __del_top(self):
		'''
		删除顶部位置：用最后一个元素替换顶部元素，然后将顶部元素下滤
		'''
		if len(self.nodes) == 1:
			del self.nodes[0]
			return
		last_node = self.nodes[len(self.nodes) - 1]
		del self.nodes[len(self.nodes) - 1]
		self.nodes[0] = last_node
		self.__down(0)

	def __swap(self, i: int, j: int):
		i_ele, j_ele = self.nodes[i], self.nodes[j]
		self.nodes[i], self.nodes[j] = j_ele, i_ele


if __name__ == '__main__':
	a = [1, 2, 3]
	del a[1]
	print(a)
