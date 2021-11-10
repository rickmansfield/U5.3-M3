"""
NOTE NOTE NOTE
The solutin starts on line 39
the code before it makes it work in VSCode
"""
class balancedBinaryTree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# r = balancedBinaryTree(5)
# r.left = balancedBinaryTree(12)
# r.right = balancedBinaryTree(32)
# r.right.left = balancedBinaryTree(8)
# r.right.right = balancedBinaryTree(4)

# r = balancedBinaryTree(5)
# r.left = balancedBinaryTree(10)
# r.right = balancedBinaryTree(25)
# r.right.left = balancedBinaryTree(12)
# r.right.right = balancedBinaryTree(3)

# r = balancedBinaryTree(5)
# r.left = balancedBinaryTree(6)
# r.right = balancedBinaryTree(6)
# r.left.left = balancedBinaryTree(7)
# r.left.right = balancedBinaryTree(7)
# r.left.left.left = balancedBinaryTree(8)
# r.left.left.right = balancedBinaryTree(8)

r = balancedBinaryTree(5)
r.left = balancedBinaryTree(7)
r.right = balancedBinaryTree(22)
r.right.left = balancedBinaryTree(17)
r.right.right = balancedBinaryTree(9)


def balancedBinaryTree(root):
    pass
    
    
print(balancedBinaryTree(r))