# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	cache = {}

	def rob(self, root: TreeNode) -> int:
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return root.val

		if root in self.cache:
			return self.cache[root]

		# 要偷当前
		rob_cur: int = root.val
		# 右边
		right: TreeNode = root.right
		if right is not None:
			rob_cur = rob_cur + self.rob(right.left) + self.rob(right.right)
		left: TreeNode = root.left
		# 左边
		if left is not None:
			rob_cur = rob_cur + self.rob(left.left) + self.rob(left.right)

		# 不偷当前
		no_rob_cur: int = self.rob(left) + self.rob(right)

		result: int = max(no_rob_cur, rob_cur)
		self.cache[root] = result
		return result
