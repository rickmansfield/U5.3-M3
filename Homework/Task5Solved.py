"""
NOTE NOTE NOTE
The solutin starts on line 39
the code before it makes it work in VSCode
"""
class minimumDepthBinaryTree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# r = minimumDepthBinaryTree(5)
# r.left = minimumDepthBinaryTree(12)
# r.right = minimumDepthBinaryTree(32)
# r.right.left = minimumDepthBinaryTree(8)
# r.right.right = minimumDepthBinaryTree(4)

# r = minimumDepthBinaryTree(5)
# r.left = minimumDepthBinaryTree(10)
# r.right = minimumDepthBinaryTree(25)
# r.right.left = minimumDepthBinaryTree(12)
# r.right.right = minimumDepthBinaryTree(3)

# r = minimumDepthBinaryTree(5)
# r.left = minimumDepthBinaryTree(6)
# r.right = minimumDepthBinaryTree(6)
# r.left.left = minimumDepthBinaryTree(7)
# r.left.right = minimumDepthBinaryTree(7)
# r.left.left.left = minimumDepthBinaryTree(8)
# r.left.left.right = minimumDepthBinaryTree(8)

r = minimumDepthBinaryTree(5)
r.left = minimumDepthBinaryTree(7)
r.right = minimumDepthBinaryTree(22)
r.right.left = minimumDepthBinaryTree(17)
r.right.right = minimumDepthBinaryTree(9)


def minimumDepthBinaryTree(root):
    if root is None:
        return 0
    
    if root.left is None:
        return minimumDepthBinaryTree(root.right) +1
    
    if not root.right:
        return minimumDepthBinaryTree(root.left) +1
    
    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right))+1
    
print(minimumDepthBinaryTree(r))
