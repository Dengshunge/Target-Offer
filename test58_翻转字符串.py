# 面试题58 翻转字符串
'''
对于python来说，翻转字符串是很简单的事情，因为python里面所有都是对象。
对于题目一，python有个split函数，用于分割字符串，分割完后再进行翻转，但我感觉这是利用了空间换取了效率。
如果用C++的写法，需要两次翻转，首先将所有字母都翻转一次，然后在判断空格，将单词翻转回来

对于题目二，同样是题目一的思路，将单词分成两部分，分别翻转，再对所有单词都翻转
'''
# 题目一 翻转单词顺序
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s1 = s.split(' ')
        return ' '.join(s1[::-1])

class Solution2:
    def __init__(self):
        self.s = []

    def ReverseSentence(self,s):
        self.s = list(s)
        self.Reverse(0,len(self.s)-1)
        pBegin,pEnd = 0,0
        while pBegin < len(self.s):
            if self.s[pBegin]=='':
                pBegin += 1
                pEnd += 1
            elif pEnd == len(self.s) or self.s[pEnd] == ' ':
                self.Reverse(pBegin,pEnd - 1)
                pBegin = pEnd + 1
                pEnd += 1
            else:
                pEnd += 1
        return ''.join(self.s)

    def Reverse(self, pBegin, pEnd):
        while pBegin < pEnd:
            self.s[pBegin], self.s[pEnd] = self.s[pEnd], self.s[pBegin]
            pBegin += 1
            pEnd -= 1

# 题目二 左旋转字符串
class Solution3:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        return s[n:] + s[:n]

class Solution4:
    def __init__(self):
        self.s = None

    def LeftRotateString(self, s, n):
        if not s:
            return ''
        self.s = list(s)
        self.Reverse(0,n-1)
        self.Reverse(n,len(self.s)-1)
        self.Reverse(0,len(self.s)-1)
        return ''.join(self.s)

    def Reverse(self, pBegin, pEnd):
        while pBegin < pEnd:
            self.s[pBegin], self.s[pEnd] = self.s[pEnd], self.s[pBegin]
            pBegin += 1
            pEnd -= 1

# s1 = 'I am a student.'
s1 = 'abcdefg'
# a = Solution()
# print(a.ReverseSentence(s1))
# b = Solution2()
# print(b.ReverseSentence(s1))
# c = Solution3()
# print(c.LeftRotateString(s1,6))
d = Solution4()
d.LeftRotateString(s1,2)
