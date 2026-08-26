#kth heaviest -> heap/pq



import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-n for n in stones]
        
        while len(maxheap)>1:
            
            heapq.heapify(maxheap)
            x=-maxheap[0]
            heapq.heappop(maxheap)
            heapq.heapify(maxheap)
            y=-maxheap[0]
            heapq.heappop(maxheap)
            if x < y:
                heapq.heappush(maxheap, -(y-x))
            elif x>y:
                heapq.heappush(maxheap,-(x-y))
        if maxheap:
            return -maxheap[0]
        else:
            return 0
        
            

            

        