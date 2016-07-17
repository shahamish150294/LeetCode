#https://leetcode.com/problems/path-sum/
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        output = []
        return dfs(root,sum, output)


def dfs(root, sum, output):
    """
    This method works like dfs where the control backtracks when leaf is reached and sum is zero return true
    :param root: TreeNode
    :param output: TreeNode
    :return: TreeNode
    """
    if root is None:
        return False
    output.append(root.val)
    sum -= root.val

    if sum == 0 and root.left is None and root.right is None:

        output.pop()
        return True

    x = dfs(root.left, sum,output)

    y = dfs(root.right, sum,output)
    output.pop()
    if x: return x
    if y: return y

    return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(0)

a = Solution()
print a.hasPathSum(root,3)
