# 面试题15 二进制中1的个数
'''
由于python的整数没有上限，没有溢出的说法。
所以对于负数的处理，可以先*-1，让其正数在计算。
书上给了2种方法，对1进行左移和将本身与本身减1做位与运算。
一个整数减去1，再和原整数做位于运算，会把该整数最右边的1变成0。
另外，左移比右移考虑的问题要少。如果负数右移，会在最高位补1，而不是0.

别人给出了一种方法，将数字变成二进制，然后用count来统计1出现的次数。
https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%B8%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.py
'''
def NumberOf1_1(num):
    count , flag = 0 , 1
    if num < 0:
        num *= -1
        count = 1
    while flag and flag <= num:
        if num & flag :
            count += 1
        flag = flag << 1
    return count

def NumberOf1_2(num):
    count = 0
    if num < 0:
        num = num&0xffffffff
    while num:
        count += 1
        num = (num-1) & num
    return count


if __name__ == '__main__':
    print(NumberOf1_1(11))
    print(NumberOf1_2(-11))
