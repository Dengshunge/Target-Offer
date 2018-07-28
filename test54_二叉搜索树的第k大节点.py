# 面试题54 二叉搜索树的第k大节点
'''
题目应该改成“二叉搜索树的第k个节点”
首先是二叉搜索树，是有序的，所以根据中序遍历，就能到第K个节点

不过值得注意的是一些python的语法
变量是值传递，不可变对象，所以想要改变，可以将其放入一个list里面
而list是地址传递，list是可变对象

因为Python对象分为可变对象(list,dict,set等)和不可变对象(number,string,tuple等)，
当传递的参数是可变对象的引用时，因为可变对象的值可以修改，因此可以通过修改参数值而修改原对象，这类似于C语言中的引用传递；
当传递的参数是不可变对象的引用时，虽然传递的是引用，参数变量和原变量都指向同一内存地址，但是不可变对象无法修改，
所以参数的重新赋值不会影响原对象，这类似于C语言中的值传递。
https://blog.csdn.net/hohaizx/article/details/78427406
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.result = None
        self.k = None

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k == 0:
            return
        self.k = k
        self.KthNodeCore(pRoot)
        return self.result

    def KthNodeCore(self, pRoot):
        if pRoot:
            self.KthNodeCore(pRoot.left)
            if self.k == 1:
                self.result = pRoot
            self.k -= 1
            self.KthNodeCore(pRoot.right)

node1 = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(7)
node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(6)
node7 = TreeNode(8)

node1.left,node1.right = node2,node3
node2.left,node2.right = node4,node5
node3.left,node3.right = node6,node7

a = Solution()
print(a.KthNode(node1,8))
