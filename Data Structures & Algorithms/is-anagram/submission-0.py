
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        firstWord=sorted(list(s))
        secondWord=sorted(list(t))

        for i in range(len(s)):
            if firstWord[i]!=secondWord[i]:
                return False
            
        return True
