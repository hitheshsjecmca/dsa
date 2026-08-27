# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        result=[]
        path=[]
        def levelorder(root,path):
            if root is None:
                return None
            path.append(root.val)
            if root.left is None and root.right is None:
                result.append("->".join(map(str,path)))
            else:
                levelorder(root.left,path)
                levelorder(root.right,path)
            path.pop()
        levelorder(root,path)
        return result
        