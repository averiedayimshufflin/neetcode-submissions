class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        window = set()
        for right, char in enumerate(s):
           
            if char in window:
               
                    
            
                while char in window:
                        
                    window.remove(s[left])
                    left+=1
                    

            window.add(char)
            if len(window) > best:
                best = len(window)
           
            
        
        return best

            