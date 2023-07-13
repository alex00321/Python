class ListNode:
    def __init__(self, val):
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
    
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        thread = ListNode(-1)
        thread.next = head
        c = thread
        while c.next and c.next.next:
            a,b = c.next,c.next.next
            c.next,a.next = b,b.next
            b.next = a
            c = c.next.next
        return thread.next

if __name__ == "__main__":
    head = ListNode([1,2,3,4])
    sol = Solution()
    result = sol.swapPairs(head)
    print(result)

