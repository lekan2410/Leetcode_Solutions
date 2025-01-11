class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head

        h = set()

        while cur != None:
            if cur in h:
                return True
            h.add(cur)

            cur = cur.next
        return False

