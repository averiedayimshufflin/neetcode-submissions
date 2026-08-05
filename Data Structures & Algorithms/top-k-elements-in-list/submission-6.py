'''
#UNDERSTAND:
Given: int array nums, int k
Return: k most frequent elements within the array.





#MATCH:

probably a frequncy map problem

#PLAN:
make a for loop and a frequency map
add one for the value every time the number is seen
when you pull from map if equal to biggest then add


#IMPLEMENT:

#REVIEW:

#EVALUATE:




'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        freq = {}
        result = []
        largest = 0
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
                
                if freq[num]> largest:
                    largest = freq[num]
        largest = freq[num]
        newdict = dict(sorted(freq.items(),key=lambda x: x[1],reverse=True))
        print(newdict)
        for key, value in newdict.items():
            print(key)
            if len(result)<k:
                result.append(key)
            else:
                return result

        
        return result


        

        