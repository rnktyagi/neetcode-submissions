# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p=[]
        path_q=[]

        def findPath(root,val,path) :
            if not root:
                return False

            path.append(root)

            if root == val:
                return True

            if findPath(root.left, val, path):
                return True

            if findPath(root.right, val, path):
                return True

            path.pop()
            return False
        
        findPath(root, p, path_p)
        findPath(root, q , path_q)

        path_p.reverse()

        for node in path_p:
            if node in path_q:
                return node