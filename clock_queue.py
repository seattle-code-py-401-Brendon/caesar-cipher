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

    def clock_wise(self, shift_num):
        for x in range(shift_num):
            value = self.dequeue()
            self.enqueue(value)

    def counter_clock_wise(self, shift_num):
        pass


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
    clock_queue.enqueue('a')
    clock_queue.enqueue('b')
    clock_queue.enqueue('c')
    clock_queue.enqueue('d')
    clock_queue.enqueue('e')
    clock_queue.clock_wise(3)
    clock_queue.print()
