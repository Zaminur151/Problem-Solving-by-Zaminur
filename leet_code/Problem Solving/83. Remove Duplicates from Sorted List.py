# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next # here we don't updated current cs we have again check the updated
                                                 # current.next by older current. it work for linked list (1,1,1,2)
                                                 # when it contains same number above 2 times
            else:
                current = current.next  

        return head