#https://leetcode.com/problems/minimum-depth-of-binary-tree/
from sys import maxsize
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #The first value in the height array will store the value of min height till a particular level
        if not root:
            return 0
        height = []
        height.append(maxsize)
        currHeight = 0
        self.calcDepth(root, currHeight,height)
        return height[0]

    def calcDepth(self,root, currHeight, height):
        """
        Visit node, increase the height. Visit left and right, if leaf then increase check with the local
        minimum if lesser then replace and decrease the height since it will backtraverse
        :param root:
        :param currHeight:
        :param height:
        :return:
        """
        if not root:
            return
        currHeight +=1

        self.calcDepth(root.left,currHeight,height)

        self.calcDepth(root.right, currHeight, height)

        if not root.left and not root.right and currHeight < height[0]:
            height[0] = currHeight

        currHeight -=1

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b

b.left = d
d.left = e
x= Solution()
print x.minDepth(a)