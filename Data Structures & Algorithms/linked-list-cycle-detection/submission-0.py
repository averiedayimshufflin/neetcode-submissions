# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
#UNDERSTAND:
Given: head
Return: true if cycle in linked list, otherwise false

note: cycle in linked list if at least one node in list can be visited again by following next pointer
index determined ind of beginning of cycle if it exists
- tial node of list will set next pointer to index-th node
- if index = -1 then tail node points to null and no cycle exists.

MATCH:
- linked list problem 

PLAN:
- make a set to keep track of each node
- while loop for as long curr is not null
- if node in set, return true
- outside while loop default reutrn false



'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        curr = head

        while curr is not None:
            if curr in node_set:
                return True
            
            node_set.add(curr)
            curr=curr.next
        
        return False
        