#https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Reverse a linked list from position m to n. Do it in-place and in one-pass.
    def reverseBetween(self, head, m, n):
        """
        :type head: Send the first node of the LL
        :type m: int Start index from where to reverse
        :type n: int End index from where to reverse
        :rtype: ListNode Returns the head of the new LL
        """
        counter = 1;
        curr = head
        prev =None
        #Reach to starting index. Save the prev and curr
        while counter<m:
            prev = curr
            curr = curr.next
            counter += 1

        first = curr
        last = curr
        curr = curr.next

        count = n - m
        #Run the reverse code n-m times
        counter = 1
        while counter <= count:

            temp = curr.next
            curr.next = last
            last = curr
            curr = temp
            counter += 1
        #To take care if m = 1
        if prev:
            #Attach head of the reversedLL to Original LL
            prev.next = last
        else:
            head = last
        #Attach tail of the reversedLL to Original LL
        first.next = curr
        return head