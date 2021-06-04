from NodeObj.Node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        inNode = Node(value)
        inNode.next = self.top
        self.top = inNode

    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            print("Stack underflow!")
            return None

    def pop(self):
        if self.top is not None:
            retVal = self.top.value
            self.top = self.top.next
            return retVal
        else:
            print("Stack underflow!")
            return None

    def isEmpty(self):
        return self.top is None

    def __str__(self):
        retStr = ""
        holder = self.top
        item = 0

        while holder is not None:
            if item == 0:
                retStr += str(holder.value)
            else:
                retStr += "," + str(holder.value)

            holder = holder.next
            item += 1

        return retStr

