'''
UNDERSTAND:
Given: string s
Return: true if palindrome, otherwise false
Notes:
- case-insensitive and ignores all non-alphanumeric characters
- no empty string
MATCH:
- Two pointer because you have to keep track of start and end
PLAN:
- Make pointer for start and end
- make for loop
- if at any point start and end diff, return false
- else return true
IMPLEMENT:

REVIEW:

EVALUATE:
time complexity = 
space complexity = 

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        s= s.replace(" ","")
     
        for c in s:
            if not c.isalnum():
               s = s.replace(c,"")
        s=s.lower()
        
        e_ptr=len(s)-1
        for i in range(len(s)-1):
            print(i)
            print(s[e_ptr])
            if s[i] !=s[e_ptr]:
                return False
            e_ptr-=1
        
        return True
        