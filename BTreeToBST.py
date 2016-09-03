#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Method calls a recursive  function that builds a BST with lowest height
        :type nums: List[int]
        :rtype: TreeNode
        """
        a = len(nums)
        if a < 1:
            return None
        return self.createBST(nums, 0, a-1)

    def createBST(self, nums, start, end):
        """
        Keep dividing nums in two parts
        :param start:
        :param end:
        :return: root of BST
        """
        if end < start:
            return None
        mid = int((start+end)/2)
        #create a new node
        root =  TreeNode(nums[mid])
        root.left = self.createBST(nums, start,mid -1)
        root.right = self.createBST(nums, mid +1 ,end)
        return root

nums = [1,2,3,4,5,6]
print(Solution().sortedArrayToBST(nums))