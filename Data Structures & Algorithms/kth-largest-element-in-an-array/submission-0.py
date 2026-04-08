import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsHeap = [-n for n in nums]
        heapq.heapify(numsHeap)

        for _ in range(k-1):
            heapq.heappop(numsHeap) 
        return -numsHeap[0]      