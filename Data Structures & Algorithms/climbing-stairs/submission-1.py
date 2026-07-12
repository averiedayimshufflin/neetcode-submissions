'''
UNDERSTAND:
Given:
- int n -> represents num of steps to reach top
- Can climb with either 1 or 2 steps at a time
Return:
- distinct number of ways to climb a staircase 
MATCH:
- This is a 1-D dynamic programming problem
PLAN:
- 




'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1 or n==2:
            return n
        
        a,b=1,2
        for _ in range(3, n+1):
            curr=a+b
            a,b=b,curr

        return b


        