try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class Solution(object):
    itineraries = {}
    final_itenary = []
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.itineraries = {}
        self.final_itenary = []
        #Lets store keys in a dictionary
        #Instead of having a key value pair
        #Lets have a pair of key-(some DS that will retrieve value lexicographically). How about storing values in a PrioirtyQ



        for itinerary in tickets:
            if not (itinerary[0] in self.itineraries.keys()):
                self.itineraries[itinerary[0]] =  Q.PriorityQueue()

            self.itineraries.get(itinerary[0]).put(itinerary[1])

        self.travel("JFK")
        return self.final_itenary

    def travel(self, root):
        """
        Takes the first destination and travels by retrieving the root of the heap.
        :param root:
        """
        pqueue = self.itineraries.get(root)
        while pqueue and not pqueue.empty():
            self.travel(pqueue.get())

        self.final_itenary.insert(0,root)



tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Solution().findItinerary(tickets)


