#https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from sys import maxsize
class Solution(object):
    def isValidBST(self, root):
        """
        Wrapper that calls validate function
        :type root: TreeNode
        :rtype: bool
        """

        max = maxsize
        min = -(maxsize)
        return self.validate(root,min,max)
    def validate(self, root, min, max):

        if root is None:
            return True

        if ((root.val<=min) or  (root.val>=max)):
            return False

        if not self.validate(root.left, min, root.val) or not self.validate(root.right, root.val, max):
            return False
        return True


x = TreeNode(1)
Solution().isValidBST(x)