# 面试题62 圆圈中最后剩下的数字
'''
这是经典的方法，利用环形链表来模拟圆圈。
书上有一种基于数学推导的方法，但面试的时候，大概率是想不到的
'''

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        # 创建一个环形链表
        head = Node(0)
        p = head
        for i in range(1,n):
            temp = Node(i)
            p.next = temp
            p = temp
        p.next = head

        p = head
        while n > 1:
            for i in range(m-1):
                p = p.next
            # 弹出该元素
            temp = p.next
            p.data,p.next = temp.data,temp.next
            n -=1
        return p.data

a = Solution()
print(a.LastRemaining_Solution(4000,997))
