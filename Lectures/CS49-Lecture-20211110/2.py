# lets make a linked list node
class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


l = LLNode(10)
l.next = LLNode(20)
l.next.next = LLNode(30)


# [10] -> [20] -> [30] -> None
