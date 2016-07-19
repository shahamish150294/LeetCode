# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        inorderStart = 0
        inorderEnd = len(inorder) - 1
        preorderStart = 0
        preorderEnd = len(preorder) - 1
        return createTree(inorder, preorder, inorderStart, inorderEnd, preorderStart, preorderEnd)


def createTree(inorder, preorder, inorderStart, inorderEnd, preorderStart, preorderEnd):
    if inorderStart > inorderEnd or preorderStart > preorderEnd:
        return
    rootVal = preorder[preorderStart]
    root = TreeNode(rootVal)
    # find root in inorder array
    i = 0
    for k in range(0, len(inorder)):
        if rootVal == inorder[k]:
            i = k
            break

    root.left = createTree(inorder, preorder, inorderStart, i - 1, preorderStart + 1,
                           preorderStart + (i - inorderStart))
    root.right = createTree(inorder, preorder, i + 1, inorderEnd, preorderStart + (i - inorderStart) + 1, preorderEnd)
    return root
