#QUEUE PROGRAM 2
queue = []
def enqueue():
    x= input("Enter Element:")
    queue.append(x)
    print(x,'is added to queue')
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        y= input("Enter Element:")
        queue.pop(y)
    print(y,'is removed from queue')
def display():
    print(queue)
while True:
    print("Select 1.Add, 2.Remove, 3.Show, 4.Quit")   
    a= int(input()) 
    if a==1:
        enqueue()
    elif a==2:
        dequeue()  
    elif a==3:
        display() 
    elif a==4:
        break
    else:
        print("Select correct input")
             