#https://leetcode.com/problems/minimum-path-sum/
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #After  thinking about a recursive approach, I build a recursion tree. Realizing that
        #memoization is going to be difficult. I went for bottom-up approach

        #memo will store the minimum from (0,0) to (i,j)
        memo =[]
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n==1:
            return grid[m-1][n-1]
        #initialize the first col of the memo
        for i in range(0,m):
            row = [0] * (n)
            if i == 0:
                row[0] = grid[i][0]
            else:
                row[0] = memo[i-1][0] + grid[i][0]
            memo.append(row)

        #initialize the first row of the memo
        for i in range(1, n):
            memo[0][i] = memo[0][i-1] + grid[0][i]
        #Take the minimum of left, top and diagonally left-top and add with the cost to the memo at i,j

        for i in range(1, m):
            for j in range(1,n):
                if memo[i-1][j] < memo[i][j-1]:
                    memo[i][j] = grid[i][j] + memo[i-1][j]
                else:
                    memo[i][j] = grid[i][j] + memo[i][j-1]

        return memo[m-1][n-1]


grid = [[1,2,3,4],
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6],
        [7,8,9,9]]
grid2 = [[1,2],[1,1]]
print Solution().minPathSum(grid2)