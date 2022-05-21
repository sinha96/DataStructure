class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DLinkedList:
	"""
	Double linked list Data structure
	"""
	def __init__(self):
		self.head = None

	def push(self, data):
		"""
		Adds new nodes to the double linked list
		:param data: new data to be added
		"""
		node = Node(data)
		node.next = self.head
		if self.head is not None:
			self.head.prev = node
		self.head = node

	def viewer(self):
		"""
		Prints linked list from the given node
		:param node: starting point of the graph
		"""
		node = self.head
		if node is None:
			return 'Double linked list is empty'

		while node is not None:
			if node.next is None:
				ender = '\n'
			else:
				ender = '<-'
			print(node.data, end=ender)
			node = node.next

	@staticmethod
	def insert(prev_node, data):
		"""
		Adds new data node in the graph
		:param prev_node: data node after which the data has to be inserted
		:param data: data that has to be inserted
		"""
		if prev_node is Node:
			return 1
		node = Node(data)
		node.next = prev_node.next
		prev_node.next = node
		node.prev = prev_node
		if node.next is not None:
			node.next.prev = node

	def append(self, data):
		"""
		Adds data node the beginning of the double linked list
		:param data: data that has to be inserted
		"""
		node = Node(data)
		node.next = None
		if self.head is None:
			node.prev = None
			self.head = node
			return
		last = self.head
		while last.next is not None:
			last = last.next
		last.next = node
		node.prev = last
		return 1


dllist = DLinkedList()
dllist.push(10)
dllist.push(20)
dllist.push(30)
dllist.viewer()

dllist.insert(dllist.head.next, 100)
dllist.viewer()

dllist.append(45)
dllist.viewer()
