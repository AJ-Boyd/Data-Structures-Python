"""
auth: AJ Boyd
date: 8/30/2023
desc: this is an implementation of a singly linked list with both a head and tail Node. 
    this program has two classes Node and LinkedList. linked lists are a fundamental 
    data structure that features dynamic size, O(1) time complexity for insertion/deletion 
    at the beginning, and a simple implementation method
"""

import random

class Node:
    #constructor initializes the properties of a Node
    def __init__(self, data = 0):
        self.data = data #the data the Node stores
        self.next = None #the next Node in the Linked List
    
    #accessors and mutators retrieve or change the properties of a Node
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
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
                curr.setNext(newNode)
                
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
                #loop until you get to the Node before the tail
                curr = self.head
                while curr.next != self.tail:
                    curr = curr.next
                #make Linked List re-connections
                curr.setNext(None)
                self.tail = curr
            
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
                
                curr.setNext((curr.getNext()).getNext())
                
                #decrement size
                self.size -= 1
                      
    #prints the data stored within each Node 
    def print(self):
        curr = self.head
        while(curr):
            print(curr.getData(), "->", end=" ")
            curr = curr.getNext()        
        print("END")

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

    #uses a merge sort algorithm to sort the Nodes in the Linked List
    def sort(self):
        #if Linked List is has fewer than 2 Nodes, it's already sorted
        if self.size > 1:
            #get middle element
            mid = self.size // 2
            
            #recursively sort both halves until only 1 Node remain in each Linked List
            left = self.sublist(0, mid)
            right = self.sublist(mid, self.size)  
            
            left.sort()
            right.sort()
            
            #merge sorted halves
            i = j = k = 0
            #merge and sort; keep looping until you run out of elements in the left or right sublist
            while i < left.size and j < right.size:
                if left.nodeAt(i).getData() <= right.nodeAt(j).getData():
                    self.nodeAt(k).setData(left.nodeAt(i).getData())
                    i += 1
                else:
                    self.nodeAt(k).setData(right.nodeAt(j).getData())
                    j += 1
                k += 1
            
            #pick up remaining elements
            while i < left.size:
                self.nodeAt(k).setData(left.nodeAt(i).getData())
                i += 1
                k += 1
    
            while j < right.size:
                self.nodeAt(k).setData(right.nodeAt(j).getData())
                j += 1
                k += 1
            
    #concatenates another Linked List to the end of the current one
    def concat(self, other):
        for i in range(other.size):
            self.insertEnd(other.nodeAt(i).getData())
               
    #concatenates another Linked List to the end of the current one, then sorts
    def merge(self, other):
        self.concat(other)
        self.sort()
    
    #returns the number of Nodes in the Linked List
    def getSize(self) -> int:
        return self.size
    
    #returns if the Linked List is empty of not
    def isEmpty(self) -> bool:
        return not self.head
    
def main():
    #create new Linked List and add 10 Nodes at random positions
    LL = LinkedList()
    for i in range(1, 11):
        LL.insertAt(random.randint(0, LL.getSize()), i*10)
    print("LL after inserting 10 Nodes: ", end=" ")
    LL.print()
    
    #sort that Linked List
    LL.sort()
    print("LL after sorting: ", end=" ")
    LL.print()
    
    #make a new Linked List and populate it
    LL2 = LinkedList()
    for i in range(11, 21):
        LL2.insertAt(random.randint(0, LL2.getSize()), i*10)
    print("LL2 after inserting 10 Nodes: ", end=" ")
    LL2.print()
    
    #merge LL and LL2
    LL.merge(LL2)
    print("LL after being merged with LL2: ", end=" ")
    LL.print()
    
    #randomly delete 5 Nodes from LL
    for i in range(5):
        LL.deleteAt(random.randint(0,LL.getSize()))
    print("LL after deleting 5 Nodes: ", end=" ")
    LL.print()
    
if __name__ == "__main__":
    main()
            