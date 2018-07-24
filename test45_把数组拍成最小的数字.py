# 面试题45 把数组拍成最小的数字

class Solution:
    def PrintMinNumber(self,numbers):
        if not numbers:
            return ''
        vec = []
        self.Permutation(numbers,0,vec)
        vec.sort()
        return vec[0]

    def Permutation(self,numbers,n,vec):
        if n >= len(numbers):
            vec.append(int(''.join(map(str,numbers))))
        for i in range(n,len(numbers)):
            numbers[i],numbers[n] = numbers[n],numbers[i]
            self.Permutation(numbers,n+1,vec)
            numbers[i], numbers[n] = numbers[n], numbers[i]

    def check(self,numbers,n,i):
        if i > n:
            for j in range(n,i):
                if numbers[j] == numbers[i]:
                    return False
        return True

class Solution2:
    def PrintMinNumber(self, numbers):
        from functools import cmp_to_key
        if not numbers:
            return ''
        lmb = cmp_to_key(lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1)))
        array = sorted(numbers, key=lmb)# 不太懂里面的运行机理
        return ''.join([str(i) for i in array])

lis =[3,5,1,4,2]
# a = Solution()
# a.PrintMinNumber(lis)
b=Solution2()
c = b.PrintMinNumber(lis)
print(c)
