import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        x = -max_heap[0]    
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if y > x:
                heapq.heappush(max_heap, x - y)   
        if max_heap:
            return -max_heap[0]
        return 0
       # while len(max_heap) > 1:
        #     y = max_heap[0]
        #     left =  2 * -y + 1
        #     right = 2 * -y + 2
        #     if left > 5:
        #         remaining = False 

        #     print("left: ", left)
        #     print("right: ", right)
        #     max = left
        #     if left < len(max_heap) and max < max_heap[left]: 
        #         max = left  
        #     if right < len(max_heap) and max < max_heap[right]: 
        #         max = right    
        #     if max_heap:
        #         if y == max:
        #             heapq.heappop(max_heap)
        #             heapq.heappop(max_heap)
        #         if y < max:
        #             heapq.heappop(max_heap)
        #             max = y - max
        # return -max_heap[0]

