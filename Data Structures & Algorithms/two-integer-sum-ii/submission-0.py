'''
#UNDERSTAND
Given: array of int -> sorted in non-decreasing order
Return: indices (1-indexed) of 2 numbers, add up to target number target and index1 <index2

Note: index1 and index 2 cannot be equal (cannot use same element)
always one valid solution

condition: must use O(1) additional space


#MATCH
- This is a two pointer problem because you can only use O(1) additional space


#PLAN
- have one pointer at the start and one pointer at the end 
- have first pointer move to one and then have the next pointer start at the index after that
the condition being a for loop for first pointer
- naother for loop for second pointer
- then if the first p and second p add up to target then return, otherwise continue

EDGE CASES:
- negative numbers


#IMPLEMENT



#REVIEW



#EVALUATE
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            for j in range (len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
        
        return None
        