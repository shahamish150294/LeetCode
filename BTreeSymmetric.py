#https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True

        return checkForSymmetry(root,root)

def checkForSymmetry(root1, root2):
    """
    Method checks whether the current root values are same. If same, check (root1.left,root2.right) and check (root1.right,root2.left)
    :param root1: TreeNode
    :param root2: TreeNode
    :return: True if symmetric
    """

    if root1 is None and root2 is None:
        return True

    if root1 and root2 and root1.val == root2.val:
        return checkForSymmetry(root1.left, root2.right) and checkForSymmetry(root1.right, root2.left)

    return False
