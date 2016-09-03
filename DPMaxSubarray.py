#https://leetcode.com/problems/maximum-subarray/
#from sys import maxint
class Solution(object):
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -maxint

        #Index through the given array assuming that max_subarray starts from each index

        for i in range(0,len(nums)):
            curr_sum = 0
            for j in range(i,len(nums)):
                curr_sum += nums[j]
                if max_sum <= curr_sum:
                    max_sum = curr_sum
                #Start with the next index if the curr_sum is negative
                elif curr_sum < 0:
                    break

        return max_sum

    def maxSubArray(self,nums):
        """
        Method calculates largest sum of a contiguous subarray using DP
        :param nums: integer array
        :return: largest sum
        """

        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1,len(nums)):
            if (curr_sum+nums[i] >= nums[i]):
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]

            if max_sum < curr_sum:
                max_sum = curr_sum

        return max_sum
n= [-2, -3, 4, -1, -2, 1, 5, -3]
print Solution().maxSubArray(n)