from DataStructure.concept.LinkedList import SLinkedList

# 1. Write a function to delete a Linked List
# 2. Find Length of a Linked List
# 3. Search an element in a Linked List
# 4. Access nth element of the linked list
# 5. Remove duplicates from a sorted linked list


class LinkedList(SLinkedList):
	def __init__(self):
		super().__init__()

	def delete(self):
		"""
		Deletes linked list data
		"""
		cnt = self.head
		while cnt:
			prv = cnt.next
			del cnt.data
			cnt = prv

	def _get_len(self, node):
		"""
		Returns total number of nodes
		"""
		if not node:
			return 0
		else:
			return 1 + self._get_len(node.next)

	def get_len(self):
		"""
		Returns total number of nodes
		"""
		return self._get_len(self.head)

	def search(self, node, data):
		"""
		Search element in a linkedlist
		"""
		if not node:
			return False
		if node.data == data:
			return 1
		return self.search(node.next, data)

	def iloc(self, index):
		"""
		Returns data of node for given index
		"""
		counter = 0
		cur = self.head
		while cur:
			if counter == index:
				return cur.data
			cur = cur.next
			counter += 1

	def drop_sorted_duplicates(self):
		"""
		Removes duplicated elements in a sorted linked list with complexity of O(n)
		"""
		tmp = self.head
		if tmp is None:
			return 1
		while tmp.next is not None:
			if tmp.data == tmp.next.data:
				unique_node = tmp.next.next
				tmp.next = None
				tmp.next = unique_node
			else:
				tmp = tmp.next
		return self.head

	def drop_duplicates(self):
		"""
		Removes duplicate elements in linked list with a complexity of O(n^2)
		"""
		ptr1 = self.head
		ptr2 = None
		dup = None
		while ptr1 is not None and ptr1.next is not None:
			ptr2 = ptr1
			while ptr2.next is not None:
				if ptr1.data == ptr2.next.data:
					dup = ptr2.next
					ptr2.next = ptr2.next.next
				else:
					ptr2 = ptr2.next

			ptr1 = ptr1.next

		return 1

	def remove_duplicates(self, head):
		"""
		Removes duplicated element from linked list with complexity of O(n)
		"""
		if self.head is None or self.head.next is None:
			return self.head

		visited_data = set()
		cur = head
		visited_data.add(self.head.data)
		while cur.next is not None:
			if cur.next.data in visited_data:
				cur.next = cur.next.next
			else:
				visited_data.add(cur.data)
				cur = cur.next
		return 1


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
	llist.remove_duplicates(llist.head)
	llist.listprint()
	print(f'Length of the Linked List is: {llist.get_len()}.')

	print("Deleting linked list")
	llist.delete()

	print("Linked list deleted")
	try:
		llist.listprint()
	except AttributeError as ex:
		print(ex)


