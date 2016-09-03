from sys import maxint
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        #Store prev longest LIS in memo
        memo = [1] * (len(nums)+1)
        j = 0

        for i in range(1,len(nums)):
            longest_length = -maxint
            while j < i:
                if nums[j] < nums[i]:
                    if longest_length < memo[j]:
                        longest_length = memo[j]
                j += 1
            if longest_length != -maxint:
                memo[j] = 1+longest_length
            j = 0

        max_length = 1
        for i in memo:
            max_length = max(max_length, i)

        return max_length
print Solution().lengthOfLIS([10, 22])


