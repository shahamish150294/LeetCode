#https://leetcode.com/problems/binary-tree-level-order-traversal/
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]
    def printQueue(self):
        q = []
        for i in range(0,self.size()):
            if self.items[i] == "/":
                q.append(self.items[i])
        return q
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node



    def levelOrder(self,root):
        """
        Level Order traversal using queue and with help of delimiter "/" to mark as end of every level
        :param root: TreeNode
        :return: List of lists of levels
        """
        levels = []
        level = []
        if root is None:
            return levels
        q = Queue()
        q.enqueue(root)
        q.enqueue("/")
        level.append(root.val)
        levels.append(level)
        level = []
        height = 1
        while not q.isEmpty():
            x = q.dequeue()
            if x == "/" and not q.isEmpty():
                q.enqueue("/")
                levels.append(level)
                level = []
                height +=1

            if height%2==0:
                if type(x) is not str and x.left:
                    q.enqueue(x.left)
                    level.append(x.left.val)

                if type(x) is not str and x.right:
                    q.enqueue(x.right)
                    level.append(x.right.val)
            else:
                if type(x) is not str and x.right:
                    q.enqueue(x.right)
                    level.append(x.right.val)
                if type(x) is not str and x.left:
                    q.enqueue(x.left)
                    level.append(x.left.val)
            print height
            print q.printQueue()
        return levels
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)


a.addRight(c)
a.addLeft(b)
b.addLeft(d)
c.addRight(e)


print a.levelOrder(a);



