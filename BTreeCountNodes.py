#https://leetcode.com/problems/count-complete-tree-nodes/
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return BTreecountNodes(root)

def BTreecountNodes(root):
    """
    Get left and right height of the root, if equal calc no of nodes, if not go left get the count, go right get the count and sum the counts
    :param root: 
    :return:
    """
    if root is None:
       return 0
    left_height = getLeftHeight(root)
    right_height = getRightHeight(root)

    if left_height == right_height:
        return (2 << (left_height - 1)) - 1

    else:
        x = BTreecountNodes(root.left)
        y = BTreecountNodes(root.right)
    return x + y + 1

def getLeftHeight(root):
    if root is None:
        return 1
    height = 1
    while root.left:
        height += 1
        root = root.left

    return height

def getRightHeight(root):
    if root is None:
        return 1
    height = 1
    while root.right:
        height += 1
        root = root.right

    return height


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

a = Solution()
print a.countNodes(root)



