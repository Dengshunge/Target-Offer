# 面试题43 1—n整数中1出现的次数
'''
这个是暴力解法
书上有更加简单的方法，但不太看懂
'''

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        number = 0
        for i in range(1, n + 1):
            number += self.NumberOf1(i)
        return number

    def NumberOf1(self,n):
        number = 0
        while n :
            if n % 10 == 1:
                number += 1
            n =  n // 10
        return number

a = Solution()
print(a.NumberOf1Between1AndN_Solution(13))
