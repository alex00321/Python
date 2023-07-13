from typing import Optional
class ListNode:
    def __init__(self, val = None):
        if isinstance(val, int):
            self.val = val
            self.next = None
        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next
    def gatherAttrs(self):
        return ",".join("{}:{}".format(k,getattr(self,k)) for k in self.__dict__.keys())
    def __str__(self):
        return self.__class__.__name__+"{"+"{}".format(self.gatherAttrs())+"}"
"""
recursion
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry =0)->Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        carry += l1.val + (l2.val if l2 else 0)
        l1.val = carry%10        
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, carry//10)
        return l1
"""
class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) ->Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(carry%10)
            carry //=10
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
    
if __name__ == "__main__":
    l1 =ListNode([1,6,3])
    l2 =ListNode([4,5,6])
    sol = Solution()
    temp = sol.addTwoNumbers(l1,l2)
    print(temp)
