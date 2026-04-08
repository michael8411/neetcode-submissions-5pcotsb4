import heapq

class Solution:

    def __init__(self):
        self.heap = []
        self.closest = []
        self.k = 0
       
        heapq.heapify(self.heap)

    def calcDist(self, point: List[int, int]):
        x1, y1 = 0, 0
        x2, y2 = point
        dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        dist_and_point = (dist, point)
        heapq.heappush(self.heap, dist_and_point)   
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for p in points:
            self.calcDist(p) 
        for _ in range(k):
            self.closest.append(heapq.heappop(self.heap)[1])
        return self.closest
 
        
        
     