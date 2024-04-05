from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        deq = Deque([(q, p)],)

        while deq:
            current = deq.popleft()
            q, p = current
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            if p and q:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True
    
p = TreeNode(1)
q = TreeNode(1, None, TreeNode(2))

solution = Solution()
print(solution.isSameTree(p, q)) # False

