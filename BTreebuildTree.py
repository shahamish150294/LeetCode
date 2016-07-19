#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        inorderStart = 0
        inorderEnd = len(inorder) - 1
        postorderStart = 0
        postorderEnd = len(postorder) - 1
        return createTree(inorder, postorder, inorderStart, inorderEnd, postorderStart, postorderEnd)


def createTree(inorder, postorder, inorderStart, inorderEnd, postorderStart, postorderEnd):

    if inorderStart > inorderEnd or postorderStart > postorderEnd:
        return
    #find root in inorder array
    i =0
    for k in range(0,len(inorder)):
        if postorder[postorderEnd] == inorder[k]:
            i = k
            break

    root = TreeNode(inorder[i])
    root.left= createTree(inorder,postorder, inorderStart, i - 1, postorderStart, postorderStart+(i-inorderStart)-1)
    root.right= createTree(inorder,postorder, i+1, inorderEnd, postorderStart+(i-inorderStart), postorderEnd - 1)

    return root

inorder = [-1]
postorder = [-1]
a = Solution()
print a.buildTree(inorder, postorder).val