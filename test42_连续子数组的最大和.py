# 面试题42 连续子数组的最大和
'''
举例子，模拟计算机运行
若全为负数的话，子序列的最大和则应该由一个单值构成

'''

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0
        nCurSum = 0
        nGreatestSum = -float('inf')
        for i in array:
            if nCurSum<=0:
                # 当nCureSum为负数的时候，抛弃前面的值
                nCurSum = i
            else:
                nCurSum += i
            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum
        return nGreatestSum

a = Solution()
array = [-10,2,3]
result = a.FindGreatestSumOfSubArray(array)
print(result)
