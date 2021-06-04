from NodeObj.Node import Node


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        inVal = Node(value)
        if self.size == 0:
            self.front = self.rear = inVal
            self.size += 1
        else:
            self.rear.next = inVal
            self.rear = inVal
            self.size += 1

    def dequeue(self):
        if self.size != 0:
            retVal = self.front
            self.front = self.front.next
            self.size -= 1
            return retVal
        else:
            print("Queue underflow!")

    def peek(self):
        return self.front.value

    def isEmpty(self):
        return self.size == 0

    def print(self):
        holder = self.front

        while holder is not None:
            print(holder)
            holder = holder.next
