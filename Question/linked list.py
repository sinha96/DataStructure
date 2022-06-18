from DataStructure import SLinkedList, Node


# 1. Write a function to delete a Linked List
# 2. Find Length of a Linked List
# 3. Search an element in a Linked List
# 4. Access nth element of the linked list
# 5. Remove duplicates from a sorted and unsorted linked list
# 6. Swap nodes in a linked list without swapping data
# 7. Pairwise swap elements of a given linked list
# 8. Move last element to front of a given Linked List
# 9. Intersection of two Sorted Linked Lists
# 10. Reverse a Linked List in groups of given size
# 11. Find the middle of a given linked list
# 12. Write a function that counts the number of times a given int occurs in a Linked List
# 13. Detect loop in a linked list and number of node in the loop



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

	def swap(self, x, y):
		"""
		Swap two nodes in a linked list
		"""
		if x == y:
			return 1
		prev_x = None
		cur_x = self.head
		while cur_x is not None and cur_x.data != x:
			prev_x = cur_x
			cur_x = cur_x.next

		prev_y = None
		cur_y = self.head
		while cur_y is not None and cur_y.data != y:
			prev_y = cur_y
			cur_y = cur_y.next

		if cur_x is None or cur_y is None:
			return 1
		if prev_x is not None:
			prev_x.next = cur_y
		else:
			self.head = cur_y

		if prev_y is not None:
			prev_y.next = cur_x
		else:
			self.head = cur_x

		tmp = cur_x.next
		cur_x.next = cur_y.next
		cur_y.next = tmp

	def swap_pairwise(self):
		"""
		Swap pairwise elements of a linked list
		"""
		tmp = self.head

		if tmp is None:
			return

		while tmp and tmp.next:
			if tmp.data != tmp.next.data:
				tmp.data, tmp.next.data = tmp.next.data, tmp.data
			tmp = tmp.next.next

	def to_front(self):
		"""
		Move last element to front of a linked list
		"""
		tmp = self.head
		sec_last = None
		if not tmp or not tmp.next:
			return
		while tmp and tmp.next:
			sec_last = tmp
			tmp = tmp.next
		sec_last.next = None
		tmp.next = self.head
		self.head = tmp

	def sorted_intersect(self, a, b):
		"""
		Intersection of two sorted linked lists
		"""

		# base case
		if a is None or b is None:
			return None

		# If both lists are non-empty
		# Advance the smaller list and call recursively
		if a.data < b.data:
			return self.sorted_intersect(a.next, b)

		if a.data > b.data:
			return self.sorted_intersect(a, b.next)

		# Below lines are executed only
		# when a.data == b.data
		temp = Node()
		temp.data = a.data

		# Advance both lists and call recursively
		temp.next = self.sorted_intersect(a.next, b.next);
		return temp

	def grp_reverse(self, head, n):
		"""
		Method to reverse node in a pair of n

		:param head: Starting Node
		:param n: Number of Node to be reversed
		"""
		if head is None:
			return None
		current = head
		nxt = None
		prv = None
		count = 0

		while current is not None and count < n:
			nxt = current.next
			current.next = prv
			prv = current
			current = nxt
			count += 1

		if nxt is not None:
			head.next = self.grp_reverse(nxt, n)

		return prv

	def middle_element(self):
		node = self.head
		ln = self._get_len(node)
		idx = ln // 2
		return self.iloc(idx)

	def counter(self, node, data):
		if node is None:
			return 0
		elif node.data != data:
			return 0 + self.counter(node.next, data)
		elif node.data == data:
			return 1 + self.counter(node.next, data)

	def loop_detector(self):
		node = self.head
		unique_nodes = set()
		loop_node = set()
		node_counter = 0
		loop_start = None
		while node:
			if node in unique_nodes:
				loop_start = node
				break
			unique_nodes.add(node)
			node = node.next
		print('initiating node counting')
		while loop_start not in loop_node:
			node_counter += 1
			loop_node.add(loop_start)
			loop_start = loop_start.next
		if loop_start:
			return f"Found loop in the Linked list with length {node_counter}"
		return "Didn't found any loop in the linked list"


if __name__ == '__main__':
	llist = LinkedList()

	for i in range(10):
		if i % 2:
			llist.at_begining(i)
		else:
			llist.at_begining(i ** 2)
	llist.head.next.next.next.next = llist.head  # adding loop in linked list
	# llist.listprint()
	print(llist.loop_detector())
# print(llist.middle_element())
# print(llist.counter(node=llist.head, data=3))
# if llist.search(llist.head, 3):
# 	print('Present')
# else:
# 	print('Absent')
# print(f'{llist.iloc(1)} At 2nd index of linked list')
# llist.swap(4, 1)
# llist.listprint()
# llist.remove_duplicates(llist.head)
# llist.listprint()
# llist.swap_pairwise()
# llist.listprint()
# llist.to_front()
# llist.listprint()
# print(llist.head.data)
# print('performing group reverse')
# llist.listprint()
# llist.head = llist.grp_reverse(llist.head, 2)
# llist.listprint()
# print(f'Length of the Linked List is: {llist.get_len()}.')
#
# print("Deleting linked list")
# llist.delete()
#
# print("Linked list deleted")
# try:
# 	llist.listprint()
# except AttributeError as ex:
# 	print(ex)
