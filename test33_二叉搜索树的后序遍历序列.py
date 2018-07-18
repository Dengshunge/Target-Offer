# 面试题33 二叉搜索树的后序遍历序列
'''
对于大部分二叉树的题目，都是用递归解决
这道题先分析出规律，通过规律来写代码，这样就简单很多

'''

def VerifySquenceOfBST(sequence):
    if not sequence:
        return False
    root = sequence[-1]
    length = len(sequence)
    # 左子树
    i = 0
    while i < length - 1:
        if sequence[i] > root:
            break
        i += 1
    # 右子树
    j = i
    while j < length - 1:
        if sequence[j] < root:
            return False # 当右子树中某个值小于root时，说明不存在该二叉搜索树
        j += 1
    # 判断左子树是不是二叉搜索树
    left = True
    if i > 0: # 当进行到此步，说明sequence不为空，当数组的元素只有1个的时候，不进入判断，返回的left为True
        left = VerifySquenceOfBST(sequence[:i])
    # 判断右子树是不是二叉搜索树
    right = True
    if i < length - 1:
        right = VerifySquenceOfBST(sequence[i:length-1])
    return left and right

lis = [5,7,6,9,11,10,8]
lis2 = [7,4,6,5]
print(VerifySquenceOfBST(lis))
