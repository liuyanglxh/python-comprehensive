# Definition for singly-linked list.
class _ListNode:
	def __init__(self, x):
		self.val = x
		self.next: _ListNode = None


class Solution:
	def reverseKGroup(self, head: _ListNode, k: int) -> _ListNode:
		a, b, c = self.get_sub_reverse(head, k)
		while c:
			x, y, z = self.get_sub_reverse(c, k)
			b.next, b, c = x, y, z
		return a

	def get_sub_reverse(self, head: _ListNode, k: int) -> (_ListNode, _ListNode, _ListNode):
		tail, k = head, k - 1
		while k and tail.next: k, tail = k - 1, tail.next
		next_head, tail.next = tail.next, None
		if k == 0:
			new_head, new_tail = self.reverse(head)
		else:
			new_head, new_tail = head, tail
		return new_head, new_tail, next_head

	def reverse(self, head: _ListNode) -> (_ListNode, _ListNode):
		if not head: return head
		t, a, b, c = head, None, head, head.next
		while c: b.next, a, b, c = a, b, c, c.next
		b.next = a
		return b, t


head: _ListNode = _ListNode(0)
tail: _ListNode = head
for i in range(1, 11):
	tail.next = _ListNode(i)
	tail = tail.next

a = Solution().reverseKGroup(head, 3)

while a:
	print(a.val)
	a = a.next
