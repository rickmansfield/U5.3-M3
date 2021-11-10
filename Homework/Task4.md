# Unit 5.3 M3 Task 4

## Instructions
- You are given a binary tree and you need to write a function that can determine if it is height-balanced.

- A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

## Example 1:
- Given the following tree [5,10,25,None,None,12,3]:
-  returns __True__
```python
    5
   / \
 10  25
    /  \
   12   3
```
## Example 2:
- Given the following tree [5,6,6,7,7,None,None,8,8]: 
- returns __False__
```python
       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
```

## Constraints
- [execution time limit] 4 seconds (py3)

- [input] tree.integer root

- [output] boolean