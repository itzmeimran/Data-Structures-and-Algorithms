#Operations performed 1.Adding 2.Deleting 3. Traversal
class CircularLinkedList:
    
    class node:
        __slots__ = 'data','next'
        
        def __init__(self,data,next):
            self.data = data
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def add_first(self,data):
        newnode = self.node(data,None)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
            newnode.next = newnode
        else:
            self.tail.next = newnode
            newnode.next = self.head
        self.head = newnode
        self.size+=1
        
    def add_last(self,data):
        newnode = self.node(data,None)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
            newnode.next = newnode
        else:
            newnode.next = self.tail.next
            self.tail.next = newnode
        self.tail = newnode
        self.size+=1
    def add_any(self,data,pos):
        newnode = self.node(data,None)
        thead = self.head
        i = 1
        while i < pos:
            thead = thead.next
            i+=1
        newnode.next = thead.next
        thead.next = newnode
        self.size+=1
    def remove_first(self):
        if self.is_empty():
            print("Linked list is empty")
        oldhead = self.tail.next
        self.tail.next = oldhead.next
        self.head = oldhead.next
        self.size-=1
        if self.is_empty():
            self.tail = None
        print("Deleted : ",oldhead.data ) 
    
    def remove_last(self):
        if self.is_empty():
            print("Linked List is empty")
        thead = self.head
        i = 0 
        while i < len(self)-2:
            thead = thead.next
            i+=1
        self.tail = thead 
        thead = thead.next
        self.tail.next = self.head 
        value = thead.data
        self.size-=1
        print("Deleted : ", value)
    def display(self):
        thead = self.head
        i = 0  
        while i < len(self):
            print(thead.data, end='-->')
            thead = thead.next 
            i+=1
        print()
        
c = CircularLinkedList()
c.add_last(1)
c.add_last(3)
c.add_last(5)
c.add_last(7)
c.add_last(9)
c.add_last(11)
c.add_last(10)
c.add_first(20)
c.display()
c.remove_last()
c.display()
            
            
          

            