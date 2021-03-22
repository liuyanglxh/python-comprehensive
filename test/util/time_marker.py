import threading, time, json, datetime

"""
"""

LOCAL = threading.local()


def get_holder():
	try:
		return LOCAL.__getattribute__('holder')
	except:
		return None


def set_holder(holder):
	LOCAL.__setattr__('holder', holder)


class Node:
	def __init__(self, info):
		self.info = info
		self.start = int(round(time.time() * 1000))
		self.sub_nodes = []
		self.prev, self.next = None, None

	def stop(self):
		self.end = int(round(time.time() * 1000))

	def add_sub(self, node):
		self.sub_nodes.append(node)

	def get_cost_info(self) -> dict:
		costInfo = {'name': self.info, 'cost': self.end - self.start}
		if self.sub_nodes:
			costInfo['sub'] = [sub.get_cost_info() for sub in self.sub_nodes]
			costInfo['sub'].sort(key=take_cost, reverse=True)
		return costInfo


def take_cost(d: dict) -> int:
	return d['cost']


class Stack:
	def __init__(self):
		self.head, self.tail = None, None

	def push(self, node: Node):
		if not self.head:
			self.head = node
		else:
			self.tail.next = node
			node.prev = self.tail
		self.tail = node

	def pop(self) -> Node:
		if not self.tail: return None
		if self.head == self.tail:
			node: Node = self.head
			self.head, self.tail = None, None
		else:
			node = self.tail
			self.tail = self.tail.prev
			self.tail.next = None
		if self.should_remove():
			set_holder(None)
		return node

	def peek(self) -> Node:
		return self.tail

	def should_remove(self):
		return not self.head


def init():
	set_holder(Stack())


def mark(info: str):
	node: Node = Node(info)
	holder: Stack = get_holder()
	if not holder:
		holder = Stack()
		set_holder(holder)
	prev: Node = holder.peek()
	if prev: prev.add_sub(node)

	holder.push(node)


def try_info():
	holder: Stack = get_holder()
	if not holder: return
	node: Node = holder.pop()
	if not node: return
	node.stop()
	peek: Node = holder.peek()
	# 最后一个节点 则输出信息
	if not peek:
		info = node.get_cost_info()
		print(json.dumps(info))
