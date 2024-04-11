from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1, TreeNode(2), TreeNode(3))
def dfs(root):
    if not root:
        return
    dfs(root.left)
    print(root.val)
    dfs(root.right)

def bfs(root):
    deq = deque()
    deq.append(root)
    while deq:
        current = deq.popleft()
        if current.right:
            deq.append(current.right)
        if current.left:
            deq.append(current.left)

dfs(root)
bfs(root)