"""
auth: AJ Boyd
date: 9/1/2023
desc: this is an implementation of a doubly linked list with both a head and tail Node.
    the key difference between a singly and doubly linked list is that a doubly linked list
    has both a next and prev attribute, allowing each node to see its preceeding Node.
    this program has two classes Node and LinkedList. linked lists are a fundamental 
    data structure that features dynamic size, O(1) time complexity for insertion/deletion 
    at the beginning and end, and a simple implementation method.
"""

import random

class Node:
    #constructor initializes the properties of a Node
    def __init__(self, data = 0):
        self.data = data #the data the Node stores
        self.next = None #the next Node in the Linked List
        self.prev = None #the previous Node in the Linked List
    
    #accessors and mutators retrieve or change the properties of a Node
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def setPrev(self, prev):
        self.prev = prev
    
    def getPrev(self):
        return self.prev
    
    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
class LinkedList:
    #constructor initializes the properties of the Linked List
    def __init__(self):
        self.head = None #the head Node
        self.tail = None #the tail Node
        self.size = 0 #the number of Nodes in the Linked List
        
    #inserts a new Node at the front of the List
    def insertFront(self, data):
        #make a new Node object
        newNode = Node(data)
        
        if self.head:
            #if Linked List is populated, only head becomes the new Node
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        else:
            #if Linked List is empty, both head and tail become the new Node
            self.head = newNode
            self.tail = newNode
            
        #increment size   
        self.size += 1
         
    #inserts a new Node at the end of List   
    def insertEnd(self, data):
        newNode = Node(data)
        
        if self.head:
            #if Linked List is populated, only tail becomes the new Node
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
        else:
            #if Linked List is empty, both head and tail become the new Node
            self.head = newNode
            self.tail = newNode
            
        #increment size   
        self.size += 1
        
    #insets a new Node at a given index in the List
    def insertAt(self, index: int, data):
        #validate index range
        if index >= 0 and index <= self.size:
            #if inserting at the front, just call the insertFront(...) method
            if index == 0:
                self.insertFront(data)
            #else if inserting at the end, just call the insertEnd(...) method
            elif index == self.size:
                self.insertEnd(data)
            #else, we add somewhere in the middle
            else:
                #make new Node
                newNode = Node(data)
                
                #loop to Node before index
                curr = self.head
                for i in range(index - 1):
                    curr = curr.getNext()
                    
                #insert new Node at index, maintaining the links
                newNode.setNext(curr.getNext())
                curr.getNext().setPrev(newNode)
                curr.setNext(newNode)
                newNode.setPrev(curr)
                
                #increment size
                self.size += 1
                
    #deletes the Node at the front of the List
    def deleteFront(self):
        #check if Linked List is populated
        if self.head:
            #check if only one Node in Linked List
            if self.head == self.tail:
                self.tail = None
                
            self.head = self.head.getNext()
            self.head.setPrev(None)
            
            #decrmement size
            self.size -= 1
    
    #deletes the Node at the end of the List        
    def deleteEnd(self):
        #check if Linked List is populated
        if self.head:
            #check if only one Node in Linked List
            if self.head == self.tail:
                self.tail = None
                self.head = self.head.getNext()
            else:
                self.tail = self.tail.getPrev()
                self.tail.setNext(None)
            
            #decrmement size
            self.size -= 1
             
    #deletes the Node at the given index      
    def deleteAt(self, index: int):
        #validate index range
        if index >= 0 and index < self.size:
            if index == 0:
                self.deleteFront()
            elif index == self.size - 1:
                self.deleteEnd()
            else:
                curr = self.head
                for i in range(index - 1):
                    curr = curr.getNext()
                
                bridge = curr.getNext().getNext()
                curr.setNext(bridge)
                bridge.setPrev(curr)
                
                #decrement size
                self.size -= 1
                
    #returns true if a Node with the corresponding data exists in the Linked List
    def exists(self, data) -> bool:
        #start at head and loop through Nodes in Linked List
        curr = self.head
        while curr != None:
            #if the data matches, return True
            if curr.getData() == data:
                return True
            curr = curr.getNext()
        #else return False
        return False
    
    #returns the index of the Node with the corresponding data
    #returns -1 if the data is not found
    def indexOf(self, data):
        #start at head and loop through Nodes in Linked List
        curr = self.head
        for i in range(self.size):
            #if the data matches, return index
            if curr.getData() == data:
                return i
            curr = curr.getNext()
        #else return -1
        return -1
    
    #returns a sublist at the given points (exclusive)
    def sublist(self, start: int, end: int):
        #range validation
        if start < 0:
            start = 0
        if end > self.size:
            end = self.size
            
        #create new Linked List and deep copy Nodes over
        sublist = LinkedList()
        for i in range(start, end):
            sublist.insertEnd(self.nodeAt(i).getData())
        
        return sublist
    
    #concatenates another Linked List to the end of the current one
    def concat(self, other):
        for i in range(other.size):
            self.insertEnd(other.nodeAt(i).getData())
    
    #returns the Node at the given index (zero-indexed)
    def nodeAt(self, index: int) -> Node:
        #validates the index is between 0 and the size (exclusive)
        #if index is invalid, returns None
        if index >= 0 and index < self.size:
            curr = self.head
            for i in range(index):
                curr = curr.getNext()
            return curr #.getData()
        return None
    
    #prints the data stored within each Node 
    def print(self):
        curr = self.head
        print("START <->", end= " ")
        while(curr):
            print(curr.getData(), "<->", end=" ")
            curr = curr.getNext()        
        print("END")
        
    #prints the Linked List in reverse order
    def rprint(self):
        curr = self.tail
        print("END <->", end=" ")
        while(curr):
            print(curr.getData(), "<->", end=" ")
            curr = curr.getPrev()
        print("START")
        
    #returns the number of Nodes in the Linked List
    def getSize(self) -> int:
        return self.size
    
    #returns if the Linked List is empty of not
    def isEmpty(self) -> bool:
        return not self.head
        
def main():
    #create new Linked List and add 10 Nodes at random positions
    for i in range(1, 11):
        LL.insertAt((i-1), i*10)
    print("LL after inserting 10 Nodes:")
    LL.print()
    LL.rprint()
    
if __name__ == "__main__":
    main()