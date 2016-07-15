class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node

    def inorderTraversal(self, root):

        """
        Method defines a nodes list and calls inorder function
        :param root: Tree root
        :return: In-ordered traverse nodes
        """
        nodes = []
        inorder(root, nodes)
        return nodes

def inorder(root, nodes):
    """
    Method recurses to explore nodes in pre-order
    :param root: Tree root
    :param nodes: In-ordered traverse nodes
    :return: None
    """
    if root is None:
        return
    if root:
        inorder(root.left, nodes)
        nodes.append(root.val)
        inorder(root.right,nodes)


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

print a.inorderTraversal(a)



