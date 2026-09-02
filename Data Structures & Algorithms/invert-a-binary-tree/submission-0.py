# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root or (not root.right and not root.left):
            print("e")
            return root
        if root.right and not root.left:
            root.left = self.invertTree(root.right)
            root.right = None
        elif root.left and not root.right:
            root.right = self.invertTree(root.left)
            root.left = None
        else:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
        
        return root
        
        
        