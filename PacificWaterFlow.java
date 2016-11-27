class Solution(object):

    """
    Initialize datastructures in this function to be used during DFS
    """
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        continent_touching_pacific = [[False for _ in range(n)] for _ in range(m)]
        continent_touching_atlantic = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):

            if not continent_touching_pacific[i][0]:

                self.dfs(i,0,matrix,continent_touching_pacific, matrix[i][0])

            if not continent_touching_atlantic[i][n-1]:

                self.dfs(i,n-1,matrix,continent_touching_atlantic, matrix[i][n-1])

        for i in range(n):

            if not continent_touching_pacific[0][i]:

                self.dfs(0,i,matrix,continent_touching_pacific, matrix[0][i])

            if not continent_touching_atlantic[m-1][i]:

                self.dfs(m-1,i,matrix,continent_touching_atlantic, matrix[m-1][i])

        results = []
        for i in range(len(continent_touching_pacific)):
            for j in range(len(continent_touching_pacific[0])):
                if continent_touching_pacific[i][j] and continent_touching_atlantic[i][j]:
                    each_results= [i,j]
                    results.append(each_results)

        return results

    def dfs(self, current_cell_row, current_cell_col, continent, continent_touching_ocean, prev_cell_height):

        if (continent[current_cell_row][current_cell_col] < prev_cell_height ):
            return

        continent_touching_ocean[current_cell_row][current_cell_col] = True

        if self.neighborsExist(current_cell_row+1, current_cell_col, continent) and not continent_touching_ocean[current_cell_row+1][current_cell_col]:
            self.dfs(current_cell_row+1, current_cell_col, continent, continent_touching_ocean, continent[current_cell_row][current_cell_col])
        if self.neighborsExist(current_cell_row-1, current_cell_col, continent)and not continent_touching_ocean[current_cell_row-1][current_cell_col]:
            self.dfs(current_cell_row-1, current_cell_col, continent, continent_touching_ocean, continent[current_cell_row][current_cell_col])
        if self.neighborsExist(current_cell_row, current_cell_col+1, continent)and not continent_touching_ocean[current_cell_row][current_cell_col+1]:
            self.dfs(current_cell_row, current_cell_col+1, continent, continent_touching_ocean, continent[current_cell_row][current_cell_col])
        if self.neighborsExist(current_cell_row, current_cell_col-1, continent) and not continent_touching_ocean[current_cell_row][current_cell_col-1]:
            self.dfs(current_cell_row, current_cell_col-1, continent, continent_touching_ocean, continent[current_cell_row][current_cell_col])

    def neighborsExist(self, current_cell_row, current_cell_col, continent):
        if current_cell_col >=0 and current_cell_col < len(continent[0]) and current_cell_row >=0 and current_cell_row < len(continent):
            return True

#Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5]])

# 1,2,2,3,5
# 3,2,3,4,4
# 2,4,5,3,1
# 6,7,1,4,5
# 5,1,1,2,4