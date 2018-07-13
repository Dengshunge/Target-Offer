# 面试题26 树的子结构
'''
树中的指针操作确实比链表的复杂挺多
虽然这道题的解题思路不难，但很考验编程能力

'''

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def HasSubtree(pRoot1, pRoot2):
    if not isinstance(pRoot1, TreeNode) or not isinstance(pRoot2, TreeNode):
        return False
    result = False
    if pRoot1 and pRoot2:
        if pRoot1.data == pRoot2.data:
            result = DoesTree1HaveTree2(pRoot1, pRoot2)
        if not result:
            result = HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = HasSubtree(pRoot1.right, pRoot2)
    return result


def DoesTree1HaveTree2(pRoot1, pRoot2):
    # 首先要明确的，如果从HasSubtree进入此函数，两指针都不会为空
    # 所以这里的空指针判断是自身迭代的结束条件
    # 当pRoot2为空的时候，说明遍历到了原来pRoot2的末尾，也就是上面的节点值都相等
    if not pRoot2:
        return True
    # 当pRoot2不空，而pRoot1为空，说明不相等
    if not pRoot1:
        return False
    if pRoot1.data != pRoot2.data:
        return False
    # 进行到此步，说明两节点的data是相等的，那就得比较左右子树
    return DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and DoesTree1HaveTree2(pRoot1.right, pRoot2.right)


if __name__ == '__main__':
    # 树1
    node1 = TreeNode(8)
    node2 = TreeNode(8)
    node3 = TreeNode(7)
    node4 = TreeNode(9)
    node5 = TreeNode(2)
    node6 = TreeNode(4)
    node7 = TreeNode(7)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node5.left, node5.right = node6, node7

    # 树2
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(2)

    node8.left, node8.right = node9, node10

    print(HasSubtree(node1, node8))
