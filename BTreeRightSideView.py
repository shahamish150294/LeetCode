# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        view = []
        height = -1
        if not root:
            return view
        self.fromRight(root,height, view)
        return view

    def fromRight(self,root, height, view):
        if not root:
            return

        height += 1
        if height > len(view)-1:
            view.append(root.val)
        else:
            view[height] = root.val

        self.fromRight(root.left,height,view)
        self.fromRight(root.right, height, view)

        height -= 1

        return

a= TreeNode(1)
b= TreeNode(2)
c= TreeNode(3)
d= TreeNode(4)
e= TreeNode(5)
f= TreeNode(6)
g= TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
print Solution().rightSideView(a)

