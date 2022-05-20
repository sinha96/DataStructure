class Stack:
	def __init__(self):
		self.stack = list()

	def add(self, data):
		if data not in self.stack:
			self.stack.append(data)
			return True
		else:
			return False

	def peek(self):
		return self.stack[-1]

	def remove(self):
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
