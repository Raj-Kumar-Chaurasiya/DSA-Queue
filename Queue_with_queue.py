from queue import Queue 
q = Queue(maxsize=4)
print(" Size of Queue: " ,q.qsize())

q.put('a')
q.put('b')
q.put('c')
q.put('d')

print("Queue : ", q.full())

print("To Remove the Element:")

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print("Queue if Empty: ",q.empty())

q.put(1)
print(" Queue is Full:" ,q.empty())
print("Then the Queue :", q.full())