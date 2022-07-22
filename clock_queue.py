import string

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

    # encryption helper method
    def clock_wise(self, letter=None, shift_num=None):
        # shift clockwise
        encryption = []
        if letter == ' ' or letter == ',' or letter == '!' or letter == '1':
            return letter
        elif self.front.value == letter:
            for x in range(shift_num):
                value = self.dequeue('f')
                self.enqueue(value, 'r')
            encrypted_letter = self.front.value
            encryption.append(letter)
        else:
            value = self.dequeue('f')
            self.enqueue(value, 'r')
            return self.clock_wise(letter, shift_num)
        return encrypted_letter

    def counter_clock_wise(self, letter=None, shift_num=None):
        if letter == ' ' or letter == ',' or letter == '!' or letter == '1':
            return letter
        elif self.rear.value == letter:
            for x in range(shift_num):
                value = self.dequeue('r')
                self.enqueue(value, 'f')
            encrypted_letter = self.rear.value

        else:
            value = self.dequeue('r')
            self.enqueue(value, 'f')
            return self.counter_clock_wise(letter, shift_num)
        return encrypted_letter

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
    alphabet = Clock_queue()
    whole_alphabets = list(string.ascii_lowercase)
    for letter in whole_alphabets:
        alphabet.enqueue(letter, 'r')
    list1 = 'hello world'
    # list2 = 'pmttw'
    secret_msg = ''
    decrypt_msg = ''
    for letter_e in list1:
        encrypt = alphabet.clock_wise(letter_e, 8)
        secret_msg += encrypt
    for letter_d in secret_msg:
        decrypt = alphabet.counter_clock_wise(letter_d, 8)
        decrypt_msg += decrypt
    print(secret_msg)
    print(decrypt_msg)
