# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
s -> 1 -> 2 -> 3 -> 4 -> None
適当にn1, n2を決めて、n3を予約しておきながら処理すればよさそう。
このとき、prevを覚えておくべきかな。
pesudoがあると良さそう

"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recurciveにしてもよさそうだが一旦愚直
        pesudo = ListNode()
        pesudo.next = head
        prev = pesudo
        n1 = head
        while n1 is not None:  # 偶数個終わりの場合
            if n1.next is None: break  # 終わりまで来た。奇数個の場合。
            n2 = n1.next
            n3 = n2.next  # 先読みをしておく
            prev.next = n2
            n2.next = n1
            n1.next = n3
            prev = n1
            n1 = n3  # 2つ単位なのでこういう飛ばし方をする
        return pesudo.next

