class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


# FIFO

class Clock_queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = self.rear = node

        else:
            # THIS TOOK SO LONG TO FIGURE OUT!
            prev_node = self.rear
            self.rear.next = node
            node.prev = prev_node
        self.rear = node

    def dequeue(self):
        #     remove from front
        if self.front is None:
            return "Empty Queue"
        else:
            temp = self.front
            self.front = temp.next
            self.front.prev = None
            return temp.value

    def print(self):
        if self.front:
            current = self.front
            while current:
                print(current.value)
                current = current.next
        else:
            return 'empty queue'

    def peek(self):
        if self.front:
            return self.front.value
        else:
            return "Empty Queue"


if __name__ == '__main__':
    clock_queue = Clock_queue()
    clock_queue.enqueue('1')
    clock_queue.enqueue('2')
    clock_queue.enqueue('3')
    # print(clock_queue.front.prev)
    # print(clock_queue.rear.next)
    clock_queue.dequeue()
    clock_queue.print()
