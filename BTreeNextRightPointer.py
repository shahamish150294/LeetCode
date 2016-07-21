#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self,root):
        """

        :param root:
        :return:
        """

        # Initialize all the pointers
        if root is None:
            return
        #cH: head at current level
        currHead = None
        #cC: Current Node at current level
        currCurr = None
        #pC: Current Node at prev level
        prevCurr = None
        #pH: Head Node at prev level
        prevHead = root
        #Prev head will dominate. All the logic depends on prevHead. Hence, it will be outer
        while prevHead:
            #Every current will start from head
            prevCurr = prevHead
            #Till the current at prev level reaches the end of that level
            while prevCurr:
                 if prevCurr.left:
                     #IF the head is init and we know the position of cc. Just keep on going next and adding pointers
                      if currHead:
                            currCurr.next = prevCurr.left
                            currCurr = currCurr.next
                    #If the head of the current level is not init.
                      else:
                            currHead = prevCurr.left
                            currCurr = currHead

                 if prevCurr.right:
                      if currHead:
                            currCurr.next = prevCurr.right
                            currCurr = currCurr.next

                      else:
                          currHead = prevCurr.right
                          currCurr = currHead
                 #Move the current of prev level
                 prevCurr = prevCurr.next
            #current will become prev
            prevHead = currHead
            #Set head of the curr level to None so that it can be initialized
            currHead = None

a = TreeLinkNode(0)
x = Solution()
x.connect(a)