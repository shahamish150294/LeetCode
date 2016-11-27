class Node(object):
    element_number = None
    parent = None
    rank = None

class DisjointSet(object):

    nodeMapper = {}

    #Create a map of all the elements of 2d array pos [0][0] is map<0, Node(i,n,0)>
    def makeSet(self, totalsize):
        for i in range(totalsize):
            n = Node()
            n.element_number = i
            n.parent = n
            n.rank = 0
            self.nodeMapper[i]  = n

    #Take union of two sets
    def unionSet(self, i, j):
        currentNode1 = self.nodeMapper[i]
        primaryNode1 = self.findSet(currentNode1)

        currentNode2 = self.nodeMapper[j]
        primaryNode2 = self.findSet(currentNode2)
        if primaryNode1.element_number == primaryNode2.element_number:
            return False
        if primaryNode1.rank >= primaryNode2.rank:
             if (primaryNode1.rank == primaryNode2.rank):
                 primaryNode1.rank = primaryNode1.rank +1
             else:
                 primaryNode1.rank = primaryNode1.rank
             primaryNode2.parent = primaryNode1
        else:
             primaryNode1.parent = primaryNode2

        return True

    #Find to which set the node belongs to
    def findSet(self, currentNode):

        parentNode = currentNode.parent
        if parentNode == currentNode:
            return parentNode

        return self.findSet(currentNode.parent)

    #To print the nodeMapper. Used for debugging purposes
    def printSets(self):
        for i in self.nodeMapper.keys():
            print( i, "values", self.findSet(self.nodeMapper[i]).element_number)

class Solution(object):
    #Number of Islands using BFS
    def numIslands_bfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        input = grid
        grid = []
        for x in (input):
            list_of_numbers_string = list(x)
            list_of_numbers_int = []
            for each_number in list_of_numbers_string:
                if each_number == '0':
                    list_of_numbers_int.append(0)
                if each_number == '1':
                    list_of_numbers_int.append(1)
            grid.append(list_of_numbers_int)

        visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        queue = []

        #Use BFS
        #Get first 1 in the grid
        row = len(grid)
        col = len(grid[0])
        count = 0
        for x in range(0,row):
            for y in range(0,col):
                if grid[x][y] == 1 and not visited[x][y]:
                    count +=1
                    element = [x,y]
                    queue.append(element)

                    while queue:
                        i = queue[0][0]
                        j = queue[0][1]
                        queue.pop(0)
                        visited[i][j] = True

                        if self.neighborExists(i-1,j,row,col) and grid[i-1][j] == 1 and not visited[i-1][j]:
                            queue.append([i-1,j])

                        if self.neighborExists(i+1,j,row,col) and grid[i+1][j] == 1 and not visited[i+1][j]:
                            queue.append([i+1,j])

                        if self.neighborExists(i,j+1,row,col) and grid[i][j+1] == 1 and not visited[i][j+1]:
                            queue.append([i,j+1])

                        if self.neighborExists(i,j-1,row,col) and grid[i][j-1] == 1 and not visited[i][j-1]:
                            queue.append([i,j-1])

        return count
    def neighborExists(self, i,j , row, col):
        if (i >= 0 and j>=0 and i<row and j < col):
            return True

    #Using disjoint sets
    def numIslands(self,grid ):
        if len(grid) == 0:
            return 0
        input = grid
        grid = []
        for x in (input):
            list_of_numbers_string = list(x)
            list_of_numbers_int = []
            for each_number in list_of_numbers_string:
                if each_number == '0':
                    list_of_numbers_int.append(0)
                if each_number == '1':
                    list_of_numbers_int.append(1)
            grid.append(list_of_numbers_int)

        rows = len(grid)
        cols = len(grid[0])

        dSet = DisjointSet()
        dSet.makeSet(rows * cols)

        position = 0
        index = []
        for i in range(rows):
            indices = []
            for j in range(cols):
                indices.append(position)
                position +=1
            index.append(indices)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue

                if self.neighborExists(i-1,j, rows,cols) and grid[i-1][j] == 1:
                    dSet.unionSet(index[i-1][j], index[i][j])

                if self.neighborExists(i+1,j, rows,cols) and grid[i+1][j] == 1:
                    dSet.unionSet(index[i+1][j], index[i][j])

                if self.neighborExists(i,j-1, rows,cols) and grid[i][j-1] == 1:
                    dSet.unionSet(index[i][j-1], index[i][j])

                if self.neighborExists(i,j+1, rows,cols) and grid[i][j+1] == 1:
                    dSet.unionSet(index[i][j+1], index[i][j])

        return (self.countTheIslands(rows,cols, grid, index, dSet))

    def countTheIslands(self, rows, cols, grid, index, dSet):
        unique_points = []
        for i in range(len(index) * len(index[0])):
            unique_points.append(0)



        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 1):
                    #First find the index[i][j] which is the position in map, look for that position in map. Find to what set that particular node belongs to using findSet. What is that elements value and update the unique_points array
                    unique_points[dSet.findSet(dSet.nodeMapper[index[i][j]]).element_number]+=1

        number_of_islands =0
        for i in unique_points:
            if i >0:
                number_of_islands +=1

        return number_of_islands


print(Solution().numIslands(["11000","11000","00100","00011"]))
print(Solution().numIslands(["11111011111111101011","01111111111110111110","10111001101111111111","11110111111111111111","10011111111111111111","10111111011101110111","01111111111101101111","11111111111101111011","11111111110111111111","11111111111111111111","01111111011111111111","11111111111111111111","11111111111111111111","11111011111110111111","10111110111011110111","11111111111101111110","11111111111110111100","11111111111111111111","11111111111111111111","11111111111111111111"]))


