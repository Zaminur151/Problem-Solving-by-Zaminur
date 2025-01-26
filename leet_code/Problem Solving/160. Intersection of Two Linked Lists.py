class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista = headA
        listb = headB

        while lista != listb:
            if lista:              #lista = lista.next if lista else headB
                lista = lista.next
            else:
                lista = headB
            if listb:              #listb = listb.next if listb else headA
                listb = listb.next
            else:
                listb = headA
        
        return listb
    
    # there is something deep to understand

    
    