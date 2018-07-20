# 面试题37 序列化二叉树
'''
序列化的意思是将二叉树存储成一个文件，反序列即将文件还原成二叉树。
在python里面，可以利用pickle或者json来进行处理，这里只是将其转化成一个list，没有存储

首先序列化，很简单，就是一个前序遍历，但不同之处在于，遇到none会打印'$'，而不是跳过。
然后反序列化，这里有点难度，还是利用递归来处理，这里需要引入一个变量，让其一直递增来进行构建节点。
具体可以看看程序，反序列化也可以理解成构建一个二叉树。
'''

class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def Serialize(pRoot,serializelis):
    if pRoot == None:
        serializelis.append('$')
        return
    serializelis.append(str(pRoot.data))
    Serialize(pRoot.left,serializelis)
    Serialize(pRoot.right,serializelis)

def Deserialize(serializelis):
    tree,sp = deserlialize(serializelis,0)
    return tree

def deserlialize(serializelis,sp):
    if sp >= len(serializelis) or not serializelis[sp].isdigit():
        return None,sp+1
    node = TreeNode(int(serializelis[sp]))
    sp += 1
    node.left,sp = deserlialize(serializelis,sp)
    node.right,sp = deserlialize(serializelis,sp)
    return node,sp


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left,node1.right = node2,node3
node2.left = node4
node3.left,node3.right = node5,node6

serializelis =[]
Serialize(node1,serializelis)
print(serializelis)
tree = Deserialize(serializelis)
print(tree.left.data)
