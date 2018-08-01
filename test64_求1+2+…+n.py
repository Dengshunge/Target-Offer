# 面试题64 求1+2+…+n
'''
这里运用了闭包的概念，涉及到python的装饰器
但我不太懂这个
'''

class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def qiusum(n):
            self.sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        qiusum(n)
        return self.sum

a = Solution()
print(a.Sum_Solution(10))
