class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        res=[intervals[0]]
        prev = res[0]
        i=1
        while i <len(intervals):
          
            if prev[1]>=intervals[i][0]:
                start = prev[0]
                end = prev[1]
                if intervals[i][0]<prev[0]:
                    start = intervals[i][0]
                if intervals[i][1]>prev[1]:
                    end = intervals[i][1]
                res[-1]=[start,end]
            else:
                res.append(intervals[i])   
            i+=1
            prev=res[-1]
        return res                 
            
