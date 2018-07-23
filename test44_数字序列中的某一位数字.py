# 面试题44 数字序列中的某一位数字
'''
第一种方法是暴力解法，不足之处是应该计算一下range的范围，而不应该用index，这样会浪费很多内存

第二中方法是找规律，这个规律有点难找，无论在面试和笔试中，这点时间不可能想到，只能靠积累了。

'''
class Solution:
    def digitAtIndex(self,index):
        if index < 0 :
            return -1
        xx = [i for i in range(index+1)]
        ss = ''.join(map(str,xx))
        print(ss[index])

class Solution_2:
    def digitAtIndex(self,index):
        if index < 0:
            return -1
        digit = 1
        while True:
            numbers = self.countOfIntegers(digit)
            if index < numbers * digit:
                return self.digitAtIndex_2(index,digit)
            index -= digit*numbers
            digit += 1

    def countOfIntegers(self,digits):
        # 统计digits位一共有多少个数字
        if digits == 1:
            return 10
        count = pow(10,digits-1)
        return 9*count

    def digitAtIndex_2(self,index,digit):
        Location = index // digit
        yushu = index % digit
        xx = str(self.beginNumber(digit) + Location)
        return xx[yushu]

    def beginNumber(self,digit):
        if digit == 1:
            return 0
        return pow(10,digit-1)

# a = Solution()
# a.digitAtIndex(12)
b=Solution_2()
print(b.digitAtIndex(12))

