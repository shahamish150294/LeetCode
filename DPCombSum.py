#https://leetcode.com/problems/combination-sum-iv/
class Solution(object):
    count = 0
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        return self.subset (nums,target)
    def subset(self,nums,target):
        if target == 0:
            self.count +=1
            print self.count

        for i in range(len(nums)):
            if target -nums[i] < 0:
                return self.count
            self.subset(nums, target - nums[i])

        return self.count

nums= [6]
target = 4
print Solution().combinationSum4(nums,target)
