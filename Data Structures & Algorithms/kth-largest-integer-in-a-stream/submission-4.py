#heap, no brute force?
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k

        self.nums=[-n for n in nums]
        heapq.heapify(self.nums)
       

    def add(self, val: int) -> int:
        print(self.nums)
        heapq.heappush(self.nums,-val)
        heapq.heapify(self.nums)
        kth_largest=0
        temp = []
        for i in range(self.k):
            temp.append(-heapq.heappop(self.nums))
            kth_largest=temp[-1]
            heapq.heapify(self.nums)
        
        for j in range(len(temp)):
            heapq.heappush(self.nums,-temp[j])
        temp.clear()
        
        
        return kth_largest


        
