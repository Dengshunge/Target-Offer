# 面试题61 扑克牌中的顺子
'''
我一开始的想法是，统计0的个数，然后看除0意外的数字是不是顺序排列，当不是顺序排序的时候，插入多少个0才能变顺序排列。
如果按我之前的想法，可能会变得复杂了。
而书上的想法是，比较0的个数和除0意外数字的间隔，若0的个数大于间隔，则说明是顺子。
这种方法能抽象的概括了很多中情况，我现在欠缺这种思维。
'''
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) != 5:
            return False
        numbers.sort()

        numberOfZeros = 0
        for i in numbers:
            if i == 0:
                numberOfZeros += 1

        numberOfGap = 0
        small = numberOfZeros
        while small < len(numbers)-1:
            if numbers[small] == numbers[small+1]:
                return False
            numberOfGap += numbers[small+1] - numbers[small] - 1
            small += 1
        return False if numberOfGap > numberOfZeros else True

numbers = [2,4,0,0,3]
a = Solution()
print(a.IsContinuous(numbers))
