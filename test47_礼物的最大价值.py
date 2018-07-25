# 面试题47 礼物的最大价值
'''
使用动态规划，f(i,j)=max{f(i-1,j),f(i,j-1)}+gift[i,j]
此时求出每个点的最大价值
如果时贪心算法的话，每次会现在价值最大的那条路，此时会陷入局部最小值，而且结果时不正确的。
例如
1,2,2,2
1,1,1,2
10,10,10,2
如果用贪心算法的话，会沿着值为2的路径走，此时就会出现错误。
如果用动态规划的话，先创建一个同等大小的矩阵，然后救出每个点的最大价值，输出最后一个点。
'''

class Solution:
    def getMaxValue_solution1(self,values):
        if not values:
            return 0
        cols,rows = len(values),len(values[0])
        maxValues = [[0 for i in range(rows)] for i in range(cols)]
        for i in range(cols):
            for j in range(rows):
                left ,up = 0,0
                if i > 0:
                    up = maxValues[i-1][j]
                if j > 0:
                    left = maxValues[i][j-1]
                maxValues[i][j] = max(up,left) + values[i][j]
        print(maxValues[cols-1][rows-1])


values=[[1,10,3,8],
        [12,2,9,6],
        [5,7,4,11],
        [3,7,16,5]]
a = Solution()
a.getMaxValue_solution1(values)
