'''
面试题3-1和3-2 数组中重复的数字
题目3-1是不知道有无重复且重复多少次，可以利用的方法有：
    1.排序后再扫描，此时排序的时间复杂度为O(nlogn)，扫描的复杂度为O(n)
    2.利用哈希表，创建一个长度为n的list，往里面按下标填数字，当发现此位置已经被填了，说明此数字重复
    3.利用书上的方法：将其两两交换，时间复杂度为O(n)
题目3-2是已经知道至少有一个数字是重复的，且不允许修改原来的list，与上题的前提不同。
    1.创建一个长度为n的list，类似上题的方法2
    2.利用类似于二分查抄的方法（书上的方法）
        这里是将1到n-1的数字对半分，而不是针对原来的list，然后统计对半的数字在原来的list中重复的次数。
        此方法能找到重复的数字，但不能保证找出所有重复的数字
        时间复杂度为O(nlogn)
'''



# 面试题3-1 数组中重复的数字
def duplicate(lis):
    #判断边界条件
    if lis == None or len(lis) == 0:
        print('数组为空')
        return False
    # 判断数字在0到n-1的范围内
    Len = len(lis)
    for i in lis:
        if i < 0 or i> Len-1:
            print('值%d不在范围内' % i)
            return False
    Flag = True#标志位，表示找到第一个重复的数字
    for i in range(Len):
        while i != lis[i]:
            m = lis[i]
            if m == lis[m]:
                Flag = False
                break
            lis[i],lis[m] = lis[m],lis[i]
        if Flag == False:
            break
    if Flag == True:
        print('未找到重复数字')
        return False
    else:
        return lis[i]

# 面试题3-2
def getDupliation(lis):
    #判断边界条件
    if lis == None or len(lis) == 0:
        print('数组为空')
        return False
    # 判断数字在1到n-1的范围内
    Len = len(lis)
    for i in lis:
        if i < 1 or i> Len-1:
            print('值%d不在范围内' % i)
            return False

    start,end = 1,Len-1
    while end >= start:
        middle = int(start + 0.5*(end-start))
        count = countRange(lis,start,middle)
        #如果只有1个数字时，统计出来的count多于1个，则说明这个数字是重复的
        if end == start:
            if count > 1:
                return start
            else:
                print('无重复')
                break

        if count > (middle - start + 1):#若count值大于start到middle的数量，则在其中继续二分查找
            end = middle
        else:
            start = middle + 1
    return False

def countRange(lis,start,end):
    count = 0
    for i in lis:
        if i>=start and i<=end:
            count += 1
    return count

if __name__ == '__main__':
    lis = []
    print(getDupliation(lis))
