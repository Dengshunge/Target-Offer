# 面试题16 数值的整数次方
'''
此题不难，重点是考察了边界条件。
要想要特殊值0和负值。
'''
g_InvalidInput = False
def Power(base,exponent):
    global g_InvalidInput
    g_InvalidInput = False
    if base == 0 and exponent < 0:
        g_InvalidInput = True
        return 0.0
    result = PowerWithUnsighedExponent_quick(base,abs(exponent))
    if exponent < 0:
        result = 1.0 / result
    return result


def PowerWithUnsighedExponent(base,exponent):
    result = 1.0
    for i in range(exponent):
        result *= base
    return result

def PowerWithUnsighedExponent_quick(base,exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    result = PowerWithUnsighedExponent_quick(base,exponent>>1)
    result = result * result # 即平方
    if exponent & 0x1:
        result *= base
    return result


if __name__ == '__main__':
    result = Power(2,-5)
    print(result)
    print(g_InvalidInput)
