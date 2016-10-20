class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from sys import maxsize
class Solution(object):
    def deleteNode(self, root, data):
        """
        case 1: Delete leaf
        case 2: Delete current node with one child
        case 3: Delete current node with two child
        """

        
    def findMin(self,root, minimum_array):
        if root:
            self.findMax(root.left, minimum_array)
            if minimum_array[0].val > root.val:
                minimum_array[0] = root
            self.findMax(root.right, minimum_array)

    def traverse(self, root):
        """
        Inorder traversal of BST
        """
        if root:
            self.traverse(root.left)
            print(root.val)
            self.traverse(root.right)


root = TreeNode(10)
root.left = TreeNode(1)
root.right = TreeNode(20)
root.left.right = TreeNode(5)
root.right.left = TreeNode(13)
root.right.right = TreeNode(30)
Solution().traverse(root)
