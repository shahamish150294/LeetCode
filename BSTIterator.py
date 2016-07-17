#https://leetcode.com/problems/binary-search-tree-iterator/
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        #Put all lefts inside a stack
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return not len(self.stack) == 0

    def next(self):
        """ Pop each left node, add to final vector and  if it has a right node, go right. If it has a left node, push to stack
        :rtype: int
        """

        node = self.stack.pop()
        result = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node= node.left

        return result

root = TreeNode(8)
root.left= TreeNode(3)
root.left.left= TreeNode(1)
root.left.right= TreeNode(4)
root.left.right.right= TreeNode(7)

i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print v