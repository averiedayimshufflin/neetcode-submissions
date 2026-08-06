class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=deque([])
        substrings=[]
        for c in s:
            
            if c in window:
                substrings.append(len(window))
                
                while c in window:
                    window.popleft()
           
      
            window.append(c)
        
        if window:
            substrings.append(len(window))
               
       
        return max(substrings) if len(substrings)>0 else 0
        
            




        