

class Node:
    def __init__(self,value=None):   #node creation 
        self.value = value
        self.next = None
    


class SLinkedList:
    def __init__(self): #Linked list creation 
        self.head = None
        self.tail = None

    def __iter__(self):     #make list Iterable
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, value, location): #Insert method for quick insertion 
        newnode = Node(value) #create node 
        if self.head is None: #check for empty list
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:   #at beginning of linked list 
                newnode.next = self.head
                self.head = newnode
            elif location == 1: # At last of LL
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:               #Specific location
                tempnode = self.head
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
        
    def traverseSLL(self):
        if self.head is None:
            print("The Linkes list is Not Exists......Insert Some Elements in the list.")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "Linked is not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The element does not exist in the list"

sl1 = SLinkedList()

sl1.insert(2,0)

sl1.insert(3,1)
sl1.insert(21,0)
sl1.insert(223,1)
sl1.insert(5,4)
sl1.insert(9,2)
sl1.insert(12,2)
sl1.insert(34,1)
sl1.searchSLL(12)
print(sl1.searchSLL(34))
