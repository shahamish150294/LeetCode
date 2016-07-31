#https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    #Find nth Fib using recursion
    def fib(self, n):

        print self.calc(n-1)
        memo = [-1] * (n)
        memo[0] = 0
        memo[1] = 1
        print self.calcDP(n-1, memo)


    def climbStairs(self, n):
        """
        climbStairs calls climbDP which is memoization implementation. For recursive implementation, see climb()
        :param n: top
        :return: distinct ways stairs can be climbed
        """
        if n == 1:
            return 1
        if n ==2:
            return 2
        memo = [-1] * (n+1)
        memo[1] = 1

        memo[2] = 2
        return self.climbDP(n, memo)


    #This calculation of Fibonacci is without DP
    def calc(self, n):

        if n == 1:
            return 1

        if n==0:
            return 0

        return self.calc(n-1) + self.calc(n-2)

    def calcDP(self, n, memo):
        if memo[n] != -1:
            return memo[n]

        memo[n] = self.calc(n-1) + self.calc(n-2)
        return memo[n]

    def climb(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.climb(n-1) + self.climb(n-2)

    def climbDP(self, n, memo):
        if memo[n] != -1:
            return memo[n]

        memo[n] = self.climbDP(n-1, memo) + self.climbDP(n-2, memo)
        return memo[n]

print Solution().climbStairs(1)

