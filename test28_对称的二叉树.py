# 面试题28 对称的二叉树
'''
对于二叉树的编程，感觉大多数都是采用了递归的方法
将一个大问题分解成很多个小问题解决

'''

class BinartTreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def isSymmetrical(Node):
    if not isinstance(Node, BinartTreeNode):
        return False
    return is_Symmetrical(Node,Node)

def is_Symmetrical(pRoot1,pRoot2):
    if not pRoot1 and not pRoot2:
        return True
    if not pRoot1 or not pRoot2:
        return False
    if pRoot1.data != pRoot2.data:
        return False
    return is_Symmetrical(pRoot1.left,pRoot2.right) and \
           is_Symmetrical(pRoot1.right,pRoot2.left)

def preOrder(root):
    if root:
        print(root.data,end=' ')
        preOrder(root.left)
        preOrder(root.right)

if __name__ == '__main__':
    node1 = BinartTreeNode(8)
    node2 = BinartTreeNode(6)
    node3 = BinartTreeNode(6)
    node4 = BinartTreeNode(5)
    node5 = BinartTreeNode(7)
    node6 = BinartTreeNode(7)
    node7 = BinartTreeNode(5)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5
    # node3.left,node3.right = node6,node7
    node3.left = node6

    preOrder(node1)
    print()

    print(isSymmetrical(node1))
