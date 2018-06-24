# 面试题13 机器人的运动范围
'''
判断位数之和有两种方法：
    1.转化为字符串
    2.通过循环，例如a=101，每次对a进行%10，循环判断条件是a!=0
    https://www.cnblogs.com/54Leo/p/6133270.html
    https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%9C%BA%E5%99%A8%E4%BA%BA%E7%9A%84%E8%BF%90%E5%8A%A8%E8%8C%83%E5%9B%B4.py
和面试题12一样使用回溯法，进行迭代，套路很相近
'''

class Solution:
    def movingCount(self,threshold,rows,cols):
        if threshold < 0 or rows<= 0 or cols <= 0:
            return 0
        visited = [False] * (rows * cols)
        count = self.movingCountCore(threshold,rows,cols,0,0,visited)
        return count

    def movingCountCore(self,threshold,rows,cols,i,j,visited):
        count = 0
        if self.check(threshold,rows,cols,i,j,visited):
            visited[i * cols + j] = True
            count = 1 + self.movingCountCore(threshold,rows,cols,i-1,j,visited) \
                      + self.movingCountCore(threshold,rows,cols,i+1,j,visited) \
                      + self.movingCountCore(threshold,rows,cols,i,j-1,visited) \
                      + self.movingCountCore(threshold,rows,cols,i,j+1,visited)
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if 0<=row<rows and 0<=col<cols  and (self.getDigitSum(row,col)<= threshold) \
                and not visited[row * cols + col]:
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
