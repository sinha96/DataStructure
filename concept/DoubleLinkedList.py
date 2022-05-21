class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DLinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		node = Node(data)
		node.next = self.head
		if self.head is not None:
			self.head.prev = node
		self.head = node

	@staticmethod
	def viewer(node):
		while node is not None:
			print(node.data)
			last = node
			node = node.next

	@staticmethod
	def insert(prev_node, data):
		if prev_node is Node:
			return 1
		node = Node(data)
		node.next = prev_node.next
		prev_node.next = node
		node.prev = prev_node
		if node.next is not None:
			node.next.prev = node

	def append(self, data):
		node = Node(data)
		node.next = None
		if self.head is None:
			node.prev = None
			self.head = node
			return
		last = self.head
		while last.next is not None:
			last = last.next



dllist = DLinkedList()
dllist.push(10)
dllist.push(20)
dllist.push(30)
dllist.viewer(dllist.head)

dllist.insert(dllist.head.next, 100)
dllist.viewer(dllist.head)
