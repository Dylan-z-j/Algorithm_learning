class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 定义结果数组
        shaobin = ListNode(-1)
        res = ListNode(-1)
        shaobin.next = res
        # 定义进位变量
        t = 0
        flag1 = 1
        flag2 = 1
        while flag1 == 1 or flag2 == 1 or t == 1:
            # ---------------------------------
            if flag1 == 1 and flag2 == 1:
                res.val = (l1.val + l2.val + t) % 10
                t = (l1.val + l2.val + t) // 10
                if l1.next == None:
                    flag1 = 0
                else:
                    l1 = l1.next
                if l2.next == None:
                    flag2 = 0
                else:
                    l2 = l2.next
                if flag1 + flag2 + t != 0:
                    res.next = ListNode()
                    res = res.next
                continue
            # ---------------------------------
            if flag1 == 1 and flag2 == 0:
                res.val = (l1.val +  t) % 10
                t = (l1.val + t) // 10
                if l1.next == None:
                    flag1 = 0
                else:
                    l1 = l1.next
                if flag1 + flag2 + t != 0:
                    res.next = ListNode()
                    res = res.next
                continue
            # ---------------------------------
            if flag1 == 0 and flag2 == 1:
                res.val = (l2.val +  t) % 10
                t = (l2.val + t) // 10
                if l2.next == None:
                    flag2 = 0
                else:
                    l2 = l2.next
                if flag1 + flag2 + t != 0:
                    res.next = ListNode()
                    res = res.next
                continue
            # ---------------------------------
            if flag1 == 0 and flag2 == 0:
                res.val = t
                t = 0
                continue
                
        return shaobin.next
