# Definition for singly-linked list.
class _ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: _ListNode, l2: _ListNode) -> _ListNode:
        node = _ListNode(0)
        head = node
        node.val += l1.val
        node.val += l2.val
        if node.val >= 10:
            node.val -= 10
            node.next = _ListNode(1)
        l1 = l1.next
        l2 = l2.next

        while l1 is not None or l2 is not None:
            if node.next is None:
                node.next = _ListNode(0)
            node = node.next
            if l1 is not None:
                node.val += l1.val
                l1 = l1.next
            if l2 is not None:
                node.val += l2.val
                l2 = l2.next
            if node.val >= 10:
                node.val -= 10
                node.next = _ListNode(1)

        return head


def print_node(node: _ListNode, msg=""):
    print(msg, end=" ")
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()


list1 = [2, 4, 3]
list2 = [5, 6, 4]
l1 = _ListNode(list1[0])
h1 = l1
for index in range(1, len(list1)):
    l1.next = _ListNode(list1[index])
    l1 = l1.next
print_node(h1, "h1")

l2 = _ListNode(list2[0])
h2 = l2
for index in range(1, len(list2)):
    l2.next = _ListNode(list2[index])
    l2 = l2.next
print_node(h2, "h2")

head = Solution().addTwoNumbers(l1=h1, l2=h2)
print_node(head, "head")
