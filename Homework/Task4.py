"""
NOTE NOTE NOTE
The recursive solutin starts on line 31
the code before it makes it work in VSCode
"""
class BinarySearchTree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# r = BinarySearchTree(5)
# r.left = BinarySearchTree(12)
# r.right = BinarySearchTree(32)
# r.right.left = BinarySearchTree(8)
# r.right.right = BinarySearchTree(4)
r = BinarySearchTree(5)
r.left = BinarySearchTree(10)
r.right = BinarySearchTree(25)
r.right.left = BinarySearchTree(12)
r.right.right = BinarySearchTree(3)
# r = BinarySearchTree(5)
# r.left = BinarySearchTree(6)
# r.right = BinarySearchTree(6)
# r.left.left = BinarySearchTree(7)
# r.left.right = BinarySearchTree(7)
# r.left.left.left = BinarySearchTree(8)
# r.left.left.right = BinarySearchTree(8)

def balancedBinaryTree(root):
    if root is None:
        return True
    
    if abs(depth(root.right)- depth(root.left)) >1:
        return False
    
    return balancedBinaryTree(root.left) and balancedBinaryTree(root.right)

def depth(root):
    if root is None:
        return 0
    else:
        left = depth(root.left)
        right = depth(root.right)
        return max(left, right) + 1

print(balancedBinaryTree(r))
