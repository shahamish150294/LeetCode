#https://leetcode.com/problems/binary-tree-paths/
outputs = []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):
        global outputs
        output = []
        outputs = []
        self.dfs(root, output)

        return outputs

    def dfs(self, root, output):
        """
        This method works like dfs where the control backtracks when leaf is reached and when both the children are visited
        :param root: TreeNode
        :param output: TreeNode
        :return: TreeNode
        """
        if root is None:
            return
        output.append(root.val)

        if root.left is None and root.right is None:
            # copy in final
            global outputs
            temp = ""
            i = 0
            while i < len(output):
                temp += str(output[i])
                if (i < len(output) - 1):
                    temp += "->"
                i += 1
            outputs.append(temp)
            output.pop()
            return

        self.dfs(root.left, output)

        self.dfs(root.right, output)
        output.pop()

        return