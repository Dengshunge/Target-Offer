# 面试题68 树中两个节点的最低公共祖先
'''
寻找树中两个节点的最低公共祖先，是一组题目。
当树是二叉搜索树的时候，最低祖先在两个节点的值的中间。
    当节点值都大于两个节点的值时，最低公共祖先在该节点的左子树上
    当节点值都小于两个节点的值时，最低公共祖先在该节点的右子树上
当树是普通的树的时候，而且有父母指针，可以将其转化成“两个链表中的以一个公共节点”

当树是普通的树的时候，而且没有父母指针。可以借助辅助空间。
    首先借助辅助空间，存储找到两个节点的路径，得到两个list
    然后将这两个list转化成“两个链表中的以一个公共节点”
    这样就能得到最低公共祖先了。
'''

class TreeNode:
    def __init__(self,data,left=None,right=None,parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def __init__(self,phead):
        self.phead = phead

    # 当树为二叉搜索树的情况
    def GetLowestNodeParent(self,node1,node2):
        if not node1 or not node2:
            return
        p = self.phead
        # 保证p1指向值小的节点，而p2指向值大的节点
        p1, p2 = node1, node2
        if p1.data > p2.data:
            p1, p2 = node2, node1

        while p.data > p2.data or p.data < p1.data:
            if p.data > p2.data:
                p = p.left
            else:
                p = p.right
        return p

    # 当树是普通的树，且有父母指针的时候
    def GetLowestNodeParent2(self,node1,node2):
        if not node1 or not node2:
            return
        p1,p2 = node1,node2
        while p1 != p2:
            p1 = p1.parent if p1.parent != None else node2
            p2 = p2.parent if p2.parent != None else node1
        return p1
    
node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(15)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(13)
node7 = TreeNode(17)
node8 = TreeNode(1)
node9 = TreeNode(4)
node10 = TreeNode(6)
node11 = TreeNode(9)
node12 = TreeNode(11)
node13 = TreeNode(14)
node14 = TreeNode(16)
node15 = TreeNode(19)

node1.left,node1.right = node2,node3
node2.left,node2.right = node4,node5
node3.left,node3.right = node6,node7
node4.left,node4.right = node8,node9
node5.left,node5.right = node10,node11
node6.left,node6.right = node12,node13
node7.left,node7.right = node14,node15

# 当树是二叉树
a = Solution(node1)
# print(a.GetLowestNodeParent(node1,node1).data)

# 当树是普通的树，且有父母指针的时候
node2.parent,node3.parent = node1,node1
node4.parent,node5.parent = node2,node2
node6.parent,node7.parent = node3,node3
node8.parent,node9.parent = node4,node4
node10.parent,node11.parent = node5,node5
node12.parent,node13.parent = node6,node6
node14.parent,node15.parent = node7,node7

print(a.GetLowestNodeParent2(node8,node9).data)
