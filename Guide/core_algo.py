# Core Algorithms:
# 0. Sorting
# 1. Recursion
# 2. Backtracking
# 3. Binary Search
# 4. Divide & Conquer
# 6. Trees & Binary Search Trees
    # 6.1 DFS
    # 6.2 BFS
    # 6.3 inorder/preorder/postorder
    # 6.4 Lowest Common Ancestor
# 7. Heaps
# 8. Priority Queues


# CODE

# 0. Sorting
my_array = [5, 2, 9, 1, 5, 6]
sorted_array = sorted(my_array)

# 1. Recursion
 ## TBD in explaination

# 2. Backtracking
 ## TBD in explaination

# 3. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right: # main condition
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 4. Divide & Conquer
 ## TBD in explaination


# 6. Trees & Binary Search Trees
class TreeNode: # binary tree node
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 6.1 DFS
def dfs(root):
    if root is None:
        return
    print(root.val)  # Process the node
    dfs(root.left)
    dfs(root.right)
# 6.2 BFS
from collections import deque
def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)  # Process the node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# 6.3 inorder/preorder/postorder
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val)  # Process the node
    inorder_traversal(root.right)

def preorder_traversal(root):
    if root is None:
        return
    print(root.val)  # Process the node
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val)  # Process the node

# 6.4 Lowest Common Ancestor ## TBD explaination
def lowest_common_ancestor(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

# 7. Heaps ## explaination ## pyramid example
import heapq
def create_min_heap(elements):
    heapq.heapify(elements)
    return elements
def push_min_heap(heap, element):
    heapq.heappush(heap, element)
def pop_min_heap(heap):
    return heapq.heappop(heap)

# 8. Priority Queues ## explaination
def create_priority_queue(elements):
    return elements
def push_priority_queue(pq, element):
    pq.append(element)
    pq.sort(key=lambda x: x[0])  # Assuming element is a tuple (priority, value)
def pop_priority_queue(pq):
    return pq.pop(0)  # Pop the element with highest priority (lowest value)
