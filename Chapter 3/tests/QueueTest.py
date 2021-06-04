from QueueObj.Queue import Queue

test = Queue()

test.enqueue(1)
test.enqueue(2)
test.enqueue(3)

test.print()
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
