# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 首先进行判空
        if head == None:
            return head

        
        head_new = ListNode(1) # 定义哨兵节点
        head_new.next = head
        head = head.next
        head_new.next.next = None
        while head != None:
            temp = head_new.next
            head_new.next = head
            head = head.next
            head_new.next.next = temp

        return head_new.next
