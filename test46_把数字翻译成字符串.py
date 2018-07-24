# 面试题46 把数字翻译成字符串
'''
将大问题分解成小问题解决，所以使用递归
f(i)表示第i位数字开始的不同翻译的数目
f(i)=f(i+1)+g(i,i+i)f(i+2)
g(i,i+i)表示当第i位和第i+1位组合成的数字在10到25的范围内时，为1，否则为0
上面的递归公式说明，第i为的总翻译数等于，当认为第i位为单值时，总数是后面的f(i+i)，当第i位和第i+1位组合组合时，
总数为f(i+2)
递归从最大的问题开始自上向下解决问题，但没法消除重复的问题。
所以我们可以从最小的问题开始自下向上解决问题。
'''

class Solution:
    def GetTranslationCount(self,number):
        if number < 0:
            return 0
        numberInString = str(number)
        return self.GetTranslation_Count(numberInString)

    def GetTranslation_Count(self,number):
        count = 0
        counts = [None] * len(number)
        for i in range(len(number)-1,-1,-1):
            count = 0
            if i < len(number) -1:
                count += counts[i+1]
            else:
                count =1
            if i < len(number) -1:
                digit1 = int(number[i])
                digit2 = int(number[i+1])
                converted = digit1*10 + digit2
                if converted >= 10 and converted <= 25:
                    if i < len(number) - 2:
                        count+=counts[i+2]
                    else:
                        count+=1
            counts[i] = count
        print(counts)
        return counts[0]

a = Solution()
c = a.GetTranslationCount(12258)
print(c)
