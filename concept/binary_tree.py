class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print(self.data)
		if self.right:
			self.right.print_tree()

	def insert(self, data):
		if data < self.data:
			if self.left is None:
				self.left = Node(data)
			else:
				self.left.insert(data)
		elif data > self.data:
			if self.right is None:
				self.right = Node(data)
			else:
				self.right.insert(data)

	def inorder(self, root):
		res = list()
		if root:
			res = self.inorder(root.left)
			res.append(root.data)
			res = res + self.inorder(root.right)
		return res


tree = Node(10)
tree.insert(5)
tree.insert(16)
tree.insert(1012)
tree.insert(50321)
print(tree.inorder(tree))
