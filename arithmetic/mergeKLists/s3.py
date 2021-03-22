from typing import List

from arithmetic.listnode import ListNode


class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		length, first = len(lists), lists[0]
		for i in range(1, length): first = self.__merge(first, lists[i])
		return first

	def __merge(self, a: ListNode, b: ListNode) -> ListNode:
		a, b, head = self.__get(a, b)
		tail = head
		while tail:
			a, b, tail.next = self.__get(a, b)
			tail = tail.next

		return head

	def __get(self, a: ListNode, b: ListNode):
		if not a and not b: return a, b, None
		if not a: return a, b.next, b.next
		if not b: return a.next, b, a.next


