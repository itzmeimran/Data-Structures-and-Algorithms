#DSA STACK
stack = []
def push():
    element = input("Enter the element:")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("stack is empty")
    else:
        e= stack.pop()
        print('removed elements:',e)
        print(stack)
while True:
    print("select the operation 1.push, 2.pop, 3.quit")
    
    cho= int(input())
    if cho == 1:
        push( )
    elif cho == 2:
        pop()
    elif cho == 3:   
        break        
    else:
        print("Enter the correct operation")