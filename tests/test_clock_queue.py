import pytest
from clock_queue import Clock_queue, Node


# @pytest.mark.skip('create queue')

def test_create_queue():
    new_queue = Clock_queue()
    assert new_queue


# @pytest.mark.skip('add a single node')

def test_add_node():
    new_queue = Clock_queue()
    new_queue.enqueue(1)
    actual = new_queue.peek()
    expected = 1
    assert actual == expected


# @pytest.mark.skip('remove Node from the front')

def test_remove_node_from_front():
    new_queue = Clock_queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    actual = new_queue.dequeue()
    expected = 1
    assert actual == expected


# @pytest.mark.skip('test for rear node prev')

def test_pointers_for_front():
    new_queue = Clock_queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    actual = new_queue.rear.prev.value
    expected = 2
    assert actual == expected


@pytest.mark.skip('')
def test_pointers_for_rear():
    pass
