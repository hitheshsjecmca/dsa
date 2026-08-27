from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        queue=deque([root])
        result=[]
        while queue:
            size=len(queue)
            for i in range(size):
                cur=queue.popleft()
                if i==size-1:
                    result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if(cur.right):
                    queue.append(cur.right)
        return result


        
        