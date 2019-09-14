from data_structures_module import *

q = Queue(10)
print(q)
for i in range(q.getSize()):
    q.EnQueue(i)
print(q)
q.DeQueue()
print(q)