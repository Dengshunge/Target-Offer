# 面试题30 包含min函数的栈
'''
本题的思路是构建2个栈，一个数据栈，一个辅助栈
对于辅助栈，每次都是压入当前的最小值
'''

class StackWithMin:
    def __init__(self):
        self.m_data=[]#数据栈
        self.m_min =[]#辅助栈

    def push(self,data):
        self.m_data.append(data)

        if len(self.m_min) == 0 or data<self.m_min[-1]:
            self.m_min.append(data)
        else:
            self.m_min.append(self.m_min[-1])

    def pop(self):
        if len(self.m_data) or len(self.m_min):
            self.m_data.pop()
            self.m_min.pop()
        else:
            return

    def min(self):
        if len(self.m_data) or len(self.m_min):
            print(self.m_min[-1])
        else:
            return

if __name__=='__main__':
    a = StackWithMin()
    a.push(3)
    a.min()
    a.push(2)
    a.push(4)
    a.min()
    a.pop()
    a.min()
    a.pop()
    a.min()
