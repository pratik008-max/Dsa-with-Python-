class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    
class CircularSLL:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    #Create Circular Linked list   
    
    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.head = node
        return "The Circular Singly Linked List is created......"
    
    #Insertion method in CSLL 
    
    def insertCSLL(self, value, location):
    #"""Inserts a new node with the given value at the specified location in the circular singly linked list.

    # Args:
    #     value: The value to store in the new node.
    #     location: The desired insertion position (0 for beginning, 1 for end, or a specific index).

    # Returns:
    #     A string indicating success ("The node is inserted successfully") or failure ("Invalid location").
    # """

        if self.head is None:
            # Handle empty list (create a new circular linked list)
            new_node = Node(value)
            new_node.next = new_node  # Set next pointer to itself for a single-node circular list
            self.head = self.tail = new_node
            return "The node is inserted successfully"

        new_node = Node(value)
        if location == 0:
            # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node  # Update tail's next for circularity
            return "The node is inserted successfully"
        elif location == 1:
            # Insert at the end (becomes the new tail)
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            return "The node is inserted successfully"
        else:
            # Insert at a specific index (similar to previous else block)
            temp_node = self.head
            index = 0
            while index < location - 1 and temp_node.next is not self.head:
                temp_node = temp_node.next
                index += 1

            if index < location - 1:  # Invalid location (beyond list length)
                return "Invalid location"

            next_node = temp_node.next
            temp_node.next = new_node
            new_node.next = next_node
            return "The node is inserted successfully"


    def traverseCSll(self):
        if self.head is None:
            print("The Linked list is not exist.....")
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    break
    
    def searchCSLL(self , nodeValue):
        if self.head is None:
            return "The node does not exist...."
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodeValue:
                    return tempnode.value
                if tempnode == self.tail.next:
                    return "The Node does not exist in the linked list..."


    def deleteCSLL(self, location):
        if self.head is None:
            return "There is no linked lst exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail =None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = nextnode.next
                


circuCSLL = CircularSLL()
circuCSLL.insertCSLL(2,0)
circuCSLL.insertCSLL(3,1)
circuCSLL.insertCSLL(26,0)
circuCSLL.insertCSLL(7,2)
circuCSLL.insertCSLL(2,3)
circuCSLL.traverseCSll()
print(circuCSLL.searchCSLL(5))
print([node.value for node in circuCSLL])
