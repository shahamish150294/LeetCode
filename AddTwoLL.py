#https://leetcode.com/problems/add-two-numbers/

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

    def addTwoNumbers(self,l1, l2):
        """
        Given two LL, l1 and l2 add the LL in reverse order
        :param l1:  l1 is the head of 1st LL
        :param l2:  l2 is the head of 2nd LL
        :return:    Returns the head of the new LL that represents the sum
        """
        headA = l1.root
        headB = l2.root

        if headA is None:
            headA = ListNode(0)

        if headB is None:
            headB = ListNode(0)

        carry = 0
        firstC = None
        count = 0
        #Loop to traverse the list till the same number of digits
        while headA and headB:
            currsum = headA.val + headB.val
            currsum += carry
            carry = currsum / 10
            currsum %= 10
            if count == 0:
                headC= ListNode(currsum)
                firstC =headC
            else:
                temp_headC = ListNode(currsum)
                headC.next = temp_headC
                headC = headC.next
            headA = headA.next
            headB=headB.next
            count += 1
        #If L1 is still left to traverse
        while headA:
            currsum = headA.val
            currsum += carry
            carry = currsum / 10
            currsum %= 10
            temp_headC = ListNode(currsum)
            headC.next = temp_headC
            headC = headC.next
            headA = headA.next
        # If L2 is still left to traverse
        while headB:
            currsum = headB.val
            currsum += carry
            carry = currsum / 10
            currsum %= 10
            temp_headC = ListNode(currsum)
            headC.next = temp_headC
            headC = headC.next
            headB = headB.next

         #Create a new node to add carry, if any
        if carry>0:
            temp_headC = ListNode(carry)
            headC.next = temp_headC
            headC = headC.next



        return firstC


    def printAll(self):
        currNode = self.root
        while currNode:
            print(currNode.val)
            currNode = currNode.next
myList = LinkedList()
myList2 = LinkedList()
myList2.add(9)
myList2.add(9)
myList2.add(9)
myList2.add(9)



myList.addTwoNumbers(myList, myList2)

