# 面试题48 最长不含重复字符的子字符串
'''
还是利用动态规划的方法来解决
定义f(i)表示以第i个字符为结尾的不包含重复字符的子字符串的最大长度。
现在有2种情况：
1. 当第i个字符没有出现过时，f(i)=f(i-1)+1
2. 当第i个字符出现过时，记两个重复字符的距离为d
    a) 若d<=f(i-1)时，说明重复的字符在f(i-i)的最长子字符串中，所以f(i)=d
    b) 若d>f(i-1)时，说明重复的字符不在f(i-i)的最长子字符串中，所以f(i)=f(i-1)+1

下面的程序中，curLength相当于f(i)。
如果不能理解的话，可以新建一个list来保存f(i)。
'''

class Solution:
    def longestSubstringWithoutDuplication(self, s1):
        curLength, maxLength = 0, 0#curLength相当于书上的f(i)
        position = [-1] * 26  # 这里26表示26个字母，这个list用于保存上一个重复字符的位置
        for i in range(len(s1)):
            prevIndex = position[ord(s1[i]) - ord('a')]  # python无字符串相减，所以用ord将字符转换为ascii码
            if prevIndex < 0 or i - prevIndex > curLength:
                # 后半个判断条件是：当第i位的字符和重复的字符的位置相差大于curLength时，不变
                curLength += 1
            else:
                if curLength > maxLength:
                    maxLength = curLength
                # 当第i位的字符和重复的字符的位置相差小于curLength时，让curLength=d
                curLength = i - prevIndex # 2个相同字符的距离d
            position[ord(s1[i]) - ord('a')] = i # 保存当先字符的下标
        if curLength > maxLength:
            maxLength = curLength
        print(maxLength)

a = Solution()
a.longestSubstringWithoutDuplication('arabcacfr')
