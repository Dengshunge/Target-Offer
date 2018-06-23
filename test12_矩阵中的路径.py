# 面试题12 矩阵中的路径
'''
此题运用了回溯法，是暴力解法的升级版
首先找到第一个字符的位置，然后进入hasPathCore函数，通过比较下一个字符串的位置来选择进入哪一个分支。
此题修改了原来的lis，如果要求不允许修改，则需要重新建一个副本，不能查找类似lis2和s2的情况。
解决方案是去掉lis[i][j] = '*'，但是这样会出现重复路径的问题。
参考了 https://blog.csdn.net/iyuanshuo/article/details/79649596
'''

def hasPath(lis,s1):
    if not lis or not s1:
        return
    rows,cols = len(lis),len(lis[0])
    for i in range(rows):
        for j in range(cols):
            if lis[i][j] == s1[0]:
                if hasPathCore(lis, s1[1:], rows, cols, i, j):
                    return True
    return False

def hasPathCore(lis,s1,rows,cols,i,j):
    if not s1:
        return True
    # lis[i][j] = '*'
    if j + 1 < cols and s1[0] == lis[i][j+1]:#往右找
        return hasPathCore(lis, s1[1:], rows, cols, i, j + 1)
    elif j - 1 >= 0 and s1[0] == lis[i][j - 1]:#往左找
        return hasPathCore(lis, s1[1:], rows, cols, i, j - 1)
    elif i + 1 < rows and s1[0] == lis[i + 1][j]:#往上找
        return hasPathCore(lis, s1[1:], rows, cols, i + 1, j)
    elif i - 1 >= 0 and s1[0] == lis[i - 1][j]:#往下找
        return hasPathCore(lis, s1[1:], rows, cols, i - 1, j)
    else:
        return False


if __name__ == '__main__':
    lis = [list('abtg'),
           list('bbbb'),
           list('cfcs'),
           list('jdeh')]
    lis2 = [list('abfe'),
            list('abcd'),
            list('adce')]
    s1 = 'bfce'
    s2 = 'bbfe'
    print(hasPath(lis,s1))
