class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val < l2.val:
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
            cur = head
            
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
            
        return head
