"""Leetcode Problem 146: LRU Cache https://leetcode.com/problems/lru-cache/
Implement an LRU Cache using Doubly linked list and HashMap
"""


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head & tail to simplify edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the list
    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert node right after head (most recently used)
    def _add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add_to_front(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # remove LRU node from tail
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
