#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#Contains two methods to find LCA 1) Comparing paths 2) Single Traversal 
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #Boolean flags to check if both the nodes are present
        flag_array = [False, False]


        a = lowestCommonAncestorSingleTraversal(root,p,q,flag_array)

        if flag_array[0] and flag_array[1]:
            return a

        else:
            return None

    def lowestCommonAncestor2(self, root, p, q):
        """
        Method calls findPath method
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
            # findPath to first node
        stack1 = []
        findPath(root, p, stack1)

        # findPath to second node
        stack2 = []
        findPath(root, q, stack2)

        if len(stack1) == 0 or len(stack2) == 0:
            return

        i = 0
        while (i < len(stack1) and i < len(stack2)):
            if stack1[i] != stack2[i]:
                break
            i += 1
        return stack1[i - 1]


def findPath(root, dest, stack):

    if root is None:
        return False

    stack.append(root)
    if root is dest:
        return True

    #goLeft
    left = findPath(root.left,dest,stack)

    #goRight
    right = findPath(root.right, dest, stack)

    if left or right:
        return True

    if not left and not right:
        stack.pop()


def lowestCommonAncestorSingleTraversal(root,p,q,flag_array):
    flag = False
    #check if the root is null
    if root is None:
        return None

    if root.val is p.val:
        flag_array[0] = True
        flag = True

    if root.val is q.val:
        flag_array[1] = True
        flag = True
    left = lowestCommonAncestorSingleTraversal(root.left, p,q,flag_array)
    right = lowestCommonAncestorSingleTraversal(root.right,p,q,flag_array)

    if flag:
       return root
    if left and right is None:
       return left
    if right and left is None:
       return right

    if right and left:
       return root


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(3)
root.left.left = TreeNode(-2)
root.left.right = TreeNode(4)
#root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
a = TreeNode(9)
print root.lowestCommonAncestor2(root, root.left.left.left, root.left).val
