# 面试题53 在排序数组中查找数字
'''
三道题目都是二分查找的变式，当涉及到元素的值和下标的关系，而且又是查找，可以考虑下二分查找
'''

# 题目一：数字在排序数组中出现的次数
'''
方法1：利用二分查找，找到等于k的数字，然后向左向右顺序扫描，此时二分查找的复杂度是O(logn)，顺序查找时O(n)，所以总的复杂度是O(n)
方法2：同样是利用二分查找，但二分查找是找到重复数字的开始和末尾，不进行顺序扫描，所以复杂度是O(logn)
'''
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        number = 0
        first = self.GetFirstK(data,k)
        last = self.GetLastK(data,k)
        if first >-1 and last > -1:
            number = last -first +1
        return number

    def GetFirstK(self,data,k):
        start, end = 0, len(data) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if data[mid]== k:
                if (mid > 0 and data[mid - 1] != k) or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def GetLastK(self,data,k):
        start, end = 0, len(data) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if data[mid]== k:
                if (mid < len(data) - 1 and data[mid + 1] != k) or mid == len(data) - 1:
                    return mid
                else:
                    start = mid + 1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1

# 题目二 0~n-1中缺失的数字
class Solution2:
    def GetMissingNumber(self,numbers):
        if not numbers:
            return -1
        start, end = 0, len(numbers) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if numbers[mid] == mid:
                # 此时下标相同，说明缺失的数字在后面
                start = mid + 1
            else:
                if (mid > 0 and numbers[mid - 1] == (mid - 1)) or mid == 0:
                    return mid
                end = mid - 1
        if start == len(numbers):#这是只有一个元素的情况
            return len(numbers) - 1
        return -1

# 题目三 数组中数值和下标相等的元素
class Solution3:
    def GetNumberSameAsIndex(self,numbers):
        if not numbers:
            return -1
        start, end = 0, len(numbers) - 1
        while start<=end:
            mid = (start + end) >> 1
            if mid == numbers[mid]:
                return mid
            elif mid < numbers[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


lis = [1,2,3,3,3,3,4,5]
lis1 = [0,1,2,4,5,6]
lis2 = [-10,-8,2]
# lis= []
# a = Solution()
# b = a.GetNumberOfK(lis,1)
# print(b)
# a = Solution2()
# print(a.GetMissingNumber(lis1))
a = Solution3()
print(a.GetNumberSameAsIndex(lis2))
