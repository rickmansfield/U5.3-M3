"""
You are given a binary tree.
Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.
Example:
Given the following binary tree

root == none ?? return a zero

    5
   / \
 12  32
     /  \
    8     4 
  /  \   /  \
  n
your function should return the depth = 3.


PLAN Recursive
--------------
base case
if there is no root then return 0

recursive case...
  left case
  set a left height variable to a call to the max depth on the left node

  right case
  set right height variable to a call to the max depth on the right node

  return something
  get the max of the left height and the right height then add one for self

"""

from time import time


class BinarySearchTree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


r = BinarySearchTree(5)
r.left = BinarySearchTree(12)
r.right = BinarySearchTree(32)
r.right.left = BinarySearchTree(8)
r.right.right = BinarySearchTree(4)


def maxDepthR(root):
    if root is None:
        return 0
    else:
        left_height = maxDepthR(root.left)
        right_height = maxDepthR(root.right)

        return max(left_height, right_height) + 1


def maxDepthI(root):
    pass


start = time()  # now
print(maxDepthR(r))
end = time()  # now
print("recursive time", end - start)

start = time()
print(maxDepthI(r))
end = time()
print("iterative time", end - start)
