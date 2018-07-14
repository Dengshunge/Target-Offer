# 面试题27 二叉树的镜像
'''
首先画图得出思路，然后用递归的方法，类似于前序遍历
'''

class BinartTreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def MirrorRecurisively(root):
    if not isinstance(root,BinartTreeNode):
        return None
    if root:
        root.left,root.right = root.right,root.left
        MirrorRecurisively(root.left)
        MirrorRecurisively(root.right)

def preOrder(root):
    if root:
        print(root.data,end=' ')
        preOrder(root.left)
        preOrder(root.right)


if __name__ == '__main__':
    node1 = BinartTreeNode(8)
    node2 = BinartTreeNode(6)
    node3 = BinartTreeNode(10)
    node4 = BinartTreeNode(5)
    node5 = BinartTreeNode(7)
    node6 = BinartTreeNode(9)
    node7 = BinartTreeNode(11)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5
    node3.left,node3.right = node6,node7

    preOrder(node1)
    print()

    MirrorRecurisively(node1)
    preOrder(node1)
    print()

