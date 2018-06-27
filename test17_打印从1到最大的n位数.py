# 面试题17 打印从1到最大的n位数
'''
此题目用字符串来解决大数字的问题，模拟加法的过程。
'''

def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return
    number = ['0'] * n
    while not Increment(number):
        PrintNumber(number)

def Increment(number):
    isOverflow = False # 表示最大n位加一后有无溢出
    nTakeOver = 0 # 进位标志符
    nLength = len(number)
    for i in range(nLength-1,-1,-1):# 从个位开始计算，至到n位，所以是倒序
        nSum = int(number[i]) + nTakeOver # 表示第n位的值，如果无进位，则nTakeOver=0，如果进位了，则nTakeOver=1
        if i == nLength - 1:#表示个位
            nSum += 1

        if nSum >= 10:#判断是否进位
            if i == 0:  # 当i==0时，说明已经溢出
                isOverflow = True
            else:# 若不是0，说明仍然处于n位之中
                nSum -= 10
                nTakeOver = 1#进位标志符置1
                number[i] = str(nSum)
        else:# 未发生进位
            number[i] = str(nSum)
            break
    return isOverflow

def PrintNumber(number):
    isBeginning0 = True # 表示非零位的开始
    nLength = len(number)

    for i in range(nLength):
        if isBeginning0 and number[i] != '0':# 当number之前为0的话，isBeginning0一直为0，知道遇到第一个非零位
            isBeginning0 = False
        if not isBeginning0:
            print('%c' % number[i],end='')
    print('')

def Print1ToMaxOfNDigits_2(n):
    if n<=0:
        return
    number = ['0'] * n
    for i in range(10):
        number[0] = str(i) # 设置最高位
        Print1ToMaxOfNDigitsRecursively(number,n,0)

# index表示传入时对应是哪一位
def Print1ToMaxOfNDigitsRecursively(number,length,index):
    if index == length - 1:# length-1表示最后一个，即个位
        PrintNumber(number)
        return
    for i in range(10):
        number[index + 1] = str(i)# index+1 下一位
        Print1ToMaxOfNDigitsRecursively(number,length,index+1)

if __name__ == '__main__':
    # Print1ToMaxOfNDigits(2)
    Print1ToMaxOfNDigits_2(3)
