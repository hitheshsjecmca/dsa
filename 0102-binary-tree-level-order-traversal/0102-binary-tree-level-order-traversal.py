# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return[]
        result=[]
        queue=deque([root])

        while queue:
            l=[]
            lsize=len(queue)
            for i in range(lsize):
                current=queue.popleft()
                l.append(current.val)
                if current.left:
                    queue.append(current.left)
                if(current.right):
                    queue.append(current.right)
            result.append(l)
        return result
        