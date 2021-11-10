# lets refactor the linked list node to be a doubly linked list node
class DLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


dl = DLLNode(10)

# None <- [10] -> None
