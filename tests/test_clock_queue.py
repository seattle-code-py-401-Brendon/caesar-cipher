import pytest
from clock_queue import Clock_queue, Node


# @pytest.mark.skip('create queue')

def test_create_queue():
    new_queue = Clock_queue()
    assert new_queue


# @pytest.mark.skip('add a single node')

def test_add_node():
    new_queue = Clock_queue()
    new_queue.enqueue(1, 'r')
    actual = new_queue.peek()
    expected = 1
    assert actual == expected


# @pytest.mark.skip('remove Node from the front')

def test_remove_node_from_front():
    new_queue = Clock_queue()
    new_queue.enqueue(1, 'r')
    new_queue.enqueue(2, 'r')
    new_queue.enqueue(3, 'r')
    actual = new_queue.dequeue('f')
    expected = 1
    assert actual == expected


# @pytest.mark.skip('test for rear node prev')

def test_pointers_for_front():
    new_queue = Clock_queue()
    new_queue.enqueue(1, 'r')
    new_queue.enqueue(2, 'r')
    new_queue.enqueue(3, 'r')
    actual = new_queue.rear.prev.value
    expected = 2
    assert actual == expected


# @pytest.mark.skip('')
def test_clock_wise_shift():
    new_queue = Clock_queue()
    new_queue.enqueue('a', 'r')
    new_queue.enqueue('b', 'r')
    new_queue.enqueue('c', 'r')
    new_queue.enqueue('d', 'r')
    new_queue.enqueue('e', 'r')
    new_queue.clock_wise('c', 2)
    actual = new_queue.peek()
    expected = 'e'
    assert actual == expected
