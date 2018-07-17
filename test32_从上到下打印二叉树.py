# 面试题32 从上到下打印二叉树
'''
本道面试题很有意思
首先是不分行打印，这时是图的广度优先搜索，利用队列来实现
其次是分行的打印，这时在利用队列的基础上，需要用2个变量来控制分行
最后是之字形打印，这里就是利用栈了，而不是队列，利用两个栈来表示奇数层和偶数层，分别管理

'''

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class MyQueue:
    def __init__(self):
        self.Queue = []

    def enqueue(self, data):
        self.Queue.append(data)

    def dequeue(self):
        return self.Queue.pop(0)

    def Print(self):
        print(self.Queue)

    def Size(self):
        return len(self.Queue)


# 不分行从上到下打印二叉树
def PrintFromTopToBottom(Node):
    if not isinstance(Node, TreeNode):
        return
    Queue = MyQueue()
    Queue.enqueue(Node)
    while Queue.Size():
        temp = Queue.dequeue()
        print(temp.data, end=' ')
        if temp.left:
            Queue.enqueue(temp.left)
        if temp.right:
            Queue.enqueue(temp.right)

# 分行从上到下打印二叉树
def PrintFromTopToBottom_2(Node):
    if not isinstance(Node, TreeNode):
        return
    Queue = MyQueue()
    toBePrinted, nextLevel = 1, 0  # toBePrinted表示本层未打印节点的数量，nextLevel表示下层要打印节点的数量
    Queue.enqueue(Node)
    while Queue.Size():
        temp = Queue.dequeue()
        print(temp.data,end=' ')
        toBePrinted -= 1
        if temp.left:
            nextLevel += 1
            Queue.enqueue(temp.left)
        if temp.right:
            nextLevel += 1
            Queue.enqueue(temp.right)
        if toBePrinted == 0:
            print()
            toBePrinted = nextLevel
            nextLevel = 0

# 之字形打印二叉树
# 需要利用两个栈来管理奇数层和偶数层
def PrintFromTopToBottom_3(Node):
    if not isinstance(Node, TreeNode):
        return
    stack1,stack2 = [Node],[]# 奇数栈从左往右打印，偶数栈从右往左打印
    stack = [stack1,stack2]
    current,next = 0,1
    while stack1 or stack2:
        temp = stack[current].pop()
        print(temp.data,end=' ')
        if current == 0:
            #在奇数层，下一层应该从右到左压入
            if temp.left:
                stack[next].append(temp.left)
            if temp.right:
                stack[next].append(temp.right)
        else:
            if temp.right:
                stack[next].append(temp.right)
            if temp.left:
                stack[next].append(temp.left)
        if not stack[current]:
            # 说明该层打印完了
            print()
            current = 1 -current
            next = 1- next


node1 = TreeNode(8)
node2 = TreeNode(6)
node3 = TreeNode(10)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(9)
node7 = TreeNode(11)

node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.left, node3.right = node6, node7

# PrintFromTopToBottom(node1)
# PrintFromTopToBottom_2(node1)
PrintFromTopToBottom_3(node1)
