#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node

    def zigzagLevelOrder(self, root):
        """
            ZigZag Level Order traversal which reverses prev level nodes and visits left and right according to ZigZag output
            :param root: TreeNode
            :return: List of lists of levels - zigzag
            """
        solution = []
        if root == None:
            return solution
        levelToProcess = [root]
        height = 1
        while len(levelToProcess) > 0:
            numbersLevel = []
            nextLevel = []

            if height%2 == 0:
                for temp in reversed(levelToProcess):
                    numbersLevel.append(temp.val)
                    if temp.right != None:
                        nextLevel.append(temp.right)
                    if temp.left != None:
                        nextLevel.append(temp.left)
            else:
                for temp in reversed(levelToProcess):
                    numbersLevel.append(temp.val)
                    if temp.left != None:
                        nextLevel.append(temp.left)
                    if temp.right  != None:
                        nextLevel.append(temp.right)

            height += 1
            solution.append(numbersLevel)
            levelToProcess = nextLevel
        return solution
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
f = TreeNode(6)
g = TreeNode(8)
a.addLeft(b)
a.addRight(c)

c.addLeft(d)
c.addRight(e)

b.addLeft(f)
b.addRight(g)
print a.zigzagLevelOrder(a);


