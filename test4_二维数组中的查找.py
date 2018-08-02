# 面试题4 二维数组中的查找
'''
这道题的思路就是从右上角开始寻找，
逐步缩减行和列。
如果不用numpy的话，就要输出参数就要包括行数和列数。
用numpy的话，有个bug，如果lis是一维数组，m,n = np.shape(lis)就会报错，
因为如果lis是一维的话，shape只会返回一个参数。
'''

# 面试题4 二维数组中的查找
import numpy as np
def Find(lis,num):
    # 首先判断其是不是空的list
    if not isinstance(lis,list) or len(lis) == 0:
        print('空的list')
        return False
    m,n = np.shape(lis)
    rows,columns = 0,n-1#行和列
    while rows<m and columns>=0:
        if num == lis[rows][columns]:
            # 当查找到该值，返回true
            return True
        elif num < lis[rows][columns]:
            # 当num小于右上角，说明值在左边
            columns -= 1
        else:
            rows += 1
    return False

if __name__ == '__main__':
    lis = [[1,2,8,9],
           [2,4,9,12],
           [4,7,10,13],
           [6,8,11,15]]
    lis1 = []
    # print(Find(lis, 9.5))
    print(Find(lis1,9))
