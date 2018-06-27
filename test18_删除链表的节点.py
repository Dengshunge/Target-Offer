# 面试题18 删除链表的节点


class Node:
    #单链表节点
    def __init__(self,data,p=None):
        self.data = data
        self.next = p
    def __del__(self):
        self.data = None
        self.next = None

class Link_List:
    def __init__(self):
        self.head = Node(None)

    def create(self,data):
        if len(data) == 0:
            print('list is null')
            return
        self.head.next = Node(data[0])
        p = self.head.next
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

    def print(self):
        p = self.head.next
        while p != None:
            print(p.data,end=' ')
            p = p.next
        print('')


#题目一 在O(1)时间内删除链表节点
def DeleteNode(LinkList,pToBeDeleted):
    if not isinstance(LinkList,Link_List) or not isinstance(pToBeDeleted,Node):
        return
    if pToBeDeleted.next != None:
        # 若删除的不是尾节点
        temp = pToBeDeleted.next
        pToBeDeleted.data = temp.data
        pToBeDeleted.next = temp.next
    elif LinkList.head.next == pToBeDeleted:
        # 若链表只有一个结点，删除头结点（也就是尾节点）
        LinkList.head.next = None
    else:
        # 若链表很多节点，删除尾节点
        p = LinkList.head.next
        while p.next != pToBeDeleted:
            p = p.next
        p.next = None


node1 = Node(10)
node2 = Node(11)
node3 = Node(13)
node4 = Node(15)
node1.next = node2
node2.next = node3
node3.next = node4

node5 = Node(17)

S = Link_List()
S.head.next = node1
S.print()
DeleteNode(S,node1)
S.print()

