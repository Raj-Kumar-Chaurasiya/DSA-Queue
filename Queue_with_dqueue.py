from collections import deque
q = deque()

q.append('a')
q.append('b')
q.append('c')
q.append('d')

print("Queue : ", q)

print("To Remove the Element:")

print(q.popleft())
print(q.popleft())
print(q.popleft())
#print(q.popleft())

print("Then the Queue :", q)