# Lets review insert
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
            this follows the rule set to build a BST:
            it is built to sort the data as we insert each element.
            in this case it allows for duplicates due to the else clause.
            if we wanted to get rid of duplicates 
            we could change the right case in to an elif
        """

        # left case?
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        # right case (for no dups change to "elif value > self.value:")
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        # base case (we found the target)
        if target == self.value:
            return self

        # left case
        if target < self.value:
            if self.left is None:
                return False
            else:
                self.left.search(value)

        # right case (if you change the case in the insert also change it here)
        else:
            if self.right is None:
                return False
            else:
                self.right.search(value)


bt = BSTNode(10)
bt.left = BSTNode(34)
bt.right = BSTNode(12)
"""
[12, 34, 1, 56, 1]
        [12]
      /      \
     [1]      [34]
    /   \        \
  [1]   [12]    [56]
  /    /  \
 [1]     n     n
- Each Node can have up to 2 children (left, right)
- if a number is inserted we run over this algorithm
- if the current node is None, insert here
- if value is less than to the root value then move to the left and run an insert on the left
- otherwise move to the right and run an insert on the right

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
"""
