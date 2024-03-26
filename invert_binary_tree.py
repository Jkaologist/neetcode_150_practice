from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root):
    if not root:
        return None

    l = invert_binary_tree(root.left)
    r = invert_binary_tree(root.right)
    root.left = r
    root.right = l

    return root


# def invert_binary_tree(root):
#     if not root:
#         return None
#     q = deque()
#     q.append(root)

#     while q:
#         curr = q.popleft()
#         curr.left, curr.right = curr.right, curr.left

#         if curr.left:
#             q.append(curr.left)
#         if curr.right:
#             q.append(curr.right)

#     return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(invert_binary_tree(root))
