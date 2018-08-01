# 面试题65 不用加减乘除做加法
'''
对数字做运算，除了四则运算之外，也就只剩下位运算了。
程序中存在一些十六进制，是为了防止越位
'''

class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            carry = (num1 & num2) << 1  # 进位
            num1 = (num1 ^ num2) % 0x100000000  # 两者异或
            num2 = carry % 0x100000000
        return num1 if num1<=0x7FFFFFFF else num1 |(~0x100000000+1) # 这步是为了防止越界

a = Solution()
print(a.Add(1,-2))
