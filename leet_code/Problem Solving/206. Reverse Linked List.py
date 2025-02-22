class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur,prev = head, None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
    
    # time and space complexity O(n)