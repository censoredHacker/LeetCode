from auto_live_reload import start_auto_live_reload
start_auto_live_reload()

# Built in Data Structures;

# 1. HashMaps
# 2. Sets
# 3. Stacks 
# 4. Queues
# 5. Linked Lists 



## HashMaps
# Basic operations: insert, delete, search
hash_map = {}
hash_map["key1"] = "value1"  # Insert
hash_map["key2"] = 123

value_1 = hash_map.get("key1")

# Deleting a key
del hash_map["key2"]

## Sets
# Basic operations: insert, delete, search
my_set = set()
my_set2 = {3,4,5}

my_set.add(1)  # Insert
my_set.add(2)

condition = 1 in my_set  # Search, value_1 is true
my_set.remove(2)  # Delete

union_set = my_set.union(my_set2)


## Stacks
# Basics: push, pop, peek, isEmpty

my_stack = []
my_stack.append(10)  # Push
my_stack.append(20)
top_element = my_stack[-1]  # Peek
popped_element = my_stack.pop()  # Pop
is_empty = len(my_stack) == 0  # isEmpty



## Queues
# Basics: enqueue, dequeue, front, isEmpty
from collections import deque
my_queue = deque()
my_queue.append(10)  # Enqueue
my_queue.append(20)

front_element = my_queue[0]  # Front
dequeued_element = my_queue.popleft()  # Dequeue 
is_empty = len(my_queue) == 0  # isEmpty

## Linked Lists
# Basics: insert, delete, search, traverse
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
# Inserting nodes
head = ListNode(1)  # Head node
second = ListNode(2)    
head.next = second
third = ListNode(3)
second.next = third
# Traversing the linked list
current = head
while current:
    print(current.value)  # Process current node
    current = current.next
    