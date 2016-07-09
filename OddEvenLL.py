#https://leetcode.com/problems/odd-even-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution(object):
    #Push all even nodes at the end
    #My approach takes two passes but constant space. Second pass to get the end of the original list.
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        if head is None:
            return head

        even = head.next
        last_even = even
        first_even = even
        prev = head

        while prev and prev.next:

            prev.next = even.next
            prev = prev.next

            if prev is None:
                break
            even = prev.next
            last_even.next = even
            last_even = last_even.next

        if last_even:
            last_even.next = None
        currNode = head
        #Go till the end of the original list
        while currNode.next:
            currNode = currNode.next
        currNode.next = first_even
        return head