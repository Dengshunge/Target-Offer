# 面试题38 字符串的排列
'''
全排列算法，很常见，利用递归
固定第i个数组，然后处理后面n-i个数组
这里需要交换2个位置，但最后会交换回来。
https://blog.csdn.net/summerxiachen/article/details/60579623
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
        lis[i], lis[n] = lis[n], lis[i]  # 交换两个位置
        Permutation_(lis,n+1)# 注意，这里是n+1
        lis[i], lis[n] = lis[n], lis[i]  # 交换回来

lis = list('abc')
Permutation(lis)
