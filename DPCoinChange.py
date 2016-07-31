#https://leetcode.com/problems/coin-change/
from sys import maxint
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        #memo to store minimum values: 0 through amount

        memo = [maxint] * (amount+1)
        memo[0] = 0

        for i in range(1,len(memo)):
            for j in coins:

                if  i>=j:
                    temp = memo[i-j]

                    if (temp != -1 and memo[i] > temp + 1):
                        memo[i] = temp + 1

        if memo[-1] == maxint:
            return -1
        else:
            return memo[-1]

print Solution().coinChange([2], 3)