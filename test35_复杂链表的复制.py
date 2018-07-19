# 面试题35 复杂链表的复制
'''
这道题有三种方法：
方法1：暴力解法，每次都遍历一遍，时间复杂度是O(n^2)
方法2：先将链表复制一遍，并将对应的节点存入hash表中，最后在构造pSibling，此方法的时间复杂度是O(n)，空间复杂度是O(n)
方法3：将需要复制的节点插入到原节点后面，然后构造pSibling，最后断开成2个链表，此时的时间复杂度是O(n)

用图形化的方式表示出来，会有助于我们理清思路。
'''

class ListNode:
    def __init__(self,data=None,pNext=None,pSibling=None):
        self.data=data
        self.pNext = pNext
        self.pSibling = pSibling

def CloneNodes(pHead):
    p = pHead
    while p:
        temp = ListNode(p.data,p.pNext)
        p.pNext = temp
        p = temp.pNext

def ConnectSiblingNodes(pHead):
    p = pHead
    while p:
        if p.pSibling:
            p_Clone = p.pNext
            p_Clone.pSibling = p.pSibling.pNext
        p = p.pNext.pNext

def ReconnectNodes(pHead):
    p1 = pHead
    p2 = pHead.pNext
    Clone_Node_Head =pHead.pNext
    while p1 and p2:
        p1.pNext = p2.pNext
        if not p2.pNext:
            break
        p2.pNext = p2.pNext.pNext
        p1 = p1.pNext
        p2 = p2.pNext
    return Clone_Node_Head

def Clone(pHead):
    if not isinstance(pHead,ListNode):
        return
    CloneNodes(pHead)
    ConnectSiblingNodes(pHead)
    return ReconnectNodes(pHead)

# 方法2  利用哈希表
def Clone_Hash(pHead):
    if not isinstance(pHead,ListNode):
        return
    p1 = pHead
    p2 = ListNode(p1.data)
    Hash = {p1:p2}
    p1 = p1.pNext
    Clone_Head = p2
    # 首先复制一个一样的链表，除了pSibling，并放入Hash表中
    while p1:
        p2.pNext = ListNode(p1.data)
        Hash[p1] = p2.pNext
        p1 = p1.pNext
        p2 = p2.pNext
    # 构建p2的pSibling
    p1,p2 = pHead,Clone_Head
    while p1:
        if p1.pSibling:
            p2.pSibling = Hash[p1.pSibling]
        p1 = p1.pNext
        p2 = p2.pNext
    return Clone_Head

def Print(pHead):
    if not isinstance(pHead,ListNode):
        return
    p = pHead
    while p:
        print(p.data,end=' ')
        p = p.pNext
    print()


node5 = ListNode('E')
node4 = ListNode('D',node5)
node3 = ListNode('C',node4)
node2 = ListNode('B',node3)
node1 = ListNode('A',node2)

node1.pSibling = node3
node2.pSibling = node5
node4.pSibling = node2


# p1 = Clone(node1)
# Print(p1)
p2 = Clone_Hash(node1)
print(p1.pSibling.data)
