class Node:
    def __init__(self,data,next):
        self.data =data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size 
    def is_empty(self):
        return self.size == 0
    
    def display (self):
        thead = self.head
        while thead:
            print(thead.data, end="-->")
            thead = thead.next
        print()
        
    def addbegin(self,data):
        newnode = Node(data,None)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            # self.size+=1
        else:
            newnode.next = self.head
            self.head = newnode
        self.size+=1
    def addlast(self,data):
        newnode = Node(data,None)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode 
            self.size+=1
    def addany(self,data,x):
        newnode = Node(data, None)
        thead = self.head
        i = 1
        while i < x:
            thead = thead.next
            i+=1
        newnode.next = thead.next
        thead.next = newnode 
        self.size+=1 
    def delfirst(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            value = self.head.data 
            self.head = self.head.next
            self.size-=1
            return value 
    def delend(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            thead =self.head
            i = 0 
            while i < len(self)-2:
                thead = thead.next
                i+=1
            self.tail = thead
            thead = thead.next 
            val = thead.data
            self.tail.next = None
            self.size-=1
            return val 
    def delany(self,x):
        thead = self.head
        i=0
        while i < x-1:
            thead = thead.next
            i+1
        val = thead.next.data
        thead.next = thead.next.next
        self.size-=1
        return val
    
        
                 
a = Linkedlist()
a.addbegin(10)
a.addbegin(20)
a.addbegin(30)
a.addlast(40)
a.addlast(50)
a.addany(80,1)
a.display()
print("Length of linked list: ", a.__len__()) 
print("Deleted Node @ first: ", a.delfirst())
a.display()
print("Deleted Node @ last: ", a.delend())
a.display()
print("Deleted Node : ", a.delany(1))
a.display()
print("Length of linked list: ", a.__len__())         
            