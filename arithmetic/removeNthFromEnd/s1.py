from arithmetic.listnode import ListNode


class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		if not head or not head.next: return None
		length, cur, lst = 0, head, []
		while cur:
			lst.append(cur)
			cur = cur.next
		if len(lst) - n == 0: return head.next
		pre, cur = lst[len(lst) - n - 1], lst[len(lst) - n]
		pre.next = cur.next
		return head
