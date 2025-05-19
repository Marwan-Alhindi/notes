---
id: d8urs7cvccohawbrb2bgo8i
title: linkedlists
desc: ''
updated: 1746530517517
created: 1746445848244
---


•	What: Sequence of nodes, each pointing to the next
•	Types: Singly, Doubly, Circular
•	Access: O(n) to reach an index
•	Insert/Delete: O(1) if you have the node reference
•	Use cases: Undo feature, dynamic memory where shifting is expensive


```py
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:             # Empty list
            self.head = new_node
            return
        current = self.head
        while current.next:           # Traverse to end
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
```