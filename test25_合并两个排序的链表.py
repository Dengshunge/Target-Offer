# 面试题25 合并两个排序的链表
'''
书上用的是递归，代码更加简洁
但也能直接用循环
'''

class ListNode:
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next

def Merge(Node1,Node2):
    if not isinstance(Node1,ListNode) or not isinstance(Node2,ListNode):
        return None
    if not Node1.data:
        return Node2
    elif not Node2.data:
        return Node1

    pAnode,pBnode = Node1,Node2
    # 创建一个用于返回头指针的pHead，让其指向小的值
    if pAnode.data < pBnode.data:
        pHead = pAnode
        pAnode = pAnode.next
    else:
        pHead = pBnode
        pBnode = pBnode.next

    p1 = pHead# 此p1用于移动
    while pAnode and pBnode:
        if pAnode.data < pBnode.data:
            p1.next = pAnode
            pAnode = pAnode.next
        else:
            p1.next = pBnode
            pBnode = pBnode.next
        p1 = p1.next
    #当其中一个指针移动到最后的时候，补上另外一个指针
    if not pAnode:
        p1.next = pBnode
    else:
        p1.next = pAnode

    return pHead

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node4 = ListNode(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node5 = ListNode(2)
    node6 = ListNode(4)
    node7 = ListNode(6)
    node8 = ListNode(8)
    node5.next = node6
    node6.next = node7
    node7.next = node8

    pHead = Merge(node1,node5)
    while pHead:
        print(pHead.data,end=' ')
        pHead = pHead.next


