# 面试题10 菲波那切数列
'''
如果采用递归的话，数字过大会导致栈溢出。
有一个办法就是讲计算的结果保存下来，不需要重复计算，这样能优化一下性能。
但还是推荐非递归版本。
'''
# 递归版本
def Fibonacci_Recursion(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci_Recursion(num-1)+Fibonacci_Recursion(num-2)

# 非递归版本
def Fibonacci_Loop(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        One,Two,fibN = 0,1,0
        for i in range(2,num+1):
            fibN = One+Two
            One,Two = Two,fibN
        return fibN

if __name__=='__main__':
    print(Fibonacci_Recursion(10))
    print(Fibonacci_Loop(10))
