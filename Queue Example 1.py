#DSA Queue 
queue = [5,15,20,25]
print('Given Queue', queue)
queue.append(30)
print("After Appending Queue", queue)
queue.pop()
print("After Removing Queue", queue)
queue.insert(0,0)
print("After Inserting Queue", queue)
print("Queue is empty -------> ",not queue)
