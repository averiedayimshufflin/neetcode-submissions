'''
UNDERSTAND: 
Given: arr of int ->
Return: length of the longest consecutive sequence of elements that can be formed

Note: that consecutive indicates that each element is 1 greater than previous, do not have to be conecutive in original array

MATCH:
I would consider this to be an array problem because we are working in an array and we could possibly use array methods in order to solve. It is a sliding window problem because the moment that we find longest or as we find it the window gets wider and if there is a point where it stops it clears the window and tries again

PLAN:
Since not consecutive in original array, this means that we could use sorted array -> probably with a lambda function in it to make it probably ascending.

O(n) because of how it is being sorted and its based on numbers and number of passes

return 



'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chicken = set(nums)
        
        longest = 0
        

        streak = 1
        for num in chicken:
            if (num-1) not in chicken:
                streak =1
                while(num+streak) in chicken:
                    streak+=1
                longest=max(longest,streak)
        return longest
        


        


                

        