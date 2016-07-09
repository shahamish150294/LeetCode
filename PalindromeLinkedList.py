#https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """

        :param head: Pass the start of the linkedlist as a parameter
        :return: Returns true if the linked list is a palindrome else returns false
        """
        if head is None:
            return True
        #Find middle
        hare , tort = head, head
        while hare.next and hare.next.next:
            tort = tort.next
            hare = hare.next.next
        # reverse second half
        ts, te = tort.next, None
        temp = None
        while ts:
            temp = ts.next
            ts.next = te
            te = ts
            ts = temp
        tort.next = te

        # p1 for start to mid and p2 for mid to end and check for palindrome
        p1 = head
        p2 = tort.next
        while p2 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next

        if p2 is None:
            return True
        else:
            return False
