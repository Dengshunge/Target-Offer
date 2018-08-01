# 面试题66 构建乘积数组
'''
这是个数学简单推导的例子
将一个问题分解成2个问题解决
'''

class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return
        C_array = [1]
        for i in range(1,len(A)):
            C_array.append(C_array[i - 1] * A[i - 1])
        D_array = [1] * len(A)
        for i in range(len(A)-2,-1,-1):
            D_array[i] = D_array[i + 1] * A[i + 1]

        result = []
        for i in range(len(A)):
            result.append(C_array[i]*D_array[i])
        return result

A = [2,3,4,5,6]
a = Solution()
a.multiply(A)
