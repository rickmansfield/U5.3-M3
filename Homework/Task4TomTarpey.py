def get_height(root):
    if root is None:
        return 0
    
    return max(get_height(root.left), get_height(root.right)) +1

def balanceBinaryTree(root):
    if root is None: 
        return True
    
    if abs(get_height(root.left) - get_height(root.right)) >1:
        return False
    
    return balanceBinaryTree(root.left) and balanceBinaryTree(root.right)