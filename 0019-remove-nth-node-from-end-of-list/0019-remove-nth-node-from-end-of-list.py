# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        cur=head
        leng=0

        while cur:
            leng+=1
            cur=cur.next
        
        if leng==n:
            return head.next
        cur=head
        for i in range(leng-n-1):
            cur=cur.next
        cur.next=cur.next.next

        return head
        