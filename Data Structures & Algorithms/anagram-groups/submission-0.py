'''
#UNDERSTAND:
Given: array of strs
Return: group anagrams together into sublists. return output in any order

Note: anagram is str that contains exact same characters as another string,
but order of car can be different



#MATCH
- this is an arrays problem

#PLAN
- make a for loop and loop through each character
- make a set to make sure each str isnt repeated
- if in the set then move on to next one
- in successful condition, make a list and search through entire thing to see
- for each one u add, you add it to set



#IMPLEMENT



#REVIEW



#EVALUATE



'''



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = set()
        result = []
     
        for i in range(len(strs)):
            if strs[i] not in count:
                newArray = []
                for j in range(i, len(strs)):
                    if "".join(sorted(strs[i])) == "".join(sorted(strs[j])) :
                        newArray.append(strs[j])
                        count.add(strs[j])
                result.append(newArray)
        return result

        