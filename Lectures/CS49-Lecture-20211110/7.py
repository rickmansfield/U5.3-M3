# Bonus Video Delete a node from BST (11 mins watch time) https://www.youtube.com/watch?v=Z0ZnRd2w8Ik
# value
# left
# right

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.search(target)

    def delete(self, value):
        if self is None:
            return self

        if value < self.value:
            self.left = self.left.delete(value)

        elif value > self.value:
            self.right = self.right.delete(value)

        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.left.min_node()

            self.value = temp.value

            self.right = self.right.delete(temp.value)

        return self

    def print_inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.print_inorder()
            print(self.value)
            if self.right is not None:
                self.right.print_inorder()


n1 = BSTNode(10)

n1.insert(5)
n1.insert(20)
n1.insert(40)
n1.insert(30)
n1.insert(8)
n1.insert(3)

print("inorder print")
n1.print_inorder()
n1.delete(8)
print("after delete")
n1.print_inorder()


# n1 = BSTNode(10)
# n2 = BSTNode(5)
# n3 = BSTNode(20)
