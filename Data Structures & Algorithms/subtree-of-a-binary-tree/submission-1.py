# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(root1, root2) :
            if not root1 and not root2 :
                return True
            
            if not root1 or not root2 :
                return False
            
            if root1.val!=root2.val :
                return False
            
            return check(root1.left , root2.left) and check(root1.right, root2.right)
        
        def findNode(root, target):
            if not root:
                return False

            if root.val == target.val and check(root, target):
                return True

            return (findNode(root.left, target) or
            findNode(root.right, target))
        
        return findNode(root, subRoot)
