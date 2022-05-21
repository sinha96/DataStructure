class Node:
    """
    Creates a Node with data and next node info
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    """
    Creates a single linked list with head as none
    """
    def __init__(self):
        self.head = None

    def listprint(self):
        """
        prints linked list's nodes
        """
        val = self.head
        while val is not None:
            print(val.data)
            val = val.next

    def at_begining(self, data):
        """
        Add new node to the linked list at the begining
        :param data: new data to be inserted

        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def at_middle(self, data, middle_node):
        """
        Add new node inbetween the linked list
        :param data: data that has to be inserted
        :param middle_node: node after which new data has to be add
        """
        if middle_node is None:
            raise ValueError('Node is not available')

        node = Node(data)
        node.next = middle_node.next
        middle_node.next = node

    def remove_node(self, remove_key):
        head = self.head
        if head is not None:
            if head.data == remove_key:
                self.head = head.next
                head = None
                return
        while head is not None:
            if head.data == remove_key:
                break
            prev = head
            head = head.next
        if head is None:
            return
        prev.next = head.next
        head = None


sll = SLinkedList()
sll.head = Node('Priyanshu')
e2 = Node('Shekhar')
e3 = Node('Sinha')

sll.head.next = e2
e2.next = e3

sll.listprint()

sll.at_begining('Hi!')
sll.listprint()

sll.at_middle(middle_node=sll.head, data="Mr")
sll.listprint()

sll.remove_node('Shekhar')
sll.listprint()

