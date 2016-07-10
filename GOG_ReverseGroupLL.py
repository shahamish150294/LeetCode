#http://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
class ListNode(object):
    def __init__(self, val, n = None):
        self.val = val
        self.next = n

class LinkedList(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        newNode = ListNode(data, self.root)
        self.root = newNode
        self.size += 1

    def reverseKGroup(self, head, k):

        curr = head
        temp = None
        prev = None
        count = 1

        #Code to reverse k nodes
        while (curr is not None and count <= k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1

        if temp:
            head.next = self.reverseKGroup(temp, k)

        return prev


    def printAll(self):
        currNode = self.root
        while currNode:
            print(currNode.val)
            currNode = currNode.next


myList = LinkedList()
myList.add(8)
myList.add(7)
myList.add(6)
myList.add(5)
myList.add(4)
myList.add(3)
myList.add(2)
myList.add(1)
myList.reverseKGroup(myList.root,3)
myList.printAll()