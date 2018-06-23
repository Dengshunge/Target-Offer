# 面试题11 旋转数组的最小数字
'''
此道面试题是二分查找的变式，比较有意思，时间复杂度为O(logn)
解题的突破点在于画图。
'''
def Min(lis):
    if not isinstance(lis,list) or not lis:
        return
    start , end = 0,len(lis)-1
    mid = start
    while lis[start] >= lis[end]:
        if end - start == 1:
            mid = end
            break
        mid = start + int((end-start)/2)
        # 如果start,end和mid指向的值都相同，只能顺序查找
        if lis[start]==lis[mid]==lis[end]:
            mid = MinInOrder(lis,start,end)
            break
        if lis[mid] >= lis[start]:#说明mid在前一段序列中
            start = mid
        elif lis[mid] <= lis[end]:#说明mid在后一段序列中
            end = mid
    return lis[mid]

def MinInOrder(lis,start,end):
    val,min = lis[start],start
    for i in range(start,end+1):
        if lis[i]<val:
            val = lis[i]
            min = i
    return min

if __name__ == '__main__':
    lis = [3,4,5,1,2]
    lis1 = [1,2,3,4,5]
    lis2 = [1,0,1,1,1]
    print(Min(lis2))
