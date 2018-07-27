# 面试题51 数组中的逆序对
'''
第一种方式是简单粗暴，每次都和后面的相比，时间复杂度是O(n)
第二种方法利用了递归的思想，很有意思，但很难想到，时间复杂度是O(nlogn)
'''

# 用于修改递归最大深度，否则在牛客网上跑会超时
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def InversePairs(self, data):
        if not data :
            return 0
        Copy = [i for i in data]
        count = self.InversePairsCore(data, Copy, 0, len(data) - 1)
        del Copy
        return count % 1000000007

    def InversePairsCore(self,data,Copy,start,end):
        if start == end:
            Copy[start] == data[start]
            return 0

        mid = int((start + end) / 2)

        left = self.InversePairsCore(Copy, data, start, mid)
        right = self.InversePairsCore(Copy, data, mid + 1, end)

        # 下面相当于merge
        # i初始化为前半段最后一个数字的下标，j初始化为后半段最后一个数字的下标
        i, j = mid, end
        indexCopy = end
        count = 0
        while i >= start and j >= mid + 1:
            if data[i]>data[j]:
                Copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - mid
            else:
                Copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        # 进行到这里，说明知道有一个数组已经到头了，或者是i或者是j
        while i >= start:
            Copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= mid + 1:
            Copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1

        return left + right + count

# 非递归版本
class Solution2:
    def InversePairs(self, data):
        if not data :
            return 0
        temp = [0]*len(data)
        k = 1
        count = 0
        while k < len(data):
            count += self.InversePairsCore(data,temp,k)
            k *=2
        return count % 1000000007

    def InversePairsCore(self,data,temp,k):
        length = len(data)
        i = 0
        count = 0
        while i <= length - 2 * k:
            count += self.Merge(data, temp, i, i + k - 1, i + 2 * k - 1)
            i += 2 * k
        if i + k - 1 < length - 1:
            count += self.Merge(data, temp, i, i + k - 1, length - 1)
        return count

    def Merge(self,data,temp,start,mid,end):
        # 分别是两个半段的末尾的指针
        i,j = mid,end
        tempIndex = end  # 缓存数组的指针
        count = 0
        while i >= start and j >= mid+1:
            if data[i] > data[j]:
                temp[tempIndex] = data[i]
                count += j - mid
                tempIndex -= 1
                i -= 1
            else:
                temp[tempIndex] = data[j]
                tempIndex -= 1
                j -= 1

        while i >= start:
            temp[tempIndex] = data[i]
            tempIndex -= 1
            i -= 1
        while j >= mid + 1:
            temp[tempIndex] = data[j]
            tempIndex -= 1
            j -= 1

        data[start:end+1] = temp[start:end+1]# 将缓存数组里面的数据复制回去原来的数组
        return count

lis = [7,5,6,4]
a = Solution2()
b = a.InversePairs(lis)
print(b)
