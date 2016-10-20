# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    count = 0
    def lastKthNode(self, head, k):

        if head is None:
            return None

        temp = self.lastKthNode(head.next, k)
        self.count +=1
        if self.count == k:
            return head
        return temp

a = ListNode(1)

b = ListNode(2)

c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

e.next =f
d.next=e
c.next=d
b.next=c
a.next=b
print(Solution().lastKthNode(a,1).val)
