# Unit 5.3 M3 Objective 3 Challenge

## Instructions
- To implement a delete operation on our BST and BSTNode classes, we must consider three cases:

1. If the BSTNode to be deleted is a leaf (has no children), we can remove that node from the tree.
2. If the BSTNode to be deleted has only one child, we copy the child node to be deleted and delete it.
3. If the BSTNode to be deleted has two children, we have to find the "in-order successor". The "in-order successor" is the next highest value, the node that has the minimum value in the right subtree.

- Given the above information, can you write pseudocode for a method that can find the minimum value of all the nodes within a tree or subtree?

