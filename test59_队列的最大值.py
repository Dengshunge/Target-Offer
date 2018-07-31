# 面试题59 队列的最大值


# 题目一 滑动窗口的最大值
class Solution:
    # 这是暴力解法，我猜测内置函数Max也是一个一个对比寻找
    def maxInWindows(self, num, size):
        # write code here
        maxInWindows = []
        if len(num)>=size and size>=1:
            for i in range(len(num)-size+1):
                maxInWindows.append(max(num[i:i+size]))
        return maxInWindows
        
num = [2,3,4,2,6,2,5,1]
a = Solution()
# print(a.maxInWindows(num,3))
print(a.maxInWindows2(num,3))
