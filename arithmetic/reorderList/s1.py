from arithmetic.reorderList.Node import ListNode


class Solution:
	def reorderList(self, head: ListNode) -> None:
		if not head: return
		nodes, head2 = [], head
		while head2:
			nodes.append(head2)
			head2 = head2.next
		l = len(nodes)
		for i in range(int(l / 2)):
			j = l - 1 - i
			if i == j - 1: break
			node, tail, pre_tail = nodes[i], nodes[j], nodes[j - 1]
			tail.next, node.next, pre_tail.next = node.next, tail, None


def createHead(lst: list) -> ListNode:
	head = ListNode(lst[0])
	sub = head
	for i in range(1, len(lst)):
		sub.next = ListNode(lst[i])
		sub = sub.next
	return head


def parseHead(head: ListNode):
	s = ""
	while head is not None:
		s += str(head.val)
		if head.next: s += "->"
		head = head.next
	return s


s = Solution()
head = createHead([1, 2, 3,4,5])
s.reorderList(head)
print(parseHead(head))
