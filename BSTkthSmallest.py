#https://leetcode.com/problems/kth-smallest-element-in-a-bst/

found = False
val = 0
rank = 0

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :rtype: int
        """
        global rank
        rank = k+1
        BSTkthSmallest(root)
        global val
        return val

def BSTkthSmallest(root):
    """
    Once kth smallest is found method changes global val to root.val and traverses BST in in-order
    :param root: TreeNode
    :return:
    """
    if root is None:
        return

    #go left if  kth smallest not found
    global found
    if root and not found:
        BSTkthSmallest(root.left)
    global rank

    #found
    rank -= 1

    if rank == 1:
        global val
        val = root.val
        found = True

    # go right if  kth smallest not found
    if root and not found:
        BSTkthSmallest(root.right)

a = TreeNode(1)
b = TreeNode(8)
c = TreeNode(1)
d = TreeNode(10)
e = TreeNode(2)
f = TreeNode(15)
g = TreeNode(20)


a.right = e

print a.kthSmallest(a,2)

