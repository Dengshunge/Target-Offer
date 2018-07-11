# 面试题22 链表中倒数第k个节点
'''
寻找链表中倒数第k个节点，可以设置2个指针，让其中一个指针先走k-1步，
然后两个指针同时移动。当先走的指针到达了链尾的时候，慢走的指针就是指向倒数第k个节点。

当要寻找链表中的中间节点，同样是设置两个指针，同时从头节点出发，一个指针每次移动一步，另外一个指针每次移动两步。
这样移动慢的指针就会指向中间节点。

当用一个指针遍历链表不能解决问题的时候，可以尝试用两个指针来遍历链表。可以让其中一个指针遍历的速度快些。

'''

class ListNode:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

def FindKthToTail(Node,k):
    if not isinstance(Node,ListNode) or not Node:
        return
    if not isinstance(k,int) or k<= 0:
        return
    pAhead = Node
    pBhead = pAhead
    i = 0
    while i < k-1 and pBhead != None:
        pBhead = pBhead.next
        i += 1
    if pBhead == None:# 当k值过大时，pBhead会指向None
        return
    while pBhead.next != None:
        pAhead = pAhead.next
        pBhead = pBhead.next
    print(pAhead.data)

def List_Print(Node):
    while Node != None:
        print(Node.data,end=' ')
        Node = Node.next
    print()

def FindListMiddle(Node):
    if not isinstance(Node,ListNode) or not Node:
        return
    pAhead = Node
    pBhead = pAhead
    while pBhead and pBhead.next != None:# 当pBhead不指向空且下一个节点不为空的时候
        #pAhead每次走一步，pBhead每次走两步
        pAhead = pAhead.next
        pBhead = pBhead.next.next
    print(pAhead.data)


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

    List_Print(node1)

    FindKthToTail(node1,2)

    FindListMiddle(node1)
