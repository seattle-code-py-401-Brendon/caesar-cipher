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

    def enqueue(self, value, side):
        node = Node(value)
        if side == 'r':
            # add to the rear
            if self.front is None:
                self.front = self.rear = node

            else:
                # THIS TOOK SO LONG TO FIGURE OUT!
                prev_node = self.rear
                self.rear.next = node
                node.prev = prev_node
            self.rear = node
        #     add to the front
        if side == 'f':
            if self.front is None:
                self.rear = self.front = node

            else:
                # THIS TOOK SO LONG TO FIGURE OUT!
                next_node = self.front
                self.front.prev = node
                node.next = next_node
            self.front = node

    def dequeue(self, side):
        #     remove from front
        if side == 'f':
            if self.front is None:
                return "Nothing to Dequeue"
            else:
                temp = self.front
                if self.front.next is None:
                    self.front = None
                    return temp.value
                else:
                    self.front = temp.next
                    self.front.prev = None
                    return temp.value
        # romove from rear
        if side == 'r':
            if self.rear is None:
                return "Nothing to Dequeue"
            else:
                temp = self.rear
                if self.rear.prev is None:
                    self.rear = None
                    return temp.value
                else:
                    self.rear = temp.prev
                    self.rear.next = None
                    return temp.value

    def clock_wise(self, shift_num):
        # shift clockwise
        for x in range(shift_num):
            value = self.dequeue('f')
            self.enqueue(value, 'r')

    def counter_clock_wise(self, shift_num):
        for x in range(shift_num):
            value = self.dequeue('r')
            self.enqueue(value, 'f')

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
    clock_queue.enqueue('a', 'r')
    clock_queue.enqueue('b', 'r')
    clock_queue.enqueue('c', 'r')
    clock_queue.counter_clock_wise(2)
    clock_queue.print()
