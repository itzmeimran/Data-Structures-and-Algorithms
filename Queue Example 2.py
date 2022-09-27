#DSA QUEUE 2
import collections 
q = collections.deque() 
print(q)
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.append(0)
q.append(-1)
q.appendleft(4)
print(q)
q.pop()
print(q)