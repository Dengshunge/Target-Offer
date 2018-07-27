# 面试题52 两个链表的第一个公共节点
'''
方法一：暴力解法，遍历链表A，在遍历的同事，查看每个链表A中的节点是否在链表B中，时间复杂度是O(mn)
方法二：利用两个辅助栈，分别压入两个量表，然后弹出，比较弹出的元素，时间复杂度是O(m+n),空间复杂度是O(m+n)
方法三：首先获得两个链表的长度，让长的链表先走“两链表长度之差”步，让他们相遇的时候，就是公共节点
方法四，让链表A接到链表B的尾部，组成环，接下来就是面试题23的方法，A每次走1步，B每次走2步，相遇的时候，让A回到起点，两指针
    再一起移动，再次相遇的时候，就是公共节点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法2
class Solution2:
    # 这种方式没有完全通过牛客网
    # 是边界条件没调好，不确定是哪个边界条件
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        if pHead1 == pHead2:
            return pHead1
        stack1, stack2 = [], []
        p1,p2 = pHead1,pHead2
        while p1:
            stack1.append(p1)
            p1 = p1.next
        while p2:
            stack2.append(p2)
            p2 = p2.next
        p1, p2 = stack1.pop(), stack2.pop()
        while stack1 and stack2 and p1 == p2:
            p1, p2 = stack1.pop(), stack2.pop()
        return p1.next

class Solution3:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 and not pHead2:
            return None
        nLength1 = self.GetListLength(pHead1)
        nLength2 = self.GetListLength(pHead2)
        nLengthDif = abs(nLength2 - nLength1)

        pListNodeLong,pListNodeShort = pHead1,pHead2
        if nLength1 < nLength2:
            pListNodeLong, pListNodeShort = pHead2, pHead1

        for i in range(nLengthDif):
            pListNodeLong = pListNodeLong.next

        while pListNodeLong and pListNodeShort and pListNodeLong != pListNodeShort:
            pListNodeLong = pListNodeLong.next
            pListNodeShort = pListNodeShort.next

        return pListNodeLong

    def GetListLength(self,pHead):
        i = 0
        p = pHead
        while p:
            i+=1
            p = p.next
        return i

class Solution3_1:
    # 这种方法不需要计算链表的长度，是上一种方法的改进
    # 当两链表一样长的时候，它们的公共节点的数目是一样，所以此时大家一起前进，会有p1==p2的情况
    # 当两链表不等长的时候，当短的链表走完的时候，它会重新指向长的链表，然后当长的链表走完的时候，会指向短的链表。
    # 此时，两链表到公共节点的距离就相等了。
    # 因为当短链表走完时，两指针之间的差值就相当于上面的nLengthDif
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        while p1!=p2:
            p1 = p1.next if p1!=None else pHead2
            p2 = p2.next if p2!=None else pHead1
        return p1

# 方法四
class Solution4:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1 = pHead1
        pend = p1
        # 把p2接到p1后面
        while p1.next:
            p1 = p1.next
        pend = p1
        p1.next = pHead2

        p1 = pHead1.next
        p2 = p1.next
        if not p2:
            return None
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if p2:# 这步是防止p2下一个为空指针
                p2 = p2.next

        if p1 != p2:
            return None
        p1 = pHead1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        pend.next = None
        return p1

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node1.next=node2
node2.next=node3
node3.next=node6
node6.next=node7
node4.next=node5
node5.next=node6

a2 = Solution2()
b = a2.FindFirstCommonNode(node1,node4)
print(b)


