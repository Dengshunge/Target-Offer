# 面试题29 顺时针打印矩阵
'''
本面试题中包含多个循环和多个边界循环判断
很考虑编程的功力
本道题分解成多个圈进行打印

网上有种思路，就是每次打印完一行后，删除这一行并将数组进行旋转。
但旋转的复杂度有点高。

'''

def PrintMatrixClockwisely(matrix):
    if not isinstance(matrix, list):
        return
    m, n = len(matrix), len(matrix[0])
    start = 0
    while m > start * 2 and n > start * 2:
        PrintMatrixInCircle(matrix, m, n, start)
        start += 1

def PrintMatrixInCircle(matrix,rows,columns,start):
    endX, endY = columns - 1 - start, rows - 1 - start
    #从左到右打印一行
    for i in range(start, endX + 1):
        print(matrix[start][i], end=' ')
    #从上到下打印一列
    if endY > start:
        for i in range(start + 1, endY + 1):
            print(matrix[i][endX], end=' ')
    #从右到左打印一行
    if endX > start and endY > start:
        for i in range(endY - 1, start - 1, -1):
            print(matrix[endX][i], end=' ')
    #从下到上打印一列
    if endX > start and endY - 1 > start:
        for i in range(endX - 1, start, -1):
            print(matrix[i][start], end=' ')


if __name__ == '__main__':
    import numpy as np
    matrix = np.arange(1,17).reshape((1,-1))
    matrix = matrix.tolist()
    print(matrix)
    # matrix = [[1]]

    PrintMatrixClockwisely(matrix)
