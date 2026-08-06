class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result=[]
        for word in strs:
            hashed = ''.join(sorted(word))
            if hashed not in anagrams:
                anagrams[hashed]=[word]
                
            else:
                anagrams[hashed].append(word)
        
        for key in anagrams:
            result.append(anagrams[key])
        
        return result
