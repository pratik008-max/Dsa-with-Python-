class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.tail = None
    
class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        tempnode = self.head
        while tempnode:
            yield tempnode
            tempnode = tempnode.next
            if tempnode == self.tail.next:
                break
    
    def createCDLL(self,nodeValue):
        newnode = Node(nodeValue)
        self.head = newnode
        self.tail = newnode
        newnode.prev = newnode
        newnode.next = newnode
        return 'The Circular doubly linked list is Created Successfully.....'
    # Insertion method to insert node in Circular doubly Linked list 
    def insertNode(self,nodevalue,location):
        if self.head is None:
            print("There is no linked list here to insert node firt create one")
        else:
            newnode = Node(nodevalue)
            if location == 0:        #Check for First location 
                newnode.prev = self.tail
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
                self.tail.next = newnode
            elif location == 1:     #Check for Last location
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.tail.next = newnode
                self.tail = newnode
            else:                   #Check for specific location 
                tempnode =self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                newnode.next.prev = newnode
                tempnode.next = newnode
    # Traversal of Circular doubly linked list in forward direction 

    def traversalCDLL(self):
        if self.head is None:
            return "No LL is there to traverse"
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                if tempnode == self.tail:
                    break
                tempnode = tempnode.next
            
    #Reverse Traversal of CDLL (Backward Direction)
    def reverseTraversal(self):
        if self.head is None:
            return "No LL is there to print"
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                if tempnode == self.head:
                    break
                tempnode = tempnode.prev
    
    
    #Search a node in Linked list 
    def searchNode(self,nodevalue):
        if self.head is None:
            return "No linked list is there to search the node"
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodevalue:
                    return tempnode.value
                if tempnode.value == self.tail:
                    return "The Node does not exist in the CDLL"
                tempnode = tempnode.next
    
    # Delete Node from Circular Doubly Linked List 

    def deleteNode(self,location):
        if self.head is None:
            print("No ll is there to delete a node")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index += 1
                tempnode.next = tempnode.next.next
                tempnode.next.prev = tempnode
            return "Node is Deleted Successfully"

        





cdll = CircularDoublyLL()
print(cdll.createCDLL(3))
cdll.insertNode(1,0)
cdll.insertNode(3,1)
cdll.insertNode(5,0)
cdll.insertNode(29,2)
cdll.insertNode(34,4)
cdll.traversalCDLL()
print([node.value for node in cdll])
cdll.reverseTraversal()
print(cdll.searchNode(45))
print(cdll.deleteNode(0))