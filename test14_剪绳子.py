# 面试题14 剪绳子
'''
此道题有2中方法，动态规划和贪婪算法
在运用动态规划之前要分析能否把大问题分解成小问题，分解后的每个小问题也存在最优解。
如果把小问题的最优解组合起来能够得到整个问题的最优解，则可以运用动态规划。
这个思路有点类似于递归，但动态规划是自下而上的计算

把小问题的最优解存储起来，然后组合成最优解。
'''

# 时间复杂度为O(n^2),空间复杂度为O(n)
def maxProductAferCutting_solution1(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    products = [0] * (length+1)
    products[1] = 1
    products[2] = 2
    products[3] = 3#长度为3的线段，如果不切分的话，长度是最大的，所以这里3个数字是不切分时的最大长度。

    for n in range(4,length+1):
        max = 0
        for i in range(1,int(n/2) + 1):#因为是对称的，所以一半
            product = products[i] * products[n-i]
            if max < product:
                max = product
        products[n] = max
    return products[length]

# 时间和空间复杂度都为O(1)
def maxProductAferCutting_solution2(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    timesOf3 = length // 3
    # 当绳子最后剩下的长度为4时，不要再减去长度为3的绳子
    # 而是把绳子剪成长度为2的两端。
    # 所以下面一行的判断就是判断剩下的长度是否为4
    if length - timesOf3 * 3 == 1:
        timesOf3 -= 1

    # 应该有3种情况：
    # 1.当剩下长度为0，即能被3整除，此时timesOf2为0，所以最后的return的后面项是'*1'
    # 2.剩下长度为1，即绳子最后的长度为4
    # 3.剩下长度为2，此时此时timesOf2为1，所以最后的return的后面项是'*2'
    timesOf2 = (length - timesOf3 * 3) / 2

    return int(pow(3,timesOf3) * pow(2,timesOf2))


if __name__ == '__main__':
    print(maxProductAferCutting_solution1(10))
    print(maxProductAferCutting_solution2(10))
