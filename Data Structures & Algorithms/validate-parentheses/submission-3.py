'''
#UNDERSTAND
Given: string s 
Return: true if fufills conidition, false otherwise
#MATCH
Stack problem because you can use it to see which ones are in consecutive order
#PLAN
- make a dict of the symbols
- while loop: condition is as long as it is not empty
- if  in the map, right hand, then put in stack
-pops for next if not in map or and if so then it will check to see if it is same or not
#IMPLEMENT

#REVIEW


#EVALUATE
'''


class Solution:
    def isValid(self, s: str) -> bool:
        set = { ")":"(","}":"{","]":"[" }
        stack=[]

        for c in s:
            if c in set:
                if stack and stack[-1] ==set[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        