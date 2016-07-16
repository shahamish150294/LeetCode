#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root,p ,q ):
        """
        If p and q are less than root go left. If p and q are greater than root go right. If root is between p and q return root because
        root will be the LCA as you are traversing the tree from top and both nodes will be to the left and right of the root at that instance
        :param root: TreeNode
        :param p: TreeNode
        :param q: TreeNode
        :return: LCA TreeNode
        """

        if root is None:
            return

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


