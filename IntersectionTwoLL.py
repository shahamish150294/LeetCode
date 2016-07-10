#https://leetcode.com/problems/intersection-of-two-linked-lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        getIntersectionNode Gives the node at which two LL intersect
        :param headA:       Pass head of 1st LL
        :param headB:       Pass head of 2nd LL
        :return:            The node at which the LLs intersect
        """
        temp_headA = headA
        temp_headB = headB
        if headA is None or headB is None:
            return None

        # count nodes in listA

        countA = 0
        while temp_headA:
            temp_headA = temp_headA.next
            countA += 1

        # count nodes in listB
        countB = 0
        while temp_headB:
            temp_headB = temp_headB.next
            countB += 1

        diff = abs(countA - countB)

        headStart = 0

        if countA > countB:
            while headStart < diff:
                headA = headA.next
                headStart += 1

        if countB > countA:
            while headStart < diff:
                headB = headB.next
                headStart += 1

        # Parallel walk
        while headA and headB:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next

        return None