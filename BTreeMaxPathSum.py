#https://leetcode.com/problems/binary-tree-maximum-path-sum/
from sys import maxint
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def maxPathSum(self,root):
        max_sum = -(maxint)
        a = []
        a.append(max_sum)
        self.calcMaxPathSum(root,a)
        return a[0]

    def calcMaxPathSum(self,root, a):
        """

        :param root: TreeNode
        :return: int
        """
        if root is None:
            return 0

        left = self.calcMaxPathSum(root.left, a)
        right = self.calcMaxPathSum(root.right, a)

        curr_path = 0
        if root.val >0:
            if left>right:
                curr_path = left + root.val
            else:
                curr_path = right + root.val
        if  root.val <=0:
            if left >right:
                curr_path = left
            else:
                curr_path = right
        #You can do the above or the following
        #curr_path = max(max(left,right)+root.val, root.val)
        curr_subtree =  max(curr_path,root.val + left+right)
        if curr_subtree > a[0]:
            a[0] = curr_subtree

        return curr_path

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

x = Solution()
print x.maxPathSum(a)