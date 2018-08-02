# 面试题5 替换空格
'''
本题有2种方法：
    1.书上的方法，从后往前扫描，减少移动次数。但由于python无法创建固定长度的字符串（除非
        将字符串转换为list），所以都产生一个O(n+x*2)的空间复杂度，其中x为空格的数量。
        时间复杂度为O(n)
    2.利用python的append，从前往后扫描，遇到空格就extend字符串。但如果超过了新建的
        list，会扩容，产生一个移动的损耗。时间复杂度是O(n)

所以遇到这种问题，尝试思考从后面操作。
另外在相关题目中，可以使用的方法有点类似归并排序。
'''

# 面试题5 替换空格
def ReplaceBlank(s1):
    if not isinstance(s1,str):
        print('非字符串')
        return
    lis = list(s1)
    originalLength = len(lis)
    numberOfBlank = 0
    for i in s1:
        if i == ' ':
            numberOfBlank += 1
    newLength = originalLength + numberOfBlank * 2#扩充之后的长度
    lis_rep = [None] * newLength
    indexOfOriginal,indexOfNew = originalLength-1,newLength-1
    while indexOfOriginal >= 0 :
        if lis[indexOfOriginal] == ' ':
            lis_rep[indexOfNew] = '0'
            lis_rep[indexOfNew-1] = '2'
            lis_rep[indexOfNew - 2] = '%'
            indexOfNew -= 3
        else:
            lis_rep[indexOfNew] = lis[indexOfOriginal]
            indexOfNew -= 1
        indexOfOriginal -= 1
    return ''.join(map(str,lis_rep))

#利用list的append，但产生了O(n)的空间复杂度，时间复杂度为O(n)
#其中，如果append超过了list的长度，会扩容，产生一个移动损耗
def ReplaceBlank1(s1):
    if not isinstance(s1,str):
        print('非字符串')
        return
    lis = list(s1)
    lis_rep = []
    for i in lis:
        if i == ' ':
            lis_rep.extend(list('%20'))
        else:
            lis_rep.append(i)
    return ''.join(map(str,lis_rep))


if __name__ == '__main__':
    s1 = ' We are happy '
    s2 = None
    s3 = '    '
    print(ReplaceBlank(s3))
    print(ReplaceBlank1(s3))
