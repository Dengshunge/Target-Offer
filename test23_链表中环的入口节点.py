# 面试题23 链表中环的入口节点
'''
可以将该问题分解成3个小问题来解决
1.确定链表中是否包含环
2.确定环中结点数目
3.寻找环的入口

https://www.cnblogs.com/fankongkong/p/7007869.html
这篇文章介绍的方法类似于书上，但比书上的节点，其仅需要2步：
1.两指针相遇确定存在环
2.环内指针和指向头结点的指针同时移动，当两者相遇时，即是环的入口（不需要再次计算环内节点的数目）
原因是当slow和fast第一次相遇的时候，在环内的位置是x-y，所以当fast再次走y步的时候，刚好到达环内的入口。
'''

class ListNode:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

def MeetingNode(Node):
    if not isinstance(Node,ListNode) or not Node:
        return None
    pSlow = Node
    pFast = pSlow.next
    while pFast and pFast.next != None and pFast != pSlow:
        pSlow = pSlow.next
        pFast = pFast.next.next
    if not pFast or not pFast.next:
        return None

    return pFast

def EntryNodeOfLoop(Node):
    if not isinstance(Node,ListNode) or not Node:
        return None
    meetingNode = MeetingNode(Node)
    if not meetingNode:
        return None
    #统计环内节点数
    nodesInLoop = 1
    pNode1 = meetingNode
    while pNode1.next != meetingNode:
        pNode1 = pNode1.next
        nodesInLoop += 1
    # 开始寻找环的入口
    # 先让pNode2移动nodesInLoop次，然后pNode1和pNode2同时移动
    # 当两个指针相遇的时候，即是环的入口节点
    pNode2 = Node
    for i in range(nodesInLoop):
        pNode2 = pNode2.next
    pNode1 = Node
    while pNode1 != pNode2:
        pNode1 = pNode1.next
        pNode2 = pNode2.next
    return pNode1

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node2

    a = EntryNodeOfLoop(node1)
    print(a.data)

