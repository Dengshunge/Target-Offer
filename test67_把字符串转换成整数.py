# 面试题67 把字符串转换成整数
'''
Python中str无相减，所以要利用ord()函数，将其转换成ascii码
这题难度不大，主要注意条件条件

'''

class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        if s[0] == '+':
            return self.StrToIntCore(s[1:])
        elif s[0] == '-':
            return -1*self.StrToIntCore(s[1:])
        return self.StrToIntCore(s)

    def StrToIntCore(self,s):
        num = 0
        for i in s:
            if ord(i) < ord('0') or ord(i) > ord('9'):
                return 0
            num = num * 10 + ord(i) - ord('0')
        return num

a = Solution()
print(a.StrToInt('1536'))
