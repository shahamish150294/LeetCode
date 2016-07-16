class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []
        if root is None:
            return 0
        return sumPath(root, nodes)

def sumPath(root, nodes):

    if root.left is None and root.right is None:
        nodes.append(root.val)
        #Get path's sum
        temp = getNum(nodes)
        print temp
        return temp
    x = 0
    if root:
        nodes.append(root.val)
    if root.left:

        x += sumPath(root.left,nodes)
        del nodes[-1]

    if root.right:

        x+=sumPath(root.right,nodes)
        del nodes[-1]

    return x


def getNum(nodes):
    temp_sum = 0
    for i in range(0,len(nodes)):
        temp_sum += nodes[i]* pow(10,(len(nodes)-i-1))

    return temp_sum

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.addLeft(b)
a.addRight(e)
b.addLeft(c)
b.addRight(d)

e.addRight(g)

print a.sumNumbers(a)



