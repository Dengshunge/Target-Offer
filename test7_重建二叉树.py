# 面试题7 重建二叉树
'''
这道面试题采用了递归的方法，用python写只需要几行即可。
书上的大部分代码都是在检查边界条件，显得有些复杂。
这里参考了https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E9%87%8D%E5%BB%BA%E4%BA%8C%E5%8F%89%E6%A0%91.py
'''
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

# 非递归前序遍历
# 当p非空或stack非空时，输出p.data并将p压入stack，遍历左子树
# 当无左子树时，弹出stack，遍历该节点的右子树
def preOrder1(BinaryTreeNode):
    if BinaryTreeNode == None:
        return
    stack = []
    p = BinaryTreeNode
    while p != None or stack:
        while p != None:
            print(p.data,end=' ')
            stack.append(p)
            p = p.left
        if stack:
            p = stack.pop().right
    print()

def ConstructCore(preorder,inorder):
    if not preorder or not inorder:
        return None
    root = BinaryTreeNode(preorder[0])#根节点
    # 判断输入的两个序列是不是匹配
    if set(preorder) != set(inorder):
        return None
    i = inorder.index(root.data)
    root.left = ConstructCore(preorder[1:i+1],inorder[:i])
    root.right = ConstructCore(preorder[i+1:],inorder[i+1:])
    return root

if __name__ == '__main__':
    preorder = [1,2,4,7,3,5,6,8]
    inorder = [4,7,2,1,5,3,8,6]
    re_root = ConstructCore(preorder,inorder)
    preOrder1(re_root)
