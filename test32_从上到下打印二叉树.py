# 面试题32 从上到下打印二叉树

class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class MyQueue:
    def __init__(self):
        self.Queue = []
    def enqueue(self,data):
        self.Queue.append(data)
    def dequeue(self):
        return self.Queue.pop(0)
    def Print(self):
        print(self.Queue)
    def Size(self):
        return len(self.Queue)

# 不分行从上到下打印二叉树
def PrintFromTopToBottom(Node):
    if not isinstance(Node,TreeNode):
        return
    Queue = MyQueue()
    Queue.enqueue(Node)
    while Queue.Size():
        temp = Queue.dequeue()
        print(temp.data,end=' ')
        if temp.left:
            Queue.enqueue(temp.left)
        if temp.right:
            Queue.enqueue(temp.right)
    
node1 = TreeNode(8)
node2 = TreeNode(6)
node3 = TreeNode(10)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(9)
node7 = TreeNode(11)

node1.left,node1.right = node2,node3
node2.left,node2.right = node4,node5
node3.left,node3.right = node6,node7

PrintFromTopToBottom(node1)
