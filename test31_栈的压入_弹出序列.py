# 面试题31 栈的压入，弹出序列
'''
本道题的关键是如果下一个弹出的数字刚好是栈顶数字，那么直接弹出；
否则继续压入数字，直到与下一个弹出的数字相等为止
'''


def IsPopOrder(pPush,pPop):
    if not isinstance(pPush,list) and not isinstance(pPop,list):
        return False
    if len(pPush) != len(pPop):
        return False
    stack = [] # 创建一个辅助栈
    j = 0#用于控制pPop的index
    for i in pPush:
        stack.append(i)
        while stack and stack[-1] == pPop[j]:
            stack.pop()
            j += 1
    if stack:
        #若栈中任然有元素
        return False
    else:
        return True

pPush = [1,2,3,4,5]
pPop = [5,4,3,2,1]
print(IsPopOrder(pPush,pPop))
