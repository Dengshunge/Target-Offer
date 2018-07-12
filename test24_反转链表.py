# 面试题24 反转链表
'''
设置三个指针
'''

class ListNode:
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next

def ReverseList(Node):
	pReversedHead = None # 用于返回的头结点
	pNode = Node
	pPrev = None # pNode之前的指针
	while pNode:
		pNext = pNode.next # pNode之后的指针
		if not pNext:
			pReversedHead = pNode
		pNode.next = pPrev
		pPrev = pNode
		pNode = pNext
	return pReversedHead

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
    pReversedHead = ReverseList(node1)

    while pReversedHead:
        print(pReversedHead.data,end=' ')
        pReversedHead = pReversedHead.next
