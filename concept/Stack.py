class Stack:
	"""
	Class to create stack data structure (FILO)
	"""
	def __init__(self):
		self.stack = list()

	def add(self, data):
		"""
		Adds new element to stack
		:param data: new data element

		"""
		if data not in self.stack:
			self.stack.append(data)
			return True
		else:
			return False

	def peek(self):
		"""
		To view last element of stack
		:return: last element of stack
		"""
		return self.stack[-1]

	def remove(self):
		"""
		Removes the last element
		:return: last element of the stack
		"""
		if len(self.stack) <= 0:
			return 'Stack is empty'
		return self.stack.pop()


stck = Stack()
stck.add(1)
stck.add(2)
stck.add(3)
stck.add(4)
stck.add(5)
print(stck.peek())
