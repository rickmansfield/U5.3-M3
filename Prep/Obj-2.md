# Unit 5.3 M3 Obj 2 Challenge

## Challenge
- In your own words, explain why an unbalanced binary search tree's performance becomes degraded.

- The primary weakness of a BST is that they only have efficient operations if they are balanced. The more unbalanced they are, the worse the efficiency of their operations gets. Another weakness is that they are don't have stellar efficiency in any one operation. They have good efficiency for a lot of different operations. So, they are more of a general-purpose data structure.

- Hence leaving a balanced tree with O(Log_n) to an unbalanced tree with O(n) means the curve no longer flatens out over time. Instead it is linear over time. Thus, keeping a tree balanced keeps is closer to O(log_n) and further from O(n)