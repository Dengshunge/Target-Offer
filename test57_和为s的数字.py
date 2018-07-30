# 面试题57 和为s的数字
'''
求和为s的数字，是设置两个指针，第一个指向头，第二个指向尾
当两者之和大于tsum时，缩小第二个指针，否则增大第二个指针。

在求和为s的序列的时候，同样是设置两个指针，当之间的和小于tsum时，增加第二个指针。
当值大于tsum时，继续减少第一个指针，直至值与tsum相等。
'''

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        left, right = 0, len(array) - 1
        while left<=right:
            temp = array[left] + array[right]
            if temp == tsum:
                return [array[left],array[right]]
            elif temp < tsum:
                left += 1
            else:
                right -= 1
        return []

class Solution2:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 0:
            return []
        if tsum < 3:
            return []
        small, big = 1, 2
        mid = (1 + tsum) >> 1  # 这步是为了循环停止，让small都大于中间的数了，怎么相加都会大于tsum
        curSum = small + big
        result = []
        while small < mid:
            if curSum == tsum:
                result.append(list(range(small, big + 1)))
            # 这一步很巧妙，当大于tsum时，减少small的值
            # 这里需要用循环，而不是if
            while curSum > tsum and small < mid:
                curSum -= small
                small += 1
                if curSum == tsum:
                    result.append(list(range(small, big + 1)))
            big += 1
            curSum += big
        return result
    
# array = [1,2,4,7,11,15]
# a = Solution()
# print(a.FindNumbersWithSum(array,100))
a = Solution2()
print(a.FindContinuousSequence(3))
