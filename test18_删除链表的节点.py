# 面试题18 删除链表的节点
'''
题目1的关键在于如何在O(1)的时间内完成删除一个结点，即将后面结点的值赋予给该节点，然后删除后面的那个节点。
题目2是删除重复节点，难点在于想到各种边界条件。

'''

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

# 题目二 删除链表中重复的节点
def DeleteDuplication(LinkList):
    if not isinstance(LinkList,Link_List):
        return
    pPreNode , pNode = LinkList.head.next,LinkList.head.next # pNode指向第一个节点
    while pNode.next != None:
        if pNode.data != pNode.next.data:
            pPreNode = pNode
            pNode = pNode.next
        else:
            # 当数据重复了
            temp = pNode.data
            while pNode and pNode.data == temp:# 循环到不重复的值或者pNode为None
                pNode = pNode.next
            if pNode == None:# 当pNode指向空
                # 若数据是[1,1]这种头部重复的话，则直接令头指针指向空
                if pPreNode == None:
                    LinkList.head.next = None
                    return
                # 若数据是[1,2,2]这种尾部重复的话，则让pPreNode.next指向空
                else:
                    pPreNode.next = pNode
                    return
            # 尾部重复
            pPreNode.next = pNode




# 题目1
# node1 = Node(10)
# node2 = Node(11)
# node3 = Node(13)
# node4 = Node(15)
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
# node5 = Node(17)
#
# S = Link_List()
# S.head.next = node1
# S.print()
# DeleteNode(S,node1)
# S.print()

# 题目2
node1 = Node(1)
node2 = Node(1)
node3 = Node(3)
node4 = Node(3)
node5 = Node(4)
node6 = Node(5)
node7 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

S = Link_List()
S.head.next = node1
S.print()
DeleteDuplication(S)
S.print()

