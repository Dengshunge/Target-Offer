# 面试题21 调整数组顺序使奇数位于偶数之前
'''
这道题的思路类似于快排的算法，设置两个指针，当符合情况的时候，交换两个指针的值
'''

def ReorderOddEven(lis):
    if not isinstance(lis,list) or not lis:
        return
    low,high = 0,len(lis)-1
    while low < high:
        while low<high and lis[low] % 2 == 1:
            low += 1
        while low < high and lis[high] %2 == 0:
            high -= 1
        lis[low],lis[high] = lis[high],lis[low]

lis = [1,5,3,7,2]
ReorderOddEven(lis)
print(lis)
