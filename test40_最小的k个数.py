# 面试题40 最小的k个数
'''
第一种方法是基于快排的思想，因为pivot的划分，基于此划分，又可以处理左边或右边，直至pivot==k-1
第二种方法是不改变原数组，利用容器，当容器中的最大元素大于数组的值时，进行替换。
    这里的容器可以是二叉树，最大堆，或者红黑树等。
'''

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or len(tinput)<k or k<=0:
            return []
        pivot = self.Partition(tinput,0,len(tinput)-1)
        while pivot != (k-1):
            if pivot>k:
                pivot = self.Partition(tinput,0,pivot-1)
            else:
                pivot = self.Partition(tinput,pivot+1,len(tinput)-1)
        return sorted(tinput[:k])

    def Partition(self,numbers,low,high):
        key = numbers[low]
        while low < high:
            while low < high and numbers[high] >= key:
                high -= 1
            numbers[low],numbers[high] = numbers[high],numbers[low]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[low],numbers[high] = numbers[high],numbers[low]
        return low

class Solution_1:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or len(tinput)<k or k<=0:
            return []
        # 我这里为了方便，使用了list，其实应该使用最大堆作为容器，这样时间复杂度更低
        vec = [x for x in tinput[:k]]
        MaxIndex = self.Find_Max(vec)
        for i in tinput[k:]:
            if i < vec[MaxIndex]:
                vec[MaxIndex] = i
                MaxIndex = self.Find_Max(vec)
        return sorted(vec)

    def Find_Max(self,lis):
        return lis.index(max(lis))



tinput = [4,5,1,6,2,7,8,3]
a = Solution_1()
b = a.GetLeastNumbers_Solution(tinput,2)
print(b)
