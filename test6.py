# 面试题6 从尾到头打印链表
'''
链表的倒序是利用堆栈，如果用递归，可能会出现递归深度的问题。
所以用循环比较好。
'''
#单链表
class Node:
    #单链表节点
    def __init__(self,data,p=None):
        self.data = data
        self.next = p                                                                                                                                              = p

# 无头指针，只有头节点
class LinkList:
    def __init__(self):
        self.head = Node(None)

    def create(self,data):
        if not isinstance(data,list) or len(data) == 0:
            print('list is null')
            return
        self.head = Node(data[0])
        p = self.head#将p指向头节点,p的类型为Node
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

    def print(self):
        p = self.head
        lis = []
        while p != None:
            lis.append(p.data)
            p = p.next
        print(' '.join(map(str,lis)))

# 非递归版本，利用堆栈
def PrintListReversingly_Iteratively(head):
    if head.next == None:
        return
    stack = []
    p = head
    while p != None:
        stack.append(p.data)
        p = p.next
    for i in range(len(stack)):
        print(stack.pop(),end=' ')

# 递归版本
def PrintListReversingly_Recursively(head):
    if head.next == None:
        return
    p = head
    if p.next != None:
        PrintListReversingly_Recursively(p.next)
    print(p.data,end=' ')


if __name__ == '__main__':
    a = LinkList()
    a.create([])
    # a.print()
    PrintListReversingly_Iteratively(a.head)
    print()
    PrintListReversingly_Recursively(a.head)
