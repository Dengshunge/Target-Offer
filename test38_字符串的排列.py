# 面试题38 字符串的排列
'''
如果面试题是按照一定要求摆放若干个数字，则可以先求出这些数字的全排列，然后一一判断每个排列是不是满足题目给定的要求。

全排列算法，很常见，利用递归
固定第i个数组，然后处理后面n-i个数组
这里需要交换2个位置，但最后会交换回来。
https://blog.csdn.net/summerxiachen/article/details/60579623

扩展提是全组合算法
这里需要用到一个缓存list
首先将元素压入vec，然后处理lis[1:]后面的元素
'''

def Permutation(lis):
    if not isinstance(lis,list):
        return
    Permutation_(lis,0)

def Permutation_(lis,n):
    if n >= len(lis):
        print(' '.join(lis))
        return
    for i in range(n,len(lis)):
        if check(lis,n,i):
            lis[i], lis[n] = lis[n], lis[i]  # 交换两个位置
            Permutation_(lis,n+1)# 注意，这里是n+1
            lis[i], lis[n] = lis[n], lis[i]  # 交换回来

def check(lis,n,i):
    # n,i是指这两个元素需要交换
    # 当lis[n]==lis[i]说明两个元素相同，不需要交换，不然会有重复
    if i > n:# 不用等号是允许自身与自身交换
        # 当不是与自身交换的时候，判断是否会有重复
        for j in range(n,i):
            if lis[j] == lis[i]:
                return False
    return True
               
def Combination(lis):
    if not isinstance(lis,list):
        return
    vec = []
    for i in range(1,len(lis)+1):
        Combination_(lis,vec,i)

def Combination_(lis,vec,m):
    if m == len(vec):
        print(' '.join(vec))
        return
    if lis:
        vec.append(lis[0])
        Combination_(lis[1:],vec,m)
        vec.pop()
        Combination_(lis[1:],vec,m)

# n个皇后问题
def queens(n):
    lis = [x for x in range(n)]
    Permutation_n(lis,0)

def Permutation_n(lis,n):
    if n >= len(lis):
        if SatisfyQueenRequirements(lis):
            print(' '.join(map(str,lis)))
        return
    for i in range(n,len(lis)):
        lis[i],lis[n] = lis[n],lis[i]
        Permutation_n(lis,n+1)
        lis[i],lis[n] = lis[n],lis[i]

def SatisfyQueenRequirements(lis):
    Flag = True
    for i in range(0,len(lis)-1):
        for j in range(i+1,len(lis)):
            if abs(i - j) == abs(lis[i] - lis[j]):
                Flag = False
                break
        if not Flag:
            break
    return Flag

# lis = list('abc')
# Permutation(lis)
# Combination(lis)
queens(8)
