class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node

	def printlist(self, n):
		if n is None:
			print(n)
			return
		print(n.data, end='->')
		self.printlist(n.next)

	def add_node(self, data, prev):
		node = Node(data)
		prev_node = self.head
		while prev_node is not None:
			if prev_node.data == prev:
				next = prev_node.next
				prev_node.next = node
				node.next = next
			prev_node = prev_node.next


ln = LinkedList()
for i in range(1, 10):
	ln.insert(i)

ln.printlist(ln.head)
ln.add_node(100, 6)
ln.printlist(ln.head)
