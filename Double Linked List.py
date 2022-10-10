class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev
class DLinkedlist:
    def __init__(self):
        self.head  = None
        self.tail = None
        self.size = 0  
        
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            thead = self.head
            while thead:
                print(thead.data, end = ' -->')
                thead = thead.next
            print()
            
    def addfirst(self,data):
        newnode = Node(data,None,None)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode 
            self.head = newnode 
            newnode.prev = None 
        self.size+=1 
        
    def addend(self,data):
        newnode = Node(data,None,None)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            thead = self.head
            while thead.next is not None:
                thead = thead.next
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
            self.tail.next = None
        self.size+=1
    
    def addany(self,data,pos):
        newnode = Node(data,None,None)
        thead = self.head
        i = 1
        while i < pos:
            thead = thead.next
            i+=1
        newnode.next = thead.next 
        thead.next.prev = newnode
        thead.next = newnode
        newnode.prev = thead
        self.size+=1
    
    def delfirst(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            value =self.head.data
            self.head = self.head.next             
            self.head.next.prev = None 
            self.size-=1    
            return value
    def delend(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            value = self.tail.data
            self.tail = self.tail.prev
            self.tail.next  = None
            self.size-=1
            return value
        
    def delany(self,x):
        thead = self.head
        i = 1
        while i < x-1:
            thead = thead.next
            i+=1
        value = thead.next.data
        thead.next = thead.next.next
        thead.next.prev = thead         
        self.size-=1 
        return value 
        
            
                
a = DLinkedlist()
a.addend(10)
a.addend(20)
a.addfirst(5)
a.addfirst(1)
a.addend(30)
a.addend(40)
a.addany(100,2)
a.display()
print("Deleted : ",a.delany(3))
a.display()
print("Deleted : ",a.delfirst())
print("Deleted : ",a.delend())
a.display()
       