# 面试题36 二叉搜索树与双向链表
'''
很常见的题目，里面涉及到大量的指针操作
原先指向左子节点的指针调整为链表中指向前一个节点的指针
原先指向右子节点的指针调整为链表中指向后一个节点的指针
'''

class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def Convert(pRoot):
    if pRoot == None:
        return None
    # 当是叶节点的时候，返回叶节点
    if not pRoot.left and not pRoot.right:
        return pRoot

    # 处理左子树
    Convert(pRoot.left)# 当第一次递归的时候，pRoot指向叶节点的父节点
    left = pRoot.left

    # 连接根与左子树最大结点
    if left:
        while left.right:
            left = left.right
        pRoot.left = left
        left.right = pRoot

    # 处理右子树
    Convert(pRoot.right)
    right = pRoot.right

    # 连接根与右子树最小结点
    if right:
        while right.left:
            right = right.left
        pRoot.right = right
        right.left = pRoot

    # 下面是为了返回给主程序使用的，由于这个程序中没有用Convert的值，所以会抛弃
    while pRoot.left:
        pRoot = pRoot.left

    return pRoot

pNode1 = TreeNode(10)
pNode2 = TreeNode(6)
pNode3 = TreeNode(14)
pNode4 = TreeNode(4)
pNode5 = TreeNode(8)
pNode6 = TreeNode(12)
pNode7 = TreeNode(16)

pNode1.left,pNode1.right = pNode2,pNode3
pNode2.left,pNode2.right = pNode4,pNode5
pNode3.left,pNode3.right = pNode6,pNode7

a = Convert(pNode1)
while a:
    print(a.data,end=' ')
    a = a.right
