'''
UNDERSTAND:
Given: array of int nums, int target
Return: indicies i and j such nums[i]+nums[j]==target and i!=j

note: every input has exactly one pair of indiices i and j
return answer with smaller index 1st
MATCH:
This is a hashtable problem
PLAN:
1. create hash map
2. loop through the list
3. add to hash table as you go
4. if the target-num is in the hash table, then get indicies of current
and one in hashtabel and do

edge cases: numbers could be negative
IMPLEMENT:
Code it up


REVIEW:


EVALUATE:


'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numbers:
                return [numbers[complement], i]
            numbers[nums[i]] = i