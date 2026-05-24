# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy=ListNode(0)
        dummy.next=head
        groupprev=dummy

        while True:
            kth=groupprev

            for i in range(k):
                kth=kth.next

                if not kth:
                    return dummy.next
            
            groupnext=kth.next

        
            prev=groupnext
            curr=groupprev.next

            while curr!=groupnext:
                temp=curr.next

                curr.next=prev
                prev=curr
                curr=temp

            temp=groupprev.next

            groupprev.next=kth

            groupprev=temp

        