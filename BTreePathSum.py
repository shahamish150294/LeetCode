#https://leetcode.com/problems/path-sum-ii/
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        global outputs
        output = []
        outputs = []
        dfs(root,sum, output)
        return outputs

def dfs(root, sum, output):
    """
    This method works like dfs where the control backtracks when leaf is reached and sum is zero, add path and return
    :param root: TreeNode
    :param output: TreeNode
    :return: TreeNode
    """
    if root is None:
        return
    output.append(root.val)
    sum -= root.val

    if sum == 0 and root.left is None and root.right is None:
        # copy in final
        global outputs
        temp = []
        i = 0
        while i < len(output):
            temp.append(output[i])
            i += 1
        outputs.append(temp)
        output.pop()
        return

    dfs(root.left, sum,output)

    dfs(root.right, sum,output)
    output.pop()

    return

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(0)

a = Solution()
print a.pathSum(root,3)
