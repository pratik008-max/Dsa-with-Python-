class Node:
  def __init__(self,value=None):
    self.value = value
    self.next = None
    self.prev = None
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
  def createDLL(self,nodeValue):
    node = Node(nodeValue)
    node.next = None
    node.prev = Node
    self.head = node
    self.tail = node
  def insertion(self,nodeValue,location):
    if self.head is None:
      print("The node cannot be inserted")
    else:
      newnode = Node(nodeValue)
      if location == 0:
        newnode.prev = None
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
      elif location == 1:
        newnode.next = None
        newnode.prev = self.tail
        self.tail.next = newnode
        self.tail = newnode
      else:
        tempnode = self.head
        index = 0
        while index < location - 1:
          tempnode = tempnode.next
          index += 1
        newnode.next = tempnode.next
        newnode.prev = tempnode
        newnode.next.prev = newnode
        tempnode.next = newnode
  def traverseDLL(self):
      if self.head is None:
        print("There is no element to print")
      else:
          tempnode = self.head
          while tempnode:
              print(tempnode.value)
              tempnode = tempnode.next
                

doubly = DoublyLinkedList()
doubly.createDLL(0)
doubly.insertion(1,1)
doubly.insertion(3,1)
doubly.insertion(2,2)
