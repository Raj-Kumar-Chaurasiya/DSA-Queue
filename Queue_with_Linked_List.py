class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class myQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.currSize = 0  
        
    
    def isEmpty(self):
        return self.front is None

    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
    
        self.currSize += 1 

    
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return -1
        removedData = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
            

        self.currSize -= 1 
        return removedData

    def getfront(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.front.data

    
    def size(self):
        return self.currSize

if __name__ == "__main__":
    q = myQueue()
    
    q.enqueue(10)
    q.enqueue(20)
    
    print("Dequeue:", q.dequeue())
    
    q.enqueue(30)
    
    print("Front:", q.getfront())
    print("Size:", q.size())