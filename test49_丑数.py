# 面试题49 丑数
'''
第一种方法时循环计算每个数，找到符合条件才结束，此时会计算很多非丑数的情况。
    最终导致的结果是跑起来会超时。
第二种方式是利用空间换时间，只计算丑数，找到在现成丑数中第一个大于此丑数的值，然后插入list里面，不断循环。
'''

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        number, uglyFound = 0, 0
        while uglyFound < index:
            number += 1
            if self.IsUgly(number):
                uglyFound += 1
        return number

    def IsUgly(self,number):
        while number % 2 == 0:
            number /= 2
        while number % 3 == 0:
            number /= 3
        while number % 5 == 0:
            number /= 5
        return True if number == 1 else False


class Solution2:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        pUglyNumbers = [1]
        NumberofUgly = 1
        pMultiply2, pMultiply3, pMultiply5 = 0, 0, 0
        while NumberofUgly < index:
            minVal = min(pUglyNumbers[pMultiply2]*2,
                         pUglyNumbers[pMultiply3]*3,
                         pUglyNumbers[pMultiply5]*5)
            pUglyNumbers.append(minVal)
            while pUglyNumbers[pMultiply2] * 2 <= pUglyNumbers[-1]:
                pMultiply2 += 1
            while pUglyNumbers[pMultiply3] * 3 <= pUglyNumbers[-1]:
                pMultiply3 += 1
            while pUglyNumbers[pMultiply5] * 5 <= pUglyNumbers[-1]:
                pMultiply5 += 1

            NumberofUgly += 1
        return pUglyNumbers[-1]

# a = Solution()
# b = a.GetUglyNumber_Solution(1500)
# print(b)
c = Solution2()
print(c.GetUglyNumber_Solution(1500))
