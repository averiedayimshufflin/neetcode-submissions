'''
UNDERSTAND: 
Given: int arr nums,
Return: List[] output

MATCH: its an array problem

PLAN:
def productExceptSelf:
    have a prefix and suffix array to keep track of the multiplication before and after to prevent O(n^2) time complexity
    loop through all elements in the array
    utilize prefix and suffix array and just multiply all together to get result, most likely appending as you go

    return array
edge cases -> very large sets of numbers

EVALUATE:
time complexity: probably like O(n) because 3n but drop coefficients
space complexity: 3n but drop coefficient so O(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        result=[]
        

        for i in range(1,len(nums)):
            
            prefix.append(prefix[i-1]*nums[i-1])
        
        nums.reverse()
        for j in range(1,len(nums)):
            suffix.append(suffix[j-1]*nums[j-1])
        suffix.reverse()

        for r in range(len(nums)):
            result.append(suffix[r]*prefix[r])
          
 
        
        return result
        