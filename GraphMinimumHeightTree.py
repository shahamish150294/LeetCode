class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adj_list = {}
        for edge in edges:
            if not adj_list.has_key(edge[0]):
                adj_list[edge[0]] = []
            adj_list.get(edge[0]).append(edge[1])
            if not adj_list.has_key(edge[1]):
                adj_list[edge[1]] = []
            adj_list.get(edge[1]).append(edge[0])

        #Try to get all the leaves
        keys = adj_list.keys()
        leaves = []
        for key in keys:
            if len(adj_list.get(key)) == 1:
                leaves.append(key)
        newleaves = []

        while (n > 2):
            n -= len(leaves)
            for leaf in leaves:
                #Following commented code gave time limit exceeded
                # # remove that key and its value.
                # del adj_list[leaf]
                #
                # #remove the key which is a neighbor of some other node
                # for node in adj_list.keys():
                #     neighbors = adj_list.get(node)
                #     if neighbors.count(leaf) > 0:
                #         neighbors.remove(leaf)
                #         # Also check if the node under consideration will be new leaf
                #         if len(neighbors) == 1:
                #             newleaves.append(node)
                neighbor = adj_list.get(leaf)
                x= neighbor.pop()
                adj_list.get(x).remove(leaf)
                if len(adj_list.get(x)) == 1:
                    newleaves.append(x)

            leaves = newleaves
            newleaves = []

        return leaves
#
# edges = [[0,3],[1,3],[2,3],[3,8],[8,10],[10,9],[6,5],[8,6]]
# n = 9
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
n = 6

print Solution().findMinHeightTrees(n,edges)