from typing import List
import functools

from arithmetic.listnode import ListNode


class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		lists = [ele for ele in lists if ele]

		# 倒叙排
		def cmp(a: ListNode, b: ListNode):
			return b.val - a.val

		sorted(lists, key=functools.cmp_to_key(cmp))
		head, tail = None, None
		while len(lists) > 0:
			index = len(lists) - 1
			last_ele = lists[index]
			if not head:
				head, tail = last_ele, last_ele
			else:
				tail.next, tail = last_ele, last_ele
			if not last_ele.next:
				del lists[index]
			elif index != 0:
				lists[index] = last_ele.next
				pre, cur = lists[index - 1], lists[index]
				while index > 0 and pre.val < cur.val: lists[index - 1], lists[index] = cur, pre
		return head
