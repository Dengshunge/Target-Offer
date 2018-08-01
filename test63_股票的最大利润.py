# 面试题63 股票的最大利润
'''
还是考察数学建模能力。
如果用暴力法的话，每个数字都与后面的数字相减，时间复杂度是O(n^2)
书中的方法很好，假设diff(i)为当卖出价为第i个数字时的最大利润。
当第i个数字固定的时候，且为卖出价，只要找到前面最小的数字，即利润最大化。
所以把前面最小的数字保存起来，这样时间复杂度为O(n)
明显快了很多
为什么我不能想到这种方法呢？
'''

class Solution:
    def MaxDiff(self,numbers):
        if not numbers or len(numbers) < 2:
            return 0
        minVal = numbers[0]
        maxDiff = numbers[1] - minVal
        for i in range(2,len(numbers)):
            # 更新最小值
            if numbers[i-1] < minVal:
                minVal = numbers[i-1]

            # 计算差值
            curDiff = numbers[i] - minVal
            if curDiff > maxDiff:
                maxDiff = curDiff
        return maxDiff

numbers = [9,11,8,5,7,12,16,14]
a = Solution()
print(a.MaxDiff(numbers))
