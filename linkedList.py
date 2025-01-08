class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtIndex(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def InsertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def InsertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def UpdateNode(self, data, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current:
            current.data = data

    def RemoveNodeAtIndex(self, index):
        if not self.head:
            raise IndexError("List is empty")

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data

        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next

        data = current.next.data
        current.next = current.next.next
        return data

    def RemoveNodeAtEnd(self):
        if not self.head:
            raise IndexError("List is empty")

        if not self.head.next:
            data = self.head.data
            self.head = None
            return data

        current = self.head
        while current.next and current.next.next:
            current = current.next

        data = current.next.data
        current.next = None
        return data

    def RemoveNodeAtBegin(self):
        if not self.head:
            raise IndexError("List is empty")

        data = self.head.data
        self.head = self.head.next
        return data

    def SizeOfList(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def Concatenate(self, other_list):
        if not self.head:
            self.head = other_list.head
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head

    def Invert(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def Display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def InsertAtBegin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        new_node.next = self.head
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        self.head = new_node

    def Display(self):
        elements = []
        if not self.head:
            return elements

        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def InsertAtBegin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def RemoveNodeAtEnd(self):
        if not self.head:
            raise IndexError("List is empty")

        if not self.head.next:
            data = self.head.data
            self.head = None
            return data

        current = self.head
        while current.next:
            current = current.next

        data = current.data
        current.prev.next = None
        return data

    def Display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class Stack:
    def __init__(self):
        self.list = SinglyLinkedList()

    def Push(self, data):
        self.list.InsertAtBegin(data)

    def Pop(self):
        return self.list.RemoveNodeAtBegin()

    def Peek(self):
        if not self.list.head:
            raise IndexError("Stack is empty")
        return self.list.head.data

    def IsEmpty(self):
        return self.list.head is None

    def Display(self):
        return self.list.Display()

class Queue:
    def __init__(self):
        self.list = SinglyLinkedList()

    def Enqueue(self, data):
        self.list.InsertAtEnd(data)

    def Dequeue(self):
        return self.list.RemoveNodeAtBegin()

    def IsEmpty(self):
        return self.list.head is None

    def Display(self):
        return self.list.Display()

class Array:
    def __init__(self):
        self.list = SinglyLinkedList()

    def Add(self, data):
        self.list.InsertAtEnd(data)

    def Get(self, index):
        current = self.list.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current:
            return current.data
        raise IndexError("Index out of range")

    def Remove(self, index):
        return self.list.RemoveNodeAtIndex(index)

    def Display(self):
        return self.list.Display()

singly_list = SinglyLinkedList()
singly_list.InsertAtEnd(1)
singly_list.InsertAtEnd(2)
singly_list.InsertAtEnd(3)
print("Singly Linked List:", singly_list.Display())

circular_list = CircularLinkedList()
circular_list.InsertAtEnd(10)
circular_list.InsertAtEnd(20)
circular_list.InsertAtBegin(5)
print("Circular Linked List:", circular_list.Display())

doubly_list = DoublyLinkedList()
doubly_list.InsertAtEnd(100)
doubly_list.InsertAtEnd(200)
doubly_list.InsertAtBegin(50)
print("Doubly Linked List:", doubly_list.Display())

stack = Stack()
stack.Push(10)
stack.Push(20)
stack.Push(30)
print("Stack:", stack.Display())
print("Popped from Stack:", stack.Pop())
print("Stack after pop:", stack.Display())

queue = Queue()
queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)
print("Queue:", queue.Display())
print("Dequeued from Queue:", queue.Dequeue())
print("Queue after dequeue:", queue.Display())

array = Array()
array.Add(5)
array.Add(10)
array.Add(15)