# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
#UNDERSTAND:
Given: 2 heads -> sorted list
Return: one sorted list -> return head of new sorted linked list


#MATCH:
This is a linked list problem



#PLAN:
have a while loop -> two pointers for each list
have two while loops for each list where basically it would fill it in with whatever us keft
return the linked list

Edge cases:
- if either list is empty -> return other list




#IMPLEMENT:



#REVIEW:



#EVALUATE:
time complexity: O(n)
space complexity: O(1)? have to double check?

'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        curr = None
        curr1 = list1
        curr2 = list2
        newHead = None

        if list1.val <= list2.val:
            newHead = list1
            list1=list1.next

        else:
            newHead = list2
            list2=list2.next
         
        
        curr = newHead
        
        while list1 is not None and list2 is not None:
            
            if list1.val <= list2.val:
                
                curr.next = list1
                list1 = list1.next
            else:
                
                curr.next = list2
                list2 = list2.next
          
            curr=curr.next
        
        if list1 is not None:
            curr.next = list1
        
        if list2 is not None:
            curr.next= list2
        
        
        
        return newHead

        
        