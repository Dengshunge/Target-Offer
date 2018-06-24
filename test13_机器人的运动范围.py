# 面试题13 机器人的运动范围
'''
判断位数之和有两种方法：
    1.转化为字符串
    2.通过循环，例如a=101，每次对a进行%10，循环判断条件是a!=0
    https://www.cnblogs.com/54Leo/p/6133270.html
    https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%9C%BA%E5%99%A8%E4%BA%BA%E7%9A%84%E8%BF%90%E5%8A%A8%E8%8C%83%E5%9B%B4.py
和面试题12一样使用回溯法，进行迭代，套路很相近

另外，用visited = [[False] * rows ]* cols这种方式创建二维数组，是个坑，虽然行，但都是array的引用。
应该用test = [[0 for i in range(m)] for j in range(n)]这种方式。
https://www.cnblogs.com/PyLearn/archive/2017/11/06/7795552.html

'''

class Solution:
    def movingCount(self,threshold,rows,cols):
        if threshold < 0 or rows<= 0 or cols <= 0:
            return 0
        visited = [[0 for i in range(rows)]for j in range(cols)]
        count = self.movingCountCore(threshold,rows,cols,0,0,visited)
        return count

    def movingCountCore(self,threshold,rows,cols,i,j,visited):
        count = 0
        if self.check(threshold,rows,cols,i,j,visited):
            a = visited[1][0]
            visited[i][j] = True
            count = 1 + self.movingCountCore(threshold,rows,cols,i-1,j,visited) \
                      + self.movingCountCore(threshold,rows,cols,i+1,j,visited) \
                      + self.movingCountCore(threshold,rows,cols,i,j-1,visited) \
                      + self.movingCountCore(threshold,rows,cols,i,j+1,visited)
        return count

    def check(self, threshold, rows, cols, i, j, visited):
        if 0<=i<rows and 0<=j<cols  and self.getDigitSum(i,j)<= threshold \
                and not visited[i][j]:
            return True
        return False

    def getDigitSum(self,i,j):
        a = 0
        for index in str(i):
            a += int(index)
        for index in str(j):
            a += int(index)
        return a

if __name__ == '__main__':
    a = Solution()
    print(a.movingCount(10,100,100))
