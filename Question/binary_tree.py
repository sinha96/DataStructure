class BinaryNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def height(node):
	if node is None:
		return 0
	return 1 + max(height(node.left), height(node.right))


def diameter(root):
	if root is None:
		return 0
	left_height = height(root.left)
	right_height = height(root.right)

	left_diameter = diameter(root.left)
	right_diameter = diameter(root.right)

	return max(left_height + right_height + 1, max(left_diameter, right_diameter))


def inorder(node):
	if not node:
		return
	inorder(node.left)
	print(node.data, end=' ')
	inorder(node.right)


def insert(node, data):
	if not node:
		root = BinaryNode(data)
		return root

	q = list()
	q.append(node)

	while len(q):
		tmp = q[0]
		q.pop(0)

		if not tmp.left:
			tmp.left = BinaryNode(data)
			break
		else:
			q.append(tmp.left)

		if not tmp.right:
			tmp.right = BinaryNode(data)
			break
		else:
			q.append(tmp.right)


if __name__ == '__main__':
	root = BinaryNode(10)
	root.left = BinaryNode(11)
	root.left.left = BinaryNode(7)
	root.right = BinaryNode(9)
	root.right.left = BinaryNode(15)
	root.right.right = BinaryNode(8)

	print("Inorder traversal before insertion:", end=" ")
	inorder(root)

	key = 12
	insert(root, key)

	print()
	print("Inorder traversal after insertion:", end=" ")
	inorder(root)