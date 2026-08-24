class Solution:
    def isValid(self, s: str) -> bool:
        key = {")":"(","}":"{","]":"["}
        stack = []

        for i in s:
            print(i)
            if i not in key:
                stack.append(i)
            else:
                if stack and stack[-1]==key.get(i):
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        
        return True