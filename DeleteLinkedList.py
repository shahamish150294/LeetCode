#https://leetcode.com/problems/delete-node-in-a-linked-list/
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp_data = node.next.val
        temp_next = node.next.next
        node.next.next = None
        node.next = temp_next
        node.val = temp_data