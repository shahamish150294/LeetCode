class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node

    def preorderTraversal(self, root):

        """
        Method defines a nodes list and calls preorder function
        :param root: Tree root
        :return: Pre-ordered traverse nodes
        """
        nodes = []
        preorder(root, nodes)
        return nodes

def preorder(root, nodes):
    """
    Method recurses to explore nodes in pre-order
    :param root: Tree root
    :param nodes: Pre-ordered traverse nodes
    :return: None
    """
    if root is None:
        return
    if root:
        nodes.append(root.val)
        preorder(root.left, nodes)
        preorder(root.right,nodes)

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
e.addLeft(f)
e.addRight(g)

print a.preorderTraversal(a)



