# circular linked lists

# class to represent the node of the list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CreateList:
    # declaring the head and tail pointer as null
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    # this function will add the new node at the end of the list.
    def add (self,data):
        newNode = Node(data)
        # check if the list is empty
        if self.head.data is None:
            # if list is empty, both head and tail would point to new node
            self.head = newNode
            self.tail = newNode
        else:
            # tail will point to new node
            self.tail.next = newNode
            # new node will become new tail
            self.tail = newNode
            # since, it is circular linked list tail will point to head
            self.tail.next = self.head

            # display all the nodes in the list
    def display(self):
        current = self.head
        if self.head is None:
            print("List ;is empty")
            return
        else:
            print("Nodes of the circular linked lists")
            # prints each node by incrementing pointer
            print(current.data),
            while(current.next !=self.head):
                current = current.next
                print(current.data)

# create an instance of a Circular linked list
cl = CreateList()
# adds data to the list
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(4)
# displays all the nodes present in the list
cl.display()
