class Queue:
	"""
	Class for Queue data structure (FIFO)
	"""
	def __init__(self):
		self.queue = list()

	def add(self, data):
		if data not in self.queue:
			self.queue.insert(0, data)
			return True
		else:
			return False

	def peek(self):
		return self.queue[0]

	def size(self):
		return len(self.queue)

	def remove(self):
		if len(self.queue) <= 0:
			return 'Queue is empty'
		return self.queue.pop()


if __name__ == '__main__':
	TheQueue = Queue()
	TheQueue.add("Mon")
	TheQueue.add("Tue")
	TheQueue.add("Wed")
	print(TheQueue.remove())
	print(TheQueue.remove())
