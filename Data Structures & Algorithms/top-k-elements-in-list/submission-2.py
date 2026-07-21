
'''
UNDERSTAND:
    Given: int array nums, int k
    Return: k most frequent elements within the array
MATCH
     This is an array problem

PLAN
     use a frequency map
     then loop through map to find greatest
     iterate through keys 
IMPLEMENT
REVIEW

EVALUATE


'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            if num not in map:
                map[num]=1
            elif num in map:
                map[num]=map.get(num)+1

        array = []
       
        for num, cnt in map.items():
            array.append([cnt,num])
            array.sort()

        res = []
        while len(res) <k:
            res.append(array.pop()[1])

        return res 
        


        