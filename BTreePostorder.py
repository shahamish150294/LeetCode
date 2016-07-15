class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node

    def postorderTraversal(self, root):

        """
        Method defines a nodes list and calls postorder function
        :param root: Tree root
        :return: Post-ordered traverse nodes
        """
        nodes = []
        postorder(root, nodes)
        return nodes

def postorder(root, nodes):
    """
    Method recurses to explore nodes in pre-order
    :param root: Tree root
    :param nodes: Post-ordered traverse nodes
    :return: None
    """
    if root is None:
        return
    if root:
        postorder(root.left, nodes)
        postorder(root.right,nodes)
        nodes.append(root.val)

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

print a.postorderTraversal(a)



