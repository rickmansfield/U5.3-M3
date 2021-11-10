# Lets refactor the doubly linked list node to be a binary tree node
class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


bt = BTNode(10)
bt.left = BTNode(34)
bt.right = BTNode(12)
"""
[12, 34, 1, 56, 1]
        [12]
      /      \
     [1]      [34]
    /   \        \
  [1]   [12]    [56]
        /  \
      n     n

"""
