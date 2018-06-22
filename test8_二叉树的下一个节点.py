# 面试题8 二叉树的下一个节点
'''
此题的方法就是画图分析，三种情况：
    1.如果一个结点有右子树，则下一个节点就是它右子树的最左节点
    2.如果一个结点无右子树：
        a.当该节点是父节点的左子节点，则下一个节点就是父节点
        b.当该节点是父节点的右子节点，则需要向上遍历，至少找个一个是它父节点的左子节点的节点。
'''
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def inOrder1(BinaryTreeNode):
    if BinaryTreeNode == None:
        return
    stack = []
    p = BinaryTreeNode
    while p != None or stack:
        while p != None:
            stack.append(p)
            p = p.left
        if stack:
            s = stack.pop()
            print(s.data, end=' ')
            p = s.right
    print()

def GetNext(BinaryTreeNode):
    if BinaryTreeNode == None:
        return
    cur = BinaryTreeNode
    if BinaryTreeNode.right:
        cur = BinaryTreeNode.right
        while cur.left:
            cur = cur.left
        return cur
    elif cur == cur.parent.left:  # 若节点是父节点的左子树
        return BinaryTreeNode.parent
    else:  # 若节点是父节点的右子树
        while cur.parent.parent and cur.parent == cur.parent.parent.right:
            cur = cur.parent
        if not cur.parent.parent:
            return
        return cur.parent.parent


if __name__ == '__main__':
    n10 = BinaryTreeNode('i')
    n9 = BinaryTreeNode('h')
    n6 = BinaryTreeNode('g')
    n5 = BinaryTreeNode('f')
    n4 = BinaryTreeNode('e', left=n9, right=n10)
    n3 = BinaryTreeNode('d')
    n2 = BinaryTreeNode('c', left=n5, right=n6)
    n1 = BinaryTreeNode('b', left=n3, right=n4)
    root = BinaryTreeNode('a', left=n1, right=n2)
    n1.parent = root
    n2.parent = root
    n3.parent = n1
    n4.parent = n1
    n5.parent = n2
    n6.parent = n2
    n9.parent = n4
    n10.parent = n4
    inOrder1(root)
    x = GetNext(n6)
    print(x)
