# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        ans = PolyNode()
        cur = ans
        while poly1 is not None and poly2 is not None:
            p = 0
            cof = 0
            if poly1.power > poly2.power:
                p = poly1.power
                cof = poly1.coefficient
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                p = poly2.power
                cof = poly2.coefficient
                poly2 = poly2.next
            else:
                p = poly2.power
                cof = poly2.coefficient + poly1.coefficient
                poly2 = poly2.next
                poly1 = poly1.next
            if cof == 0: continue
            cur.next = PolyNode(cof, p)
            cur = cur.next

        if poly1 is not None: cur.next = poly1
        if poly2 is not None: cur.next = poly2
        return ans.next