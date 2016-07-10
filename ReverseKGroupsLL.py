# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):

        first_of_first = ListNode(0)
        pre = first_of_first
        pre.next = head
        curr = head
        count = 0

        while curr:
            count += 1
            if count % k == 0:
                pre = self.reverse( pre, curr.next)
                curr = pre.next
            else:
                curr = curr.next

        return first_of_first.next

    def reverse(self, prev_of_first, next_of_last):

        first = prev_of_first.next
        next = first.next

        while next is not next_of_last:
            first.next = next.next
            next.next = prev_of_first.next
            prev_of_first.next = next
            next = first.next
        return first    