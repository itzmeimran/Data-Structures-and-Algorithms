#Linked List
class Node:
    def __init__(self,data):
        self.data =data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")    
        else:
            n= self.head
            while n is not None:
                print(n.data,"----->", end = " ") 
                n = n.ref 
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
        else:
            n= self.head
            while n.ref is not None:
                n= n.ref
            n.ref = new_node
                
    def add_after(self,data,x):
        n =self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the list")
        else:
            new_node = Node(data) 
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self,data,x):
        n =self.head
        if n is None:
            print("Linked List is empty")
            return
        if n.data ==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n = n.ref
        if n.ref is not None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def del_begin(self):
        if self.head is None: 
            print("LinkedList is empty")
        else:
            self.head = self.head.ref
    def del_end(self):
        if self.head is None:
            print("LinkedList is empty")
        elif self.head.ref is None:
            self.head.ref = None
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
                n.ref = None
                
                
                
        
        
        

L= LinkedList()
L.add_begin(10)
L.add_begin(20)
L.add_begin(30)
L.add_end(5)
L.del_end()
L.print_LL()
