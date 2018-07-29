# 面试题56 数组中数字出现的次数
'''
这道题很难想到思路，但方法很巧妙，利用了二进制
首先，相同的数字异或为0，可以考虑将一个数组分成两个子数组，这两个子数组里面，分别包含一个出现1次的数字和若干个成对出现的数字。
这样通过异或，就得获得只出现1次的数字。

这道题要求了时间复杂度为O(n),空间复杂度为O(1)，如果不这么要求的话，可以利用排序或者哈希表。
'''

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array)<2:
            return

        resultExclusiveOR = 0
        # 每一位都进行异或，当相同的数字异或，会变成0，所以最后的结果是两个只出现1次的数字异或的结果
        for i in array:
            resultExclusiveOR ^= i

        # 异或的结果为1，说明这2个数字的二进制的这一位不相同，可以根据这一位的不同，划分成2个子数组
        indexOf1 = self.FindFirstBitIs1(resultExclusiveOR)

        # 将2个子数组分别各自异或，因为每个子数组现在的组成是1个出现1次的数字和若干对成对出现的数字
        # 成对出现的的数字异或的结果为0
        # 所以最后的结果就是那个只出现1次的数字
        num1, num2 = 0, 0
        for i in array:
            if self.IsBit1(i,indexOf1):
                num1 ^= i
            else:
                num2 ^= i
        return sorted([num1,num2])

    def FindFirstBitIs1(self,num):
        indexBit = 0
        # 后面的这个判断条件是为了防止数组中没有出现的数字
        # 但python中int无上限，所以我就认为设置了最大是10位
        while num & 1 == 0 and indexBit < 10:
            num = num >> 1
            indexBit += 1
        return indexBit

    def IsBit1(self,num,indexBit):
        num = num >> indexBit
        return num & 1

'''
同样是利用位运算的思想。把每个数字的每个位都对应相加，如果一个数字出现3次，那么它的二进制表示的每一位也就出现3次，
那么每一位都能被3整除。
所以当再加上一个不重复的数字时，就能得到这个结果
'''
class Solution2:
    def FindNumberAppearingOnec(self,array):
        if not array:
            return
        bitSum = [0]*32
        for i in array:
            bitMask = 1
            # 将每一位的二进制都分别按位相加
            for j in range(31,-1,-1):
                bit = i & bitMask
                if bit != 0:
                    bitSum[j] += 1
                bitMask = bitMask << 1

        # 当出现一位不能被3整除的时候，说明只出现1次的数字在这个二进制中也占1位。
        result = 0
        for i in bitSum:
            result = result<<1
            result += i % 3
        print(result)

# array = [2,4,3,6,3,2,5,5]
# a = Solution()
# print(a.FindNumsAppearOnce(array))
array = [1,1,1,2,2,2,3,4,4,4]
a = Solution2()
a.FindNumberAppearingOnec(array)
