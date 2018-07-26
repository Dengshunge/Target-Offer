# 面试题50 第一个只出现一次的字符
'''
如果需要判断多个字符是不是在某个字符串里出现过或者统计多个字符在字符串中出现的次数，我们可以考虑给予数组创建一个简单的哈希表，
这样可以用很小的空间消耗换来时间效率的提升。

在题目一中，书上是利用ascii码来建一个数组，而我们可以直接调用python中的dict。
在题目二中，是从字符流中读取，可以理解为更新了字符串，原来和题目一一样，利用哈希表。
'''

class Solution:
    def FirstNotRepeatingChar(self,s1):
        if not s1:
            return -1
        Hash_Map = {}
        for i in s1:
            Hash_Map[i] = Hash_Map.get(i, 0) + 1
        # 在python3.x版本中，dict是的顺序是根据插入时候的顺序的，不会改变
        # for i in Hash_Map:
        #     if Hash_Map[i] == 1:
        #         return i
        # 而如果在python2.x版本中，dict的顺序会改变
        for i in s1:
            if Hash_Map[i] == 1:
                return i
        return -1

class Solution2:
    def __init__(self):
        self.s=''
        self.Hash_Map = {}

    def FirstAppearingOnce(self):
        for i in self.s:
            if self.Hash_Map[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        self.s += char
        self.Hash_Map[char] = self.Hash_Map.get(char,0) + 1

# a = Solution()
# print(a.FirstNotRepeatingChar('NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp'))
b = Solution2()
