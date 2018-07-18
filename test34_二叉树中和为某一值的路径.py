# 面试题34 二叉树中和为某一值的路径
'''
本道题是以根节点为扩展的，包含的路径必须右根节点，所以不能某一部分的值之和
'''

class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def FindPath(Node,expectedSum):
    if not isinstance(Node,TreeNode) or not isinstance(expectedSum,int):
        return
    path = []
    currentSum = 0
    Find_Path(Node,expectedSum,path,currentSum)

def Find_Path(Node,expectedSum,path,currentSum):
    currentSum += Node.data
    path.append(Node)

    # 如果是叶节点，且路径上的节点值之和等于输入的值，则打印
    isLeaf = Node.left == None and Node.right == None
    if currentSum == expectedSum and isLeaf:
        for i in path:
            print(i.data,end=' ')
        print()

    # 如果不是叶节点，则遍历它的子节点
    if Node.left:
        Find_Path(Node.left,expectedSum,path,currentSum)
    if Node.right:
        Find_Path(Node.right,expectedSum,path,currentSum)

    # 在返回父节点之前，在路径上删除当前节点
    path.pop()

node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(12)
node4 = TreeNode(4)
node5 = TreeNode(7)

node1.left,node1.right = node2,node3
node2.left,node2.right = node4,node5

FindPath(node1,22)
