# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        if root is None:
            return 0
        return self.sumval(root,0)
    def sumval(self,root,current):
        if root is None:
            return 0
        current=current*10+root.val
        if root.left is None and root.right is None:
            return current
        return self.sumval(root.left,current)+self.sumval(root.right,current)
        