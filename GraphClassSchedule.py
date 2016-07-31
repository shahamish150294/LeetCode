class Solution(object):
    adj_list = {}
    result = []
    def findOrder(self, numCourses, prerequisites):

        #base case

        #create graph
        self.adj_list = {}
        self.result = []
        #add keys to list
        for i in range(0,numCourses):
            self.adj_list[i] = []

        for prerequisite in prerequisites:
            if not self.adj_list.has_key(prerequisite[0]):
                self.adj_list[prerequisite[0]] = []
            self.adj_list.get(prerequisite[0]).append(prerequisite[1])

        #DS req for topo sort
        visited = []
        visited = [False for i in range(0,numCourses)]
        stack = []

        keys = self.adj_list.keys()
        nocycle = False
        for key in keys:
            if not visited[key]:
                nocycle = self.topoSort(key, visited, stack)
                if not nocycle:
                    break

        if nocycle:
            while len(stack) > 0:
                self.result.insert(0,stack.pop())
        else:
            return []

        return self.result



    def topoSort(self,currentKey, visited, stack):

        visited[currentKey] = True

        neighbors = self.adj_list[currentKey]

        stack.append(currentKey)
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if stack.count(neighbor) > 0:
                    return False
                if not visited[neighbor]:
                    if not self.topoSort(neighbor, visited, stack):
                        return False
        if len(stack) > 0:
            self.result.append(stack.pop())
            return True

numCourses = 4
order =  [[1,0],[0,1],[3,1],[3,2]]
print Solution().findOrder(numCourses, order)
