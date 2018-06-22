# 面试题9 用两个栈实现队列
class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self,element=None):
        if not element:
            return
        self.stack1.append(element)

    def deleteHead(self):
        if not self.stack1 and not self.stack2:
            return
        if not self.stack2:#若stack2为空
            while self.stack1:
                self.stack2.append(self.stack1.pop())# 将stack1的元素反向压入stack2
        return self.stack2.pop()

if __name__ == '__main__':
    aa = CQueue()
    aa.appendTail(3)
    aa.appendTail(2)
    aa.appendTail()
    print(aa.deleteHead())
    print(aa.deleteHead())
    print(aa.deleteHead())
