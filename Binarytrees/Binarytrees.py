class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Example tree
rt = TreeNode(1)
rt.right = TreeNode(2)
rt.right.left = TreeNode(3)
rt.right.right = TreeNode(4)
rt.left = TreeNode(5)
inorder(rt)  # Output: 5 1 3 2 4