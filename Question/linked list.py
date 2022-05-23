from DataStructure.concept.LinkedList import SLinkedList

# 1. Write a function to delete a Linked List
# 2. Find Length of a Linked List
# 3. Search an element in a Linked List
# 4. Access nth element of the linked list


class LinkedList(SLinkedList):
	def __init__(self):
		super().__init__()

	def delete(self):
		cnt = self.head
		while cnt:
			prv = cnt.next
			del cnt.data
			cnt = prv

	def _get_len(self, node):
		if not node:
			return 0
		else:
			return 1 + self._get_len(node.next)

	def get_len(self):
		return self._get_len(self.head)

	def search(self, node, data):
		if not node:
			return False
		if node.data == data:
			return 1
		return self.search(node.next, data)

	def iloc(self, index):
		counter = 0
		cur = self.head
		while cur:
			if counter == index:
				return cur.data
			cur = cur.next
			counter += 1


if __name__ == '__main__':
	llist = LinkedList()
	llist.at_begining(1)
	llist.at_begining(4)
	llist.at_begining(1)
	llist.at_begining(12)
	llist.at_begining(1)
	llist.listprint()
	if llist.search(llist.head, 12):
		print('Present')
	else:
		print('Absent')
	print(f'{llist.iloc(1)} At 2nd index of linked list')
	print(f'Length of the Linked List is: {llist.get_len()}.')

	print("Deleting linked list")
	llist.delete()

	print("Linked list deleted")
	try:
		llist.listprint()
	except AttributeError as ex:
		print(ex)


